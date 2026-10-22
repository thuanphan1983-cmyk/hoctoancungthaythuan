import React, { useState, useMemo } from 'react';
import {
  BookOpen, CheckCircle, Lock, Unlock, Camera, Upload,
  FileText, Download, BarChart2, Award, RefreshCw,
  Sparkles, FileSpreadsheet, Trash2, ChevronRight, Check, X
} from 'lucide-react';
import MathView from './components/MathView';
import { CURRICULUM_KNTT } from './data/curriculum';
import { getExamFromBank } from './data/examBank';
import {
  generateExamAI,
  gradeEssayVisionAI,
  generateFourPartDetailedFeedback,
  compressImage
} from './services/geminiService';
import { calculateTrueFalseScore, normalizeShortAnswer } from './utils/scoring';
import { exportResultToPDF } from './utils/exportPdf';
import { exportSubmissionsToExcel, exportSubmissionsToCSV } from './utils/exportExcel';

export default function App() {
  // Cấu hình API Key
  const [apiKey, setApiKey] = useState(() => localStorage.getItem("GEMINI_API_KEY") || "");
  const [toast, setToast] = useState(null); // { type: 'warning' | 'info' | 'success', message: '' }
  const toastTimerRef = useRef(null);
  const [showKeyModal, setShowKeyModal] = useState(false);
  const [showEssayKeyModal, setShowEssayKeyModal] = useState(false);
  const [tempKeyInput, setTempKeyInput] = useState("");

  const showToast = (type, message) => {
    if (toastTimerRef.current) clearTimeout(toastTimerRef.current);
    setToast({ type, message });
    toastTimerRef.current = setTimeout(() => {
      setToast(null);
    }, 6000);
  };

  // Thông tin học sinh & lựa chọn bài học
  const [studentName, setStudentName] = useState("");
  const [className, setClassName] = useState("9A1");
  const [selectedGrade, setSelectedGrade] = useState("9"); // Mặc định Toán 9 (trọng tâm)
  const [selectedChapter, setSelectedChapter] = useState(CURRICULUM_KNTT["9"].chapters[0].id);
  const [selectedLesson, setSelectedLesson] = useState(CURRICULUM_KNTT["9"].chapters[0].lessons[0]);
  const [selectedTestNum, setSelectedTestNum] = useState(1); // 1, 2, hoặc 3

  // Trạng thái màn hình: 'setup' | 'exam' | 'result' | 'dashboard'
  const [view, setView] = useState("setup");
  const [loadingAI, setLoadingAI] = useState(false);
  const [examData, setExamData] = useState(() => getExamFromBank("9", "c1_9", "Bài 1: Khái niệm phương trình và hệ hai phương trình bậc nhất hai ẩn", 1));

  // Trạng thái làm bài của học sinh
  const [mcAnswers, setMcAnswers] = useState({}); // { 0: optIndex, 1: optIndex }
  const [mcLockedIndex, setMcLockedIndex] = useState(0); // Câu hiện tại đang mở (0 -> 11)
  const [tfAnswers, setTfAnswers] = useState({ 1: {}, 2: {} });
  const [saAnswers, setSaAnswers] = useState({ 1: "", 2: "", 3: "", 4: "" });
  const [essayImages, setEssayImages] = useState({ 1: null, 2: null, 3: null }); // DataURL ảnh chụp
  const [sharedEssayImage, setSharedEssayImage] = useState(null); // Ảnh chụp chung cả 3 câu tự luận
  const [zoomImage, setZoomImage] = useState(null); // Modal phóng to ảnh
  const [gradingProgress, setGradingProgress] = useState(""); // Tiến độ chấm bài

  // Lọc Dashboard
  const [filterClass, setFilterClass] = useState("ALL");

  // Kết quả thi & Lịch sử
  const [resultData, setResultData] = useState(null);
  const [submissions, setSubmissions] = useState(() => {
    try {
      const saved = localStorage.getItem("MATH_SUBMISSIONS_KNTT");
      return saved ? JSON.parse(saved) : [];
    } catch (e) {
      return [];
    }
  });

  // Đổi khối lớp
  const handleGradeChange = (grade) => {
    setSelectedGrade(grade);
    const firstChap = CURRICULUM_KNTT[grade]?.chapters[0];
    if (firstChap) {
      setSelectedChapter(firstChap.id);
      setSelectedLesson(firstChap.lessons[0]);
    }
  };

  // Đổi chương
  const handleChapterChange = (chapId) => {
    setSelectedChapter(chapId);
    const chap = CURRICULUM_KNTT[selectedGrade]?.chapters.find((c) => c.id === chapId);
    if (chap && chap.lessons.length > 0) {
      setSelectedLesson(chap.lessons[0]);
    }
  };

  // Lưu API Key
  const saveApiKey = (key) => {
    setApiKey(key);
    localStorage.setItem("GEMINI_API_KEY", key);
  };

  // ==========================================
  // LUỒNG TIÊU CHUẨN: BỐC THẲNG ĐỀ TĨNH (KHÔNG CẦN KEY)
  // ==========================================
  const handleStartStandardExam = (isFallback = false) => {
    if (!studentName.trim() || !className.trim()) {
      alert("Vui lòng nhập đầy đủ Họ và tên học sinh cùng Lớp đăng ký!");
      return;
    }

    setMcAnswers({});
    setMcLockedIndex(0);
    setTfAnswers({ 1: {}, 2: {} });
    setSaAnswers({ 1: "", 2: "", 3: "", 4: "" });
    setEssayImages({ 1: null, 2: null, 3: null });
    setSharedEssayImage(null);
    setLoadingAI(false);

    const bankExam = getExamFromBank(selectedGrade, selectedChapter, selectedLesson, selectedTestNum);
    setExamData(bankExam);
    setView("exam");

    if (isFallback) {
      showToast(
        "warning",
        "Mô hình AI đang bận, hệ thống tự động kích hoạt Đề thi chuẩn để bạn tiếp tục làm bài!"
      );
    }
  };

  // ==========================================
  // LUỒNG AI: SINH ĐỀ AI CÁ NHÂN HÓA (CÓ FALLBACK)
  // ==========================================
  const handleStartAIGeneratedExam = async () => {
    if (!studentName.trim() || !className.trim()) {
      alert("Vui lòng nhập đầy đủ Họ và tên học sinh cùng Lớp đăng ký!");
      return;
    }

    const cleanKey = apiKey.trim();
    if (!cleanKey) {
      setTempKeyInput("");
      setShowKeyModal(true);
      return;
    }

    setMcAnswers({});
    setMcLockedIndex(0);
    setTfAnswers({ 1: {}, 2: {} });
    setSaAnswers({ 1: "", 2: "", 3: "", 4: "" });
    setEssayImages({ 1: null, 2: null, 3: null });
    setSharedEssayImage(null);
    setLoadingAI(true);

    try {
      const currentChap = CURRICULUM_KNTT[selectedGrade]?.chapters.find((c) => c.id === selectedChapter);
      const newExam = await generateExamAI({
        apiKey: cleanKey,
        grade: selectedGrade,
        lesson: selectedLesson,
        testNum: selectedTestNum,
        chapterTitle: currentChap?.title || ""
      });
      setLoadingAI(false);
      setExamData(newExam);
      setView("exam");
      showToast("success", "Đã khởi tạo bộ đề AI cá nhân hóa thành công!");
    } catch (err) {
      console.warn("Lỗi sinh đề AI (kích hoạt fallback):", err);
      setLoadingAI(false);
      handleStartStandardExam(true);
    }
  };

  const handleStartExam = handleStartStandardExam;

  // ==========================================
  // TẢI ẢNH BÀI LÀM TỰ LUẬN
  // ==========================================
  const handleImageUpload = async (qId, e) => {
    const file = e.target.files && e.target.files[0];
    if (!file) return;
    try {
      const compressed = await compressImage(file);
      if (qId === "shared") {
        setSharedEssayImage(compressed);
      } else {
        setEssayImages((prev) => ({ ...prev, [qId]: compressed }));
      }
    } catch (err) {
      console.error("Lỗi nén ảnh:", err);
    }
  };

  // ==========================================
  // NỘP BÀI & CHẤM ĐIỂM TỰ ĐỘNG
  // ==========================================
  const handleSubmitExam = async () => {
    if (Object.keys(mcAnswers).length < 12) {
      const confirmSubmit = window.confirm("Em chưa hoàn thành hết 12 câu trắc nghiệm. Em vẫn muốn nộp bài?");
      if (!confirmSubmit) return;
    }

    setLoadingAI(true);

    // 1. Chấm Phần I (12 câu x 0.25đ = 3.0đ)
    let scorePart1 = 0;
    let mcCorrectCount = 0;
    examData.part1.forEach((q, idx) => {
      if (mcAnswers[idx] === q.correct) {
        scorePart1 += 0.25;
        mcCorrectCount++;
      }
    });

    // 2. Chấm Phần II (2 câu Đúng/Sai = 2.0đ, chấm lũy tiến Bộ GD&ĐT)
    let scorePart2 = 0;
    const tfDetails = {};
    examData.part2.forEach((q) => {
      const s = calculateTrueFalseScore(tfAnswers[q.id], q.statements);
      scorePart2 += s;
      tfDetails[q.id] = s;
    });

    // 3. Chấm Phần III (4 câu Trả lời ngắn x 0.5đ = 2.0đ)
    let scorePart3 = 0;
    let saCorrectCount = 0;
    examData.part3.forEach((q) => {
      if (normalizeShortAnswer(saAnswers[q.id]) === normalizeShortAnswer(q.answer)) {
        scorePart3 += 0.5;
        saCorrectCount++;
      }
    });

    // 4. Chấm Phần IV (3 câu Tự luận x 1.0đ = 3.0đ) qua Gemini Vision
    let scorePart4 = 0;
    const essayFeedbacks = {};

    for (const q of examData.part4) {
      const imgDataUrl = essayImages[q.id] || sharedEssayImage;
      if (imgDataUrl) {
        const fb = await gradeEssayVisionAI({
          apiKey,
          question: q.question,
          rubric: q.rubric,
          level: q.level,
          imgDataUrl,
          questionId: q.id
        });
        scorePart4 += fb.score;
        essayFeedbacks[q.id] = { ...fb, usedImage: imgDataUrl };
      } else {
        essayFeedbacks[q.id] = {
          score: 0,
          ocrText: "(Chưa nộp ảnh chụp bài làm)",
          steps: [
            { step: "Chưa nộp bài làm viết tay", awarded: 0, max: 1.0, status: "Chưa làm", note: "Không có ảnh chụp bài làm để chấm." }
          ],
          mistakes: "Chưa nộp ảnh bài làm.",
          comment: "Học sinh chưa nộp ảnh chụp bài làm cho câu này (0.0 / 1.0 điểm).",
          modelSolution: `Lời giải chuẩn tham khảo: ${q.rubric}`,
          usedImage: null
        };
      }
    }

    const totalScore = Number((scorePart1 + scorePart2 + scorePart3 + scorePart4).toFixed(2));

    // Tạo nhận xét CHI TIẾT CẢ 4 PHẦN (Trắc nghiệm, Đúng/Sai, Trả lời ngắn, Tự luận)
    const feedbacks = await generateFourPartDetailedFeedback({
      apiKey,
      studentName,
      className: className.toUpperCase().trim(),
      lesson: selectedLesson,
      testNum: selectedTestNum,
      scorePart1,
      scorePart2: Number(scorePart2.toFixed(2)),
      scorePart3,
      scorePart4: Number(scorePart4.toFixed(2)),
      totalScore,
      mcCorrectCount,
      saCorrectCount
    });

    const finalRecord = {
      id: Date.now(),
      timestamp: new Date().toLocaleString("vi-VN"),
      studentName,
      className: className.toUpperCase().trim(),
      grade: selectedGrade,
      lesson: selectedLesson,
      testNum: selectedTestNum,
      scorePart1,
      scorePart2: Number(scorePart2.toFixed(2)),
      scorePart3,
      scorePart4: Number(scorePart4.toFixed(2)),
      totalScore,
      tfDetails,
      essayFeedbacks,
      feedbacks,
      overallTeacherComment: feedbacks.overall
    };

    const updated = [finalRecord, ...submissions];
    setSubmissions(updated);
    try {
      localStorage.setItem("MATH_SUBMISSIONS_KNTT", JSON.stringify(updated));
    } catch (e) {
      console.warn("LocalStorage full:", e);
    }

    setResultData(finalRecord);
    setLoadingAI(false);
    setView("result");
  };

  // Thống kê theo lớp
  const filteredSubs = useMemo(() => {
    if (filterClass === "ALL") return submissions;
    return submissions.filter((s) => s.className === filterClass);
  }, [submissions, filterClass]);

  const uniqueClasses = useMemo(() => {
    const s = new Set(submissions.map((x) => x.className));
    return Array.from(s).sort();
  }, [submissions]);

  const classStats = useMemo(() => {
    if (filteredSubs.length === 0) return null;
    const total = filteredSubs.reduce((acc, cur) => acc + cur.totalScore, 0);
    const avg = (total / filteredSubs.length).toFixed(2);
    const gioi = filteredSubs.filter((s) => s.totalScore >= 8).length;
    const kha = filteredSubs.filter((s) => s.totalScore >= 6.5 && s.totalScore < 8).length;
    const dat = filteredSubs.filter((s) => s.totalScore >= 5 && s.totalScore < 6.5).length;
    const chuaDat = filteredSubs.filter((s) => s.totalScore < 5).length;

    return { avg, gioi, kha, dat, chuaDat, count: filteredSubs.length };
  }, [filteredSubs]);

  return (
    <div className="min-h-screen bg-slate-50 text-slate-800 font-sans flex flex-col">
      {/* HEADER */}
      <header className="bg-indigo-900 text-white shadow-md sticky top-0 z-50 print:hidden">
        <div className="max-w-6xl mx-auto px-4 py-3.5 flex flex-wrap items-center justify-between gap-4">
          <div className="flex items-center gap-3">
            <div className="bg-amber-400 text-indigo-950 p-2.5 rounded-xl font-bold flex items-center justify-center shadow">
              <BookOpen className="w-5 h-5" />
            </div>
            <div>
              <h1 className="text-base md:text-lg font-black tracking-tight flex items-center gap-2">
                HỆ THỐNG KIỂM TRA TOÁN THCS (KẾT NỐI TRI THỨC)
                <span className="text-[10px] bg-amber-400 text-slate-950 px-2 py-0.5 rounded-full font-bold">LỚP 8 & 9</span>
              </h1>
              <p className="text-xs text-indigo-200">
                Chuẩn Ma trận 2025 Bộ GD&ĐT • Khóa tuần tự Phần I • Nhận xét cả 4 phần • Chấm Tự luận AI Vision
              </p>
            </div>
          </div>

          <div className="flex items-center gap-2">
            <button
              onClick={() => setView("setup")}
              className={`px-3.5 py-2 rounded-xl text-xs md:text-sm font-semibold transition flex items-center gap-1.5 ${
                view === "setup" ? "bg-white text-indigo-950 shadow" : "bg-indigo-800 hover:bg-indigo-700 text-white"
              }`}
            >
              <FileText className="w-4 h-4" /> Làm bài kiểm tra
            </button>
            <button
              onClick={() => setView("dashboard")}
              className={`px-3.5 py-2 rounded-xl text-xs md:text-sm font-semibold flex items-center gap-1.5 transition ${
                view === "dashboard" ? "bg-white text-indigo-950 shadow" : "bg-indigo-800 hover:bg-indigo-700 text-white"
              }`}
            >
              <BarChart2 className="w-4 h-4" /> Thống kê lớp ({submissions.length})
            </button>
          </div>
        </div>
      </header>

      <main className="flex-1 max-w-5xl w-full mx-auto p-4 md:p-6">
        {/* ============================================================== */}
        {/* MÀN HÌNH 1: THIẾT LẬP BÀI KIỂM TRA                              */}
        {/* ============================================================== */}
        {view === "setup" && (
          <div className="bg-white rounded-2xl shadow-sm border border-slate-200 p-6 md:p-8 space-y-6">
            <div className="border-b pb-4 flex flex-wrap justify-between items-center gap-4">
              <div>
                <h2 className="text-xl font-bold text-slate-900">Thiết lập Bài kiểm tra Định kỳ theo Bài học</h2>
                <p className="text-xs md:text-sm text-slate-500 mt-0.5">
                  Đầy đủ chương trình Toán 6, 7, 8, 9 (Trọng tâm Toán 8 và Toán 9). Mỗi bài học có đúng 3 đề độc lập.
                </p>
              </div>
              <div className="flex flex-col items-end gap-1">
                <div className="text-[11px] font-medium text-slate-500">
                  Google Gemini API Key <span className="text-slate-400 font-normal">(Tùy chọn - Dùng cho Sinh đề AI & Chấm tự luận)</span>
                </div>
                <input
                  type="password"
                  placeholder="Nhập Gemini API Key nếu muốn sinh đề AI..."
                  value={apiKey}
                  onChange={(e) => saveApiKey(e.target.value)}
                  className="text-xs border border-slate-300 rounded-lg px-3 py-1.5 w-72 focus:ring-2 focus:ring-indigo-500 outline-none bg-slate-50"
                />
              </div>
            </div>

            {/* Thông tin học sinh */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4 bg-indigo-50/70 p-4 rounded-xl border border-indigo-100">
              <div>
                <label className="block text-xs font-bold uppercase text-indigo-900 mb-1">
                  Họ và tên Học sinh *
                </label>
                <input
                  type="text"
                  placeholder="VD: Nguyễn Văn An"
                  value={studentName}
                  onChange={(e) => setStudentName(e.target.value)}
                  className="w-full px-3.5 py-2.5 rounded-lg border border-slate-300 focus:ring-2 focus:ring-indigo-600 outline-none bg-white text-sm"
                />
              </div>
              <div>
                <label className="block text-xs font-bold uppercase text-indigo-900 mb-1">
                  Lớp đăng ký (Dùng để thống kê) *
                </label>
                <input
                  type="text"
                  placeholder="VD: 9A1, 8B, 7A2..."
                  value={className}
                  onChange={(e) => setClassName(e.target.value)}
                  className="w-full px-3.5 py-2.5 rounded-lg border border-slate-300 focus:ring-2 focus:ring-indigo-600 outline-none bg-white uppercase text-sm font-semibold"
                />
              </div>
            </div>

            {/* Chọn khối, chương, bài */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div className="space-y-4">
                <div>
                  <label className="block text-xs font-bold uppercase text-slate-600 mb-2">
                    1. Khối lớp (Bộ sách Kết nối tri thức)
                  </label>
                  <div className="grid grid-cols-4 gap-2">
                    {["8", "9", "6", "7"].map((g) => (
                      <button
                        key={g}
                        onClick={() => handleGradeChange(g)}
                        className={`py-2.5 rounded-xl font-bold text-sm border transition relative ${
                          selectedGrade === g
                            ? "bg-indigo-600 text-white border-indigo-600 shadow-sm"
                            : "bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100"
                        }`}
                      >
                        Toán {g}
                        {(g === "8" || g === "9") && (
                          <span className="absolute -top-1.5 -right-1 text-[9px] bg-amber-400 text-slate-950 px-1 rounded font-bold">
                            Trọng tâm
                          </span>
                        )}
                      </button>
                    ))}
                  </div>
                </div>

                <div>
                  <label className="block text-xs font-bold uppercase text-slate-600 mb-2">
                    2. Chọn Chương học ({CURRICULUM_KNTT[selectedGrade]?.chapters.length || 0} chương)
                  </label>
                  <select
                    value={selectedChapter}
                    onChange={(e) => handleChapterChange(e.target.value)}
                    className="w-full p-2.5 rounded-xl border border-slate-300 bg-white text-sm font-medium focus:ring-2 focus:ring-indigo-600 outline-none"
                  >
                    {CURRICULUM_KNTT[selectedGrade]?.chapters.map((chap) => (
                      <option key={chap.id} value={chap.id}>
                        {chap.title}
                      </option>
                    ))}
                  </select>
                </div>

                <div>
                  <label className="block text-xs font-bold uppercase text-slate-600 mb-2">
                    3. Chọn Bài học cụ thể
                  </label>
                  <select
                    value={selectedLesson}
                    onChange={(e) => setSelectedLesson(e.target.value)}
                    className="w-full p-2.5 rounded-xl border border-slate-300 bg-white text-sm font-medium focus:ring-2 focus:ring-indigo-600 outline-none"
                  >
                    {CURRICULUM_KNTT[selectedGrade]?.chapters
                      .find((c) => c.id === selectedChapter)
                      ?.lessons.map((les) => (
                        <option key={les} value={les}>
                          {les.toLowerCase().includes("cuối chương") ? `⭐ [Đề tổng hợp] ${les}` : les}
                        </option>
                      ))}
                  </select>
                </div>
              </div>

              <div className="space-y-4">
                <div>
                  <label className="block text-xs font-bold uppercase text-slate-600 mb-2">
                    4. Chọn Đề kiểm tra (Phân hóa độ khó tăng dần: Đề 1 &lt; Đề 2 &lt; Đề 3)
                  </label>
                  <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
                    {[
                      {
                        num: 1,
                        title: "Bài kiểm tra số 1",
                        level: "Cơ bản & Chuẩn kiến thức",
                        scoreRange: "Mục tiêu 5.0 - 7.0 điểm",
                        badge: "🌱 Mức độ Cơ bản",
                        badgeColor: "bg-emerald-100 text-emerald-800 border-emerald-300",
                        desc: "Bám sát chuẩn SGK, hỏi trực tiếp định nghĩa, công thức cơ bản."
                      },
                      {
                        num: 2,
                        title: "Bài kiểm tra số 2",
                        level: "Khá & Vận dụng linh hoạt",
                        scoreRange: "Mục tiêu 7.0 - 8.5 điểm",
                        badge: "🚀 Mức độ Khá (Khó hơn Đề 1)",
                        badgeColor: "bg-blue-100 text-blue-800 border-blue-300",
                        desc: "Khó hơn Đề 1 rõ rệt: biến đổi nhiều bước, bài toán thực tế trung bình."
                      },
                      {
                        num: 3,
                        title: "Bài kiểm tra số 3",
                        level: "Giỏi & Phân hóa sâu",
                        scoreRange: "Mục tiêu 8.5 - 10.0 điểm",
                        badge: "🔥 Nâng cao (Khó nhất)",
                        badgeColor: "bg-purple-100 text-purple-800 border-purple-300",
                        desc: "Độ khó cao nhất, phân hóa sâu cho HSG và thi vào 10 (chốt điểm 10)."
                      }
                    ].map((item) => (
                      <button
                        key={item.num}
                        type="button"
                        onClick={() => setSelectedTestNum(item.num)}
                        className={`p-3.5 rounded-xl border-2 text-left transition relative flex flex-col justify-between ${
                          selectedTestNum === item.num
                            ? "border-indigo-600 bg-indigo-50/70 shadow-md ring-2 ring-indigo-500/20"
                            : "border-slate-200 bg-white hover:border-slate-300 hover:bg-slate-50/70"
                        }`}
                      >
                        <div>
                          <div className="flex items-center justify-between mb-1.5">
                            <span className="text-sm font-black text-slate-900">{item.title}</span>
                            <span className={`text-[10px] font-bold px-2 py-0.5 rounded-full border ${item.badgeColor}`}>
                              {item.badge}
                            </span>
                          </div>
                          <div className="text-xs font-bold text-indigo-950 mb-1">{item.level}</div>
                          <div className="text-[11px] text-slate-500 leading-snug">{item.desc}</div>
                        </div>
                        <div className="mt-3 pt-2 border-t border-slate-100 text-[10px] font-bold text-slate-600 flex items-center justify-between">
                          <span className="text-indigo-700">{item.scoreRange}</span>
                          {selectedTestNum === item.num && (
                            <span className="text-emerald-700 font-extrabold flex items-center gap-1">
                              ✓ Đang chọn
                            </span>
                          )}
                        </div>
                      </button>
                    ))}
                  </div>

                  {/* BANNER HƯỚNG DẪN MỨC ĐỘ KHÓ */}
                  <div className="mt-2.5 p-3 rounded-xl border text-xs leading-relaxed flex items-start gap-2.5 bg-slate-50 border-slate-200">
                    <span className="text-base">
                      {selectedTestNum === 1 ? "🌱" : selectedTestNum === 2 ? "🚀" : "🔥"}
                    </span>
                    <div>
                      <span className="font-bold text-slate-900">
                        {selectedTestNum === 1
                          ? "Cấu trúc Đề số 1 (Đề chuẩn cơ bản): "
                          : selectedTestNum === 2
                          ? "Cấu trúc Đề số 2 (Độ khó cao hơn Đề 1): "
                          : "Cấu trúc Đề số 3 (Độ khó cao nhất - Phân hóa học sinh giỏi): "}
                      </span>
                      <span className="text-slate-700">
                        {selectedTestNum === 1
                          ? "Tập trung củng cố kiến thức nền tảng SGK. Các câu hỏi hỏi trực tiếp công thức và ví dụ mẫu. Thích hợp cho mọi học sinh rèn luyện nắm chắc điểm 5 đến 7."
                          : selectedTestNum === 2
                          ? "Nâng cao độ khó so với Đề 1, yêu cầu biến đổi nhiều bước, giải toán thực tế và kết hợp nhiều kiến thức. Phù hợp mục tiêu điểm 7 đến 8.5."
                          : "Độ khó cao nhất, chứa các dạng bài phân hóa sâu sắc (chứa tham số m, cực trị hình học, bất đẳng thức GTLN/GTNN). Phù hợp ôn thi vào lớp 10 và bồi dưỡng HSG."}
                      </span>
                    </div>
                  </div>
                </div>

                {/* Tóm tắt ma trận 10 điểm */}
                <div className="bg-slate-50 p-4 rounded-xl border border-slate-200 text-xs space-y-1.5">
                  <div className="font-bold text-slate-800 uppercase tracking-wide">
                    Ma trận Đề kiểm tra chuẩn Bộ GD&ĐT (10,0 điểm):
                  </div>
                  <ul className="space-y-1 text-slate-600">
                    <li>• <b>Phần I (3,0đ):</b> 12 câu Trắc nghiệm (0,25đ/câu) - Khóa tuần tự Câu 1 → 12.</li>
                    <li>• <b>Phần II (2,0đ):</b> 2 câu Đúng/Sai (1,0đ/câu) - Chấm lũy tiến 0,1 - 0,25 - 0,5 - 1,0đ.</li>
                    <li>• <b>Phần III (2,0đ):</b> 4 câu Trả lời ngắn (0,5đ/câu) - Điền số nguyên hoặc số thập phân.</li>
                    <li>• <b>Phần IV (3,0đ):</b> 3 câu Tự luận (1,0đ/câu) - Chụp ảnh bài giải, AI Vision chấm chi tiết.</li>
                  </ul>
                </div>
              </div>
            </div>

            <div className="pt-4 flex flex-col sm:flex-row justify-end items-stretch sm:items-center gap-3">
              {/* Nút 1: Làm bài ngay (Đề Chuẩn) - Nổi bật, KHÔNG yêu cầu API Key */}
              <button
                type="button"
                onClick={() => handleStartStandardExam(false)}
                disabled={loadingAI}
                className="bg-gradient-to-r from-indigo-600 to-blue-600 hover:from-indigo-700 hover:to-blue-700 text-white font-bold px-6 py-3.5 rounded-xl shadow-lg hover:shadow-indigo-500/25 flex items-center justify-center gap-2.5 transition transform active:scale-95 text-sm sm:text-base border border-indigo-400/30"
              >
                <BookOpen className="w-5 h-5" />
                <span>Làm bài ngay (Đề Chuẩn)</span>
              </button>

              {/* Nút 2: Sinh đề AI Cá nhân hóa - Yêu cầu Key & Fallback */}
              <button
                type="button"
                onClick={handleStartAIGeneratedExam}
                disabled={loadingAI}
                className="bg-white hover:bg-purple-50 text-purple-700 border-2 border-purple-400 hover:border-purple-600 font-bold px-6 py-3.5 rounded-xl shadow-md flex items-center justify-center gap-2.5 transition transform active:scale-95 text-sm sm:text-base disabled:opacity-50"
              >
                {loadingAI ? (
                  <>
                    <RefreshCw className="w-5 h-5 animate-spin" />
                    <span>Đang kết nối Gemini AI...</span>
                  </>
                ) : (
                  <>
                    <Sparkles className="w-5 h-5" />
                    <span>Sinh đề AI Cá nhân hóa</span>
                  </>
                )}
              </button>
            </div>
          </div>
        )}

        {/* ============================================================== */}
        {/* MÀN HÌNH 2: LÀM BÀI KIỂM TRA                                    */}
        {/* ============================================================== */}
        {view === "exam" && (
          <div className="space-y-6">
            {/* Banner đầu bài */}
            <div className="bg-white p-5 rounded-2xl shadow-sm border border-slate-200 flex flex-wrap justify-between items-center gap-4">
              <div>
                <span className="text-xs font-bold uppercase px-2.5 py-1 bg-indigo-100 text-indigo-800 rounded-md">
                  Khối {selectedGrade} • Lớp {className.toUpperCase()}
                </span>
                <h2 className="text-lg font-bold text-slate-900 mt-1">
                  <MathView text={examData.title} />
                </h2>
                <p className="text-xs text-slate-500 mt-0.5">Học sinh: <b>{studentName}</b></p>
              </div>
              <div className="text-right">
                <div className="text-xs text-slate-500">Tiến độ Phần I</div>
                <div className="text-lg font-black text-indigo-600">
                  {Object.keys(mcAnswers).length} / 12 câu
                </div>
              </div>
            </div>

            {/* PHẦN I: 12 CÂU TRẮC NGHIỆM TUẦN TỰ */}
            <section className="bg-white p-6 rounded-2xl shadow-sm border border-slate-200 space-y-4">
              <div className="border-b pb-3">
                <h3 className="text-sm md:text-base font-bold text-indigo-950 uppercase">
                  Phần I. Câu trắc nghiệm nhiều lựa chọn (3,0 điểm - 0,25 điểm/câu)
                </h3>
                <p className="text-xs text-amber-700 font-medium mt-0.5">
                  * Ràng buộc bắt buộc: Học sinh phải chọn đáp án và xác nhận xong Câu 1 mới được mở Câu 2, tiếp tục tuần tự cho đến Câu 12.
                </p>
              </div>

              <div className="space-y-4">
                {examData.part1.map((q, index) => {
                  const isUnlocked = index <= mcLockedIndex;
                  return (
                    <div
                      key={q.id}
                      className={`p-4 rounded-xl border transition ${
                        isUnlocked
                          ? "bg-white border-slate-200"
                          : "bg-slate-50/80 border-slate-200 opacity-60 select-none"
                      }`}
                    >
                      <div className="flex items-center justify-between mb-2">
                        <div className="flex items-center gap-2">
                          <span className="px-2.5 py-0.5 bg-indigo-600 text-white text-xs font-bold rounded">
                            Câu {index + 1}
                          </span>
                          <span className="text-xs px-2 py-0.5 bg-slate-100 text-slate-600 rounded font-medium">
                            {q.level}
                          </span>
                        </div>
                        {isUnlocked ? (
                          <span className="text-xs text-emerald-600 flex items-center gap-1 font-semibold">
                            <Unlock className="w-3.5 h-3.5" /> Đã mở khóa
                          </span>
                        ) : (
                          <span className="text-xs text-slate-500 flex items-center gap-1 font-medium">
                            <Lock className="w-3.5 h-3.5" /> Hoàn thành câu {index} để mở
                          </span>
                        )}
                      </div>

                      {isUnlocked ? (
                        <>
                          <div className="text-sm font-medium text-slate-800 mb-3">
                            <MathView text={q.question} />
                          </div>
                          <div className="grid grid-cols-1 md:grid-cols-2 gap-2.5">
                            {q.options.map((opt, optIdx) => {
                              const labels = ["A", "B", "C", "D"];
                              const selected = mcAnswers[index] === optIdx;
                              return (
                                <button
                                  key={optIdx}
                                  onClick={() => {
                                    setMcAnswers((prev) => ({ ...prev, [index]: optIdx }));
                                    if (index === mcLockedIndex && mcLockedIndex < 11) {
                                      setMcLockedIndex(index + 1);
                                    }
                                  }}
                                  className={`text-left px-3.5 py-2.5 rounded-lg border text-sm flex items-center gap-2.5 transition ${
                                    selected
                                      ? "bg-indigo-600 text-white border-indigo-600 font-semibold shadow-sm"
                                      : "bg-slate-50 hover:bg-indigo-50/60 border-slate-200 text-slate-700"
                                  }`}
                                >
                                  <span
                                    className={`w-6 h-6 rounded-full flex items-center justify-center text-xs font-bold flex-shrink-0 ${
                                      selected ? "bg-white text-indigo-700" : "bg-white border text-slate-600"
                                    }`}
                                  >
                                    {labels[optIdx]}
                                  </span>
                                  <MathView text={opt} />
                                </button>
                              );
                            })}
                          </div>
                        </>
                      ) : (
                        <p className="text-xs italic text-slate-400">
                          Câu hỏi số {index + 1} đang bị khóa cho đến khi em chọn đáp án câu {index}.
                        </p>
                      )}
                    </div>
                  );
                })}
              </div>
            </section>

            {/* PHẦN II: 2 CÂU ĐÚNG / SAI */}
            <section className="bg-white p-6 rounded-2xl shadow-sm border border-slate-200 space-y-4">
              <div className="border-b pb-3">
                <h3 className="text-sm md:text-base font-bold text-indigo-950 uppercase">
                  Phần II. Câu trắc nghiệm Đúng / Sai (2,0 điểm - 1,0 điểm/câu)
                </h3>
                <p className="text-xs text-slate-500 mt-0.5">
                  Quy tắc chấm chuẩn Bộ GD&ĐT: Đúng 1 ý = 0,1đ • Đúng 2 ý = 0,25đ • Đúng 3 ý = 0,5đ • Đúng cả 4 ý = 1,0đ.
                </p>
              </div>

              <div className="space-y-5">
                {examData.part2.map((q) => (
                  <div key={q.id} className="p-4 rounded-xl border border-slate-200 bg-slate-50/50 space-y-3">
                    <div className="font-bold text-sm text-slate-900">
                      Câu {q.id}: <MathView text={q.stem} />
                    </div>
                    <div className="space-y-2">
                      {q.statements.map((stmt) => {
                        const currentVal = tfAnswers[q.id]?.[stmt.key];
                        return (
                          <div
                            key={stmt.key}
                            className="bg-white p-3 rounded-lg border border-slate-200 flex flex-wrap items-center justify-between gap-3"
                          >
                            <div className="text-sm text-slate-800 flex-1">
                              <span className="font-bold text-indigo-700 mr-1.5">{stmt.key})</span>
                              <MathView text={stmt.text} />
                              <span className="ml-2 text-[11px] px-2 py-0.5 bg-slate-100 text-slate-500 rounded">
                                {stmt.level}
                              </span>
                            </div>
                            <div className="flex items-center gap-2">
                              <button
                                onClick={() =>
                                  setTfAnswers((prev) => ({
                                    ...prev,
                                    [q.id]: { ...prev[q.id], [stmt.key]: true }
                                  }))
                                }
                                className={`px-3 py-1.5 rounded-lg text-xs font-bold border transition ${
                                  currentVal === true
                                    ? "bg-emerald-600 text-white border-emerald-600"
                                    : "bg-white text-slate-600 border-slate-300 hover:bg-slate-100"
                                }`}
                              >
                                Đúng
                              </button>
                              <button
                                onClick={() =>
                                  setTfAnswers((prev) => ({
                                    ...prev,
                                    [q.id]: { ...prev[q.id], [stmt.key]: false }
                                  }))
                                }
                                className={`px-3 py-1.5 rounded-lg text-xs font-bold border transition ${
                                  currentVal === false
                                    ? "bg-rose-600 text-white border-rose-600"
                                    : "bg-white text-slate-600 border-slate-300 hover:bg-slate-100"
                                }`}
                              >
                                Sai
                              </button>
                            </div>
                          </div>
                        );
                      })}
                    </div>
                  </div>
                ))}
              </div>
            </section>

            {/* PHẦN III: 4 CÂU TRẢ LỜI NGẮN */}
            <section className="bg-white p-6 rounded-2xl shadow-sm border border-slate-200 space-y-4">
              <div className="border-b pb-3">
                <h3 className="text-sm md:text-base font-bold text-indigo-950 uppercase">
                  Phần III. Câu trắc nghiệm Trả lời ngắn (2,0 điểm - 0,5 điểm/câu)
                </h3>
                <p className="text-xs text-slate-500 mt-0.5">
                  1 câu Thông hiểu, 2 câu Vận dụng thấp và 1 câu Vận dụng cao. Chấp nhận số nguyên và số thập phân (dấu phẩy hoặc dấu chấm).
                </p>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                {examData.part3.map((q) => (
                  <div key={q.id} className="p-4 rounded-xl border border-slate-200 bg-slate-50/40 flex flex-col justify-between space-y-3">
                    <div>
                      <div className="flex items-center justify-between mb-1.5">
                        <span className="font-bold text-sm text-indigo-900">Câu {q.id}</span>
                        <span className="text-xs px-2 py-0.5 bg-amber-100 text-amber-800 rounded font-medium">
                          {q.level}
                        </span>
                      </div>
                      <div className="text-sm text-slate-800">
                        <MathView text={q.question} />
                      </div>
                    </div>
                    <div>
                      <input
                        type="text"
                        placeholder="Nhập đáp số (VD: 3 hoặc -2.5 hoặc -2,5)..."
                        value={saAnswers[q.id] || ""}
                        onChange={(e) => setSaAnswers((prev) => ({ ...prev, [q.id]: e.target.value }))}
                        className="w-full px-3 py-2 text-sm rounded-lg border border-slate-300 bg-white focus:ring-2 focus:ring-indigo-600 outline-none font-semibold"
                      />
                    </div>
                  </div>
                ))}
              </div>
            </section>

            {/* PHẦN IV: 3 CÂU TỰ LUẬN CHỤP ẢNH BÀI LÀM */}
            <section className="bg-white p-6 rounded-2xl shadow-sm border border-slate-200 space-y-4">
              <div className="border-b pb-3">
                <h3 className="text-sm md:text-base font-bold text-indigo-950 uppercase">
                  Phần IV. Tự luận - Chụp ảnh bài giải viết tay để AI Vision chấm (3,0 điểm - 1,0 điểm/câu)
                </h3>
                <p className="text-xs text-slate-500 mt-0.5">
                  Học sinh trình bày bài giải ra giấy, sau đó mở camera chụp trực tiếp hoặc tải ảnh bài làm lên từng câu.
                </p>
              </div>

              <div className="space-y-4">
                {examData.part4.map((q) => (
                  <div key={q.id} className="p-4 rounded-xl border border-slate-200 space-y-3">
                    <div className="flex items-center justify-between">
                      <span className="font-bold text-sm text-indigo-900">Câu tự luận {q.id} (1,0 điểm)</span>
                      <span className="text-xs px-2.5 py-0.5 bg-purple-100 text-purple-800 rounded font-medium">
                        {q.level}
                      </span>
                    </div>
                    <div className="text-sm font-medium text-slate-800">
                      <MathView text={q.question} />
                    </div>

                    <div className="flex flex-wrap items-center gap-4 pt-2">
                      <label className="cursor-pointer inline-flex items-center gap-2 px-4 py-2 rounded-xl bg-indigo-50 hover:bg-indigo-100 text-indigo-700 font-semibold text-xs border border-indigo-200 transition">
                        <Camera className="w-4 h-4" />
                        <span>Chụp / Tải ảnh bài làm Câu {q.id}</span>
                        <input
                          type="file"
                          accept="image/*"
                          capture="environment"
                          onChange={(e) => handleImageUpload(q.id, e)}
                          className="hidden"
                        />
                      </label>

                      {essayImages[q.id] && (
                        <div className="flex items-center gap-3">
                          <img
                            src={essayImages[q.id]}
                            alt={`Bài làm câu ${q.id}`}
                            className="h-16 w-24 object-cover rounded-lg border border-slate-300 shadow-sm"
                          />
                          <button
                            onClick={() => setEssayImages((prev) => ({ ...prev, [q.id]: null }))}
                            className="text-xs text-rose-600 hover:underline"
                          >
                            Xóa ảnh
                          </button>
                        </div>
                      )}
                    </div>
                  </div>
                ))}
              </div>
            </section>

            {/* NÚT NỘP BÀI */}
            <div className="flex justify-end gap-3 pb-8">
              <button
                onClick={handleSubmitExam}
                disabled={loadingAI}
                className="bg-emerald-600 hover:bg-emerald-700 text-white font-bold px-8 py-3.5 rounded-xl shadow-lg flex items-center gap-2 transition disabled:opacity-50"
              >
                {loadingAI ? (
                  <>
                    <RefreshCw className="w-5 h-5 animate-spin" /> AI đang chấm điểm & viết nhận xét cả 4 phần...
                  </>
                ) : (
                  <>
                    <CheckCircle className="w-5 h-5" /> Nộp bài & Chấm điểm tự động
                  </>
                )}
              </button>
            </div>
          </div>
        )}

        {/* ============================================================== */}
        {/* MÀN HÌNH 3: PHIẾU KẾT QUẢ VÀ XUẤT PDF A4                        */}
        {/* ============================================================== */}
        {view === "result" && resultData && (
          <div className="space-y-6">
            <div className="flex justify-between items-center print:hidden">
              <button
                onClick={() => setView("setup")}
                className="text-sm font-semibold text-indigo-700 hover:underline"
              >
                ← Quay lại làm đề khác
              </button>
              <div className="flex items-center gap-2">
                <button
                  onClick={() => exportResultToPDF("exam-report-card", resultData.studentName, resultData.lesson)}
                  className="bg-indigo-600 hover:bg-indigo-700 text-white font-bold px-5 py-2.5 rounded-xl shadow flex items-center gap-2 text-sm"
                >
                  <Download className="w-4 h-4" /> Xuất file PDF (Chuẩn A4)
                </button>
                <button
                  onClick={() => window.print()}
                  className="bg-slate-700 hover:bg-slate-800 text-white font-bold px-4 py-2.5 rounded-xl text-sm"
                >
                  In trực tiếp
                </button>
              </div>
            </div>

            {/* KHU VỰC IN PHIẾU KẾT QUẢ A4 */}
            <div
              id="exam-report-card"
              className="bg-white p-8 rounded-2xl shadow-sm border border-slate-300 space-y-6 print:border-none print:shadow-none print:p-0"
            >
              <div className="border-b-2 border-slate-800 pb-4 flex justify-between items-start">
                <div>
                  <h2 className="text-xl font-black uppercase text-slate-900">
                    PHIẾU KẾT QUẢ BÀI KIỂM TRA MÔN TOÁN
                  </h2>
                  <p className="text-sm font-semibold text-indigo-800 mt-1">
                    Bộ sách: Kết nối tri thức với cuộc sống - Khối {resultData.grade}
                  </p>
                  <p className="text-xs text-slate-600 mt-0.5">
                    Bài học: <b>{resultData.lesson}</b> | Đề: <b>Bài kiểm tra số {resultData.testNum}</b>
                  </p>
                </div>
                <div className="text-right">
                  <div className="inline-block bg-indigo-900 text-white px-4 py-2 rounded-xl text-center">
                    <div className="text-[10px] uppercase tracking-wider opacity-80">Tổng điểm</div>
                    <div className="text-3xl font-black text-amber-400">{resultData.totalScore} / 10</div>
                  </div>
                </div>
              </div>

              {/* Thông tin học sinh */}
              <div className="grid grid-cols-2 md:grid-cols-4 gap-3 bg-slate-50 p-4 rounded-xl border border-slate-200 text-sm">
                <div>
                  <span className="text-slate-500 text-xs block">Họ và tên học sinh:</span>
                  <strong className="text-slate-900">{resultData.studentName}</strong>
                </div>
                <div>
                  <span className="text-slate-500 text-xs block">Lớp đăng ký:</span>
                  <strong className="text-indigo-700">{resultData.className}</strong>
                </div>
                <div>
                  <span className="text-slate-500 text-xs block">Thời gian nộp bài:</span>
                  <strong className="text-slate-800">{resultData.timestamp}</strong>
                </div>
                <div>
                  <span className="text-slate-500 text-xs block">Xếp loại năng lực:</span>
                  <strong className="text-emerald-700">
                    {resultData.totalScore >= 8 ? "Giỏi" : resultData.totalScore >= 6.5 ? "Khá" : resultData.totalScore >= 5 ? "Đạt" : "Chưa đạt"}
                  </strong>
                </div>
              </div>

              {/* Bảng điểm 4 phần */}
              <div className="grid grid-cols-2 md:grid-cols-4 gap-3 text-center">
                <div className="p-3 rounded-xl border bg-white">
                  <div className="text-xs text-slate-500">Phần I (12 câu TN)</div>
                  <div className="text-lg font-bold text-slate-900">{resultData.scorePart1} / 3,0đ</div>
                </div>
                <div className="p-3 rounded-xl border bg-white">
                  <div className="text-xs text-slate-500">Phần II (2 câu Đúng/Sai)</div>
                  <div className="text-lg font-bold text-slate-900">{resultData.scorePart2} / 2,0đ</div>
                </div>
                <div className="p-3 rounded-xl border bg-white">
                  <div className="text-xs text-slate-500">Phần III (4 câu TL ngắn)</div>
                  <div className="text-lg font-bold text-slate-900">{resultData.scorePart3} / 2,0đ</div>
                </div>
                <div className="p-3 rounded-xl border bg-white">
                  <div className="text-xs text-slate-500">Phần IV (3 câu Tự luận)</div>
                  <div className="text-lg font-bold text-slate-900">{resultData.scorePart4} / 3,0đ</div>
                </div>
              </div>

              {/* KHU VỰC NHẬN XÉT CHI TIẾT CẢ 4 PHẦN VÀ ĐÁNH GIÁ CHUNG */}
              <div className="space-y-3">
                <div className="flex items-center gap-2 border-b-2 border-indigo-900 pb-1.5">
                  <Award className="w-5 h-5 text-indigo-900" />
                  <h3 className="font-black text-sm md:text-base uppercase text-indigo-950 tracking-tight">
                    Phiếu nhận xét đánh giá chi tiết cả 4 phần kiểm tra:
                  </h3>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-3.5">
                  {/* Nhận xét Phần I */}
                  <div className="bg-blue-50/70 border border-blue-200 rounded-xl p-3.5 space-y-1">
                    <div className="flex items-center justify-between">
                      <span className="text-xs font-bold uppercase text-blue-900 flex items-center gap-1.5">
                        <span className="w-2 h-2 rounded-full bg-blue-600"></span>
                        Phần I. Trắc nghiệm 4 lựa chọn
                      </span>
                      <span className="text-xs font-black text-blue-700 bg-white px-2 py-0.5 rounded border border-blue-200">
                        {resultData.scorePart1} / 3,0đ
                      </span>
                    </div>
                    <p className="text-xs text-slate-700 leading-relaxed font-medium">
                      {resultData.feedbacks?.part1}
                    </p>
                  </div>

                  {/* Nhận xét Phần II */}
                  <div className="bg-emerald-50/70 border border-emerald-200 rounded-xl p-3.5 space-y-1">
                    <div className="flex items-center justify-between">
                      <span className="text-xs font-bold uppercase text-emerald-900 flex items-center gap-1.5">
                        <span className="w-2 h-2 rounded-full bg-emerald-600"></span>
                        Phần II. Trắc nghiệm Đúng / Sai
                      </span>
                      <span className="text-xs font-black text-emerald-700 bg-white px-2 py-0.5 rounded border border-emerald-200">
                        {resultData.scorePart2} / 2,0đ
                      </span>
                    </div>
                    <p className="text-xs text-slate-700 leading-relaxed font-medium">
                      {resultData.feedbacks?.part2}
                    </p>
                  </div>

                  {/* Nhận xét Phần III */}
                  <div className="bg-amber-50/70 border border-amber-200 rounded-xl p-3.5 space-y-1">
                    <div className="flex items-center justify-between">
                      <span className="text-xs font-bold uppercase text-amber-900 flex items-center gap-1.5">
                        <span className="w-2 h-2 rounded-full bg-amber-600"></span>
                        Phần III. Trắc nghiệm Trả lời ngắn
                      </span>
                      <span className="text-xs font-black text-amber-700 bg-white px-2 py-0.5 rounded border border-amber-200">
                        {resultData.scorePart3} / 2,0đ
                      </span>
                    </div>
                    <p className="text-xs text-slate-700 leading-relaxed font-medium">
                      {resultData.feedbacks?.part3}
                    </p>
                  </div>

                  {/* Nhận xét Phần IV */}
                  <div className="bg-purple-50/70 border border-purple-200 rounded-xl p-3.5 space-y-1">
                    <div className="flex items-center justify-between">
                      <span className="text-xs font-bold uppercase text-purple-900 flex items-center gap-1.5">
                        <span className="w-2 h-2 rounded-full bg-purple-600"></span>
                        Phần IV. Tự luận viết tay (AI Vision)
                      </span>
                      <span className="text-xs font-black text-purple-700 bg-white px-2 py-0.5 rounded border border-purple-200">
                        {resultData.scorePart4} / 3,0đ
                      </span>
                    </div>
                    <p className="text-xs text-slate-700 leading-relaxed font-medium">
                      {resultData.feedbacks?.part4}
                    </p>
                  </div>
                </div>

                {/* Đánh giá & Định hướng tổng quát */}
                <div className="bg-indigo-50 border-2 border-indigo-200 rounded-xl p-4 space-y-1.5">
                  <div className="text-xs font-bold uppercase text-indigo-900 flex items-center gap-1.5">
                    <Sparkles className="w-4 h-4 text-amber-500" />
                    Đánh giá tổng quát năng lực & Định hướng học tập:
                  </div>
                  <p className="text-sm text-slate-800 leading-relaxed font-medium">
                    {resultData.feedbacks?.overall || resultData.overallTeacherComment}
                  </p>
                </div>
              </div>

              {/* Chi tiết tự luận chấm AI Vision */}
              <div className="space-y-3 pt-2">
                <h4 className="font-bold text-sm uppercase text-slate-800 border-b pb-1">
                  Chi tiết nhận diện chữ viết tay & chấm bài Tự luận (Phần IV):
                </h4>
                {examData.part4.map((q) => {
                  const fb = resultData.essayFeedbacks[q.id];
                  return (
                    <div key={q.id} className="p-3.5 rounded-xl border border-slate-200 bg-slate-50/50 text-xs space-y-1.5">
                      <div className="flex justify-between font-bold text-slate-900">
                        <span>Câu {q.id} ({q.level}): <MathView text={q.question} /></span>
                        <span className="text-indigo-700">{fb?.score || 0} / 1,0 điểm</span>
                      </div>
                      {fb?.ocrText && (
                        <div className="text-slate-600 italic">
                          <b>Lời giải AI nhận diện từ ảnh:</b> {fb.ocrText}
                        </div>
                      )}
                      <div className="text-emerald-800">
                        <b>Lời phê & Phân tích lỗi sai:</b> {fb?.comment}
                      </div>
                      <div className="text-slate-500">
                        <b>Hướng dẫn chấm chuẩn (Rubric):</b> {q.rubric}
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>
          </div>
        )}

        {/* ============================================================== */}
        {/* MÀN HÌNH 4: THỐNG KÊ LỚP HỌC & XUẤT EXCEL / CSV                  */}
        {/* ============================================================== */}
        {view === "dashboard" && (
          <div className="bg-white rounded-2xl shadow-sm border border-slate-200 p-6 space-y-6">
            <div className="flex flex-wrap justify-between items-center gap-4 border-b pb-4">
              <div>
                <h2 className="text-xl font-bold text-slate-900">
                  Bảng Thống kê Kết quả Học tập theo Lớp
                </h2>
                <p className="text-xs md:text-sm text-slate-500 mt-0.5">
                  Bộ lọc lớp, điểm trung bình, phân loại năng lực và xuất file Excel / CSV đầy đủ nhận xét 4 phần
                </p>
              </div>

              <div className="flex flex-wrap items-center gap-2 print:hidden">
                <button
                  onClick={() => exportSubmissionsToExcel(submissions, filterClass)}
                  className="bg-emerald-600 hover:bg-emerald-700 text-white px-3.5 py-2 rounded-xl text-xs font-bold flex items-center gap-1.5 shadow"
                >
                  <FileSpreadsheet className="w-4 h-4" /> Xuất Excel (.xlsx)
                </button>
                <button
                  onClick={() => exportSubmissionsToCSV(submissions, filterClass)}
                  className="bg-teal-600 hover:bg-teal-700 text-white px-3.5 py-2 rounded-xl text-xs font-bold flex items-center gap-1.5 shadow"
                >
                  <Download className="w-4 h-4" /> Xuất CSV
                </button>
                {submissions.length > 0 && (
                  <button
                    onClick={() => {
                      if (window.confirm("Thầy/Cô có chắc chắn muốn xóa toàn bộ lịch sử điểm số đã lưu?")) {
                        setSubmissions([]);
                        localStorage.removeItem("MATH_SUBMISSIONS_KNTT");
                      }
                    }}
                    className="bg-rose-50 text-rose-600 hover:bg-rose-100 px-3 py-2 rounded-xl text-xs font-bold border border-rose-200 transition flex items-center gap-1"
                  >
                    <Trash2 className="w-3.5 h-3.5" /> Xóa lịch sử
                  </button>
                )}
              </div>
            </div>

            {/* Thống kê nhanh */}
            {classStats && (
              <div className="grid grid-cols-2 md:grid-cols-5 gap-3">
                <div className="bg-indigo-50 border border-indigo-200 p-3.5 rounded-xl text-center">
                  <div className="text-xs text-indigo-700 font-bold uppercase">Điểm TB Lớp</div>
                  <div className="text-2xl font-black text-indigo-950 mt-1">{classStats.avg}</div>
                </div>
                <div className="bg-emerald-50 border border-emerald-200 p-3.5 rounded-xl text-center">
                  <div className="text-xs text-emerald-700 font-bold uppercase">Giỏi (≥ 8.0)</div>
                  <div className="text-2xl font-black text-emerald-800 mt-1">{classStats.gioi} <span className="text-xs font-normal">({Math.round((classStats.gioi / classStats.count) * 100)}%)</span></div>
                </div>
                <div className="bg-blue-50 border border-blue-200 p-3.5 rounded-xl text-center">
                  <div className="text-xs text-blue-700 font-bold uppercase">Khá (6.5 - 7.9)</div>
                  <div className="text-2xl font-black text-blue-800 mt-1">{classStats.kha} <span className="text-xs font-normal">({Math.round((classStats.kha / classStats.count) * 100)}%)</span></div>
                </div>
                <div className="bg-amber-50 border border-amber-200 p-3.5 rounded-xl text-center">
                  <div className="text-xs text-amber-700 font-bold uppercase">Đạt (5.0 - 6.4)</div>
                  <div className="text-2xl font-black text-amber-800 mt-1">{classStats.dat} <span className="text-xs font-normal">({Math.round((classStats.dat / classStats.count) * 100)}%)</span></div>
                </div>
                <div className="bg-rose-50 border border-rose-200 p-3.5 rounded-xl text-center">
                  <div className="text-xs text-rose-700 font-bold uppercase">Chưa đạt (&lt; 5.0)</div>
                  <div className="text-2xl font-black text-rose-800 mt-1">{classStats.chuaDat} <span className="text-xs font-normal">({Math.round((classStats.chuaDat / classStats.count) * 100)}%)</span></div>
                </div>
              </div>
            )}

            {/* Bộ lọc theo lớp */}
            <div className="flex flex-wrap items-center gap-3 bg-slate-50 p-3.5 rounded-xl border border-slate-200 text-xs">
              <span className="font-bold text-slate-700">Lọc theo Lớp học:</span>
              <button
                onClick={() => setFilterClass("ALL")}
                className={`px-3 py-1.5 rounded-lg font-semibold transition ${
                  filterClass === "ALL"
                    ? "bg-indigo-600 text-white"
                    : "bg-white text-slate-700 border border-slate-300 hover:bg-slate-100"
                }`}
              >
                Tất cả ({submissions.length})
              </button>
              {uniqueClasses.map((cls) => {
                const count = submissions.filter((s) => s.className === cls).length;
                return (
                  <button
                    key={cls}
                    onClick={() => setFilterClass(cls)}
                    className={`px-3 py-1.5 rounded-lg font-semibold transition ${
                      filterClass === cls
                        ? "bg-indigo-600 text-white"
                        : "bg-white text-slate-700 border border-slate-300 hover:bg-slate-100"
                    }`}
                  >
                    Lớp {cls} ({count})
                  </button>
                );
              })}
            </div>

            {filteredSubs.length === 0 ? (
              <div className="text-center py-12 text-slate-400 text-sm">
                Chưa có dữ liệu bài làm nào được ghi nhận cho bộ lọc này.
              </div>
            ) : (
              <div className="overflow-x-auto">
                <table className="w-full text-left border-collapse text-xs md:text-sm">
                  <thead>
                    <tr className="bg-slate-100 text-slate-700 text-[11px] uppercase font-bold">
                      <th className="p-3 border">Lớp</th>
                      <th className="p-3 border">Họ tên Học sinh</th>
                      <th className="p-3 border text-center">Khối</th>
                      <th className="p-3 border">Bài học & Đề</th>
                      <th className="p-3 border text-center">P.I (3đ)</th>
                      <th className="p-3 border text-center">P.II (2đ)</th>
                      <th className="p-3 border text-center">P.III (2đ)</th>
                      <th className="p-3 border text-center">P.IV (3đ)</th>
                      <th className="p-3 border text-center">Tổng</th>
                      <th className="p-3 border text-center">Xếp loại</th>
                      <th className="p-3 border">Đánh giá chung</th>
                    </tr>
                  </thead>
                  <tbody>
                    {filteredSubs.map((sub) => (
                      <tr key={sub.id} className="hover:bg-slate-50 transition">
                        <td className="p-3 border font-bold text-indigo-700">{sub.className}</td>
                        <td className="p-3 border font-medium text-slate-900">{sub.studentName}</td>
                        <td className="p-3 border text-center">Toán {sub.grade}</td>
                        <td className="p-3 border text-xs">
                          <div className="font-medium text-slate-800">{sub.lesson}</div>
                          <span className="text-indigo-600 font-semibold">Bài KT số {sub.testNum}</span>
                        </td>
                        <td className="p-3 border text-center">{sub.scorePart1}</td>
                        <td className="p-3 border text-center">{sub.scorePart2}</td>
                        <td className="p-3 border text-center">{sub.scorePart3}</td>
                        <td className="p-3 border text-center">{sub.scorePart4}</td>
                        <td className="p-3 border text-center font-bold text-emerald-700 text-sm">{sub.totalScore}</td>
                        <td className="p-3 border text-center">
                          <span
                            className={`px-2 py-0.5 rounded font-bold text-[11px] ${
                              sub.totalScore >= 8
                                ? "bg-emerald-100 text-emerald-800"
                                : sub.totalScore >= 6.5
                                ? "bg-blue-100 text-blue-800"
                                : sub.totalScore >= 5
                                ? "bg-amber-100 text-amber-800"
                                : "bg-rose-100 text-rose-800"
                            }`}
                          >
                            {sub.totalScore >= 8 ? "Giỏi" : sub.totalScore >= 6.5 ? "Khá" : sub.totalScore >= 5 ? "Đạt" : "Chưa đạt"}
                          </span>
                        </td>
                        <td className="p-3 border text-xs text-slate-600 max-w-xs">{sub.feedbacks?.overall || sub.overallTeacherComment}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )}
          </div>
        )}
      </main>
    </div>
  );
}
