# -*- coding: utf-8 -*-
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')
PROJECT_DIR = r"C:\Users\May Tinh Chau A\.gemini\antigravity\scratch\toan-thcs-kntt"
index_path = os.path.join(PROJECT_DIR, "index.html")

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. BỎ HOÀN TOÀN KHÓA ĐỀ TRONG handleStartPeriodicExam
old_unlock_block = """        // Kiểm tra xem đề thi có đang bị khóa hay không
        if (exam && exam.grade && exam.term) {
          const currentKey = `${exam.grade}_${exam.term}`;
          const currentUnlocked = periodicUnlocked[currentKey] || 1;
          const testNum = Number(exam.testNum) || 1;
          if (testNum > currentUnlocked) {
            showToast("warning", `Vui lòng hoàn thành và nộp bài Đề số ${testNum - 1} trước để mở khóa Đề số ${testNum}!`);
            return;
          }
        }"""

# Chuẩn hóa xuống dòng nếu cần
content = content.replace(old_unlock_block, "        // Toàn bộ đề thi định kỳ đã được mở tự do cho học sinh làm bài")
content = content.replace(old_unlock_block.replace("\r\n", "\n"), "        // Toàn bộ đề thi định kỳ đã được mở tự do cho học sinh làm bài")

# 2. BỎ KHÓA ĐỀ TRONG DANH SÁCH ĐỀ ĐỊNH KỲ (UI)
old_ui_block = """                          {termExams.map((ex, idx) => {
                            const unlockKey = `${periodicGrade}_${periodicTerm}`;
                            const unlockedUpTo = periodicUnlocked[unlockKey] || 1;
                            const isUnlocked = (idx + 1) <= unlockedUpTo;

                            return (
                              <button
                                key={ex.id || idx}
                                onClick={() => {
                                  if (!isUnlocked) {
                                    showToast("warning", `Vui lòng hoàn thành và nộp bài Đề số ${idx} trước để mở khóa Đề số ${idx + 1}!`);
                                    return;
                                  }
                                  setSelectedPeriodicTestIdx(idx);
                                }}
                                className={`p-4 rounded-xl border text-left transition relative ${
                                  !isUnlocked
                                    ? "opacity-60 bg-slate-100/80 border-slate-200 cursor-not-allowed select-none"
                                    : selectedPeriodicTestIdx === idx
                                    ? "bg-emerald-50 border-emerald-600 ring-2 ring-emerald-200 text-slate-900 shadow-sm"
                                    : "bg-slate-50 border-slate-200 hover:bg-slate-100 text-slate-800"
                                }`}
                              >
                                <div className="flex items-center justify-between">
                                  <span className="font-bold text-sm text-indigo-950">
                                    Đề số {ex.testNum || (idx + 1)}
                                  </span>
                                  {isUnlocked ? (
                                    <span className={`text-[10px] font-bold px-2 py-0.5 rounded ${
                                      idx === 0 ? "bg-blue-100 text-blue-800" :
                                      idx === 1 ? "bg-emerald-100 text-emerald-800" :
                                      idx === 2 ? "bg-amber-100 text-amber-800" :
                                      idx === 3 ? "bg-purple-100 text-purple-800" :
                                      idx === 4 ? "bg-teal-100 text-teal-800" :
                                      idx === 5 ? "bg-rose-100 text-rose-800" :
                                      idx === 6 ? "bg-indigo-100 text-indigo-800" :
                                      "bg-violet-100 text-violet-800"
                                    }`}>
                                      {idx === 0 ? "Đề 01 (Cơ bản)" : idx === 1 ? "Đề 02 (Khá)" : idx === 2 ? "Đề 03 (Nâng cao)" : `Đề ${(idx + 1 < 10 ? '0' + (idx+1) : idx+1)}`}
                                    </span>
                                  ) : (
                                    <span className="text-[10px] font-bold px-2 py-0.5 rounded bg-slate-200 text-slate-600 flex items-center gap-1">
                                      <span>🔒</span> Chưa mở
                                    </span>
                                  )}
                                </div>"""

new_ui_block = """                          {termExams.map((ex, idx) => {
                            return (
                              <button
                                key={ex.id || idx}
                                onClick={() => {
                                  setSelectedPeriodicTestIdx(idx);
                                }}
                                className={`p-4 rounded-xl border text-left transition relative ${
                                  selectedPeriodicTestIdx === idx
                                    ? "bg-emerald-50 border-emerald-600 ring-2 ring-emerald-200 text-slate-900 shadow-sm"
                                    : "bg-slate-50 border-slate-200 hover:bg-slate-100 text-slate-800"
                                }`}
                              >
                                <div className="flex items-center justify-between">
                                  <span className="font-bold text-sm text-indigo-950">
                                    Đề số {ex.testNum || (idx + 1)}
                                  </span>
                                  <span className={`text-[10px] font-bold px-2 py-0.5 rounded ${
                                    idx === 0 ? "bg-blue-100 text-blue-800" :
                                    idx === 1 ? "bg-emerald-100 text-emerald-800" :
                                    idx === 2 ? "bg-amber-100 text-amber-800" :
                                    idx === 3 ? "bg-purple-100 text-purple-800" :
                                    idx === 4 ? "bg-teal-100 text-teal-800" :
                                    idx === 5 ? "bg-rose-100 text-rose-800" :
                                    idx === 6 ? "bg-indigo-100 text-indigo-800" :
                                    "bg-violet-100 text-violet-800"
                                  }`}>
                                    {idx === 0 ? "Đề 01 (Cơ bản)" : idx === 1 ? "Đề 02 (Khá)" : idx === 2 ? "Đề 03 (Nâng cao)" : `Đề ${(idx + 1 < 10 ? '0' + (idx+1) : idx+1)}`}
                                  </span>
                                </div>"""

content = content.replace(old_ui_block, new_ui_block)
content = content.replace(old_ui_block.replace("\r\n", "\n"), new_ui_block.replace("\r\n", "\n"))

# 3. GỠ BỎ RESTORE TITLE TRONG AFTERPRINT KHIẾN HỘP THOẠI IN BỊ RESET TÊN FILE
content = content.replace('window.addEventListener("afterprint", restoreTitle, { once: true });', '// document.title giữ nguyên tên đề thi để Save As PDF chuẩn xác 100%')
content = content.replace('window.addEventListener("afterprint", restore, { once: true });', '// document.title giữ nguyên tên đề thi để Save As PDF chuẩn xác 100%')

# 4. CẬP NHẬT CSS @MEDIA PRINT
old_print_hide = """      #periodic-filter-card,
      [data-no-print="true"],
      .toast-container {
        display: none !important;
        visibility: hidden !important;
        height: 0 !important;
        max-height: 0 !important;
        margin: 0 !important;
        padding: 0 !important;
        overflow: hidden !important;
      }"""

new_print_hide = """      #periodic-filter-card,
      [data-no-print="true"],
      .toast-container {
        display: none !important;
        visibility: hidden !important;
        height: 0 !important;
        max-height: 0 !important;
        margin: 0 !important;
        padding: 0 !important;
        overflow: hidden !important;
      }
      #setup-controls-card *,
      .setup-controls-card * {
        display: none !important;
        visibility: hidden !important;
      }"""

content = content.replace(old_print_hide, new_print_hide)
content = content.replace(old_print_hide.replace("\r\n", "\n"), new_print_hide.replace("\r\n", "\n"))

# 5. CẬP NHẬT SELECTOR ĐỀ SGK (7 ĐỀ KHI LÀ BÀI CUỐI CHƯƠNG)
old_selector_start = "4. Chọn Đề kiểm tra bài học SGK (3 mã đề chuẩn hóa theo độ dốc)"

# Tìm khối selector 3 đề
idx_sel = content.find(old_selector_start)
if idx_sel != -1:
    # Tìm thẻ <div> chứa label này
    div_start = content.rfind("<div>", 0, idx_sel)
    # Tìm khối kết thúc thẻ div của selector (trước comment {/* Tóm tắt ma trận 10 điểm */})
    end_marker = "{/* Tóm tắt ma trận 10 điểm */}"
    idx_end = content.find(end_marker, idx_sel)
    if div_start != -1 and idx_end != -1:
        target_div = content[div_start:idx_end].strip()
        # Đảm bảo target_div kết thúc đúng thẻ </div>
        print("Found target selector block! Length:", len(target_div))
        
        new_selector_code = """{(() => {
                      const isChapterExam = selectedLesson && selectedLesson.toLowerCase().includes("cuối chương");
                      const lessonTests = isChapterExam ? [
                        {
                          num: 1,
                          title: "Đề số 1",
                          level: "Cơ bản - Khá",
                          ratio: "40% NB • 30% TH • 20% VD • 10% VDC",
                          scoreRange: "7 - 8 điểm",
                          desc: "Bao quát kiến thức toàn chương",
                          icon: "🌱",
                          activeStyle: "border-emerald-600 bg-emerald-50/90 ring-2 ring-emerald-500/30 text-emerald-950",
                          badgeColor: "bg-emerald-100 text-emerald-800 border border-emerald-300"
                        },
                        {
                          num: 2,
                          title: "Đề số 2",
                          level: "Tương đương Đề 1",
                          ratio: "40% NB • 30% TH • 20% VD • 10% VDC",
                          scoreRange: "7 - 8 điểm",
                          desc: "Rèn luyện mô hình đề độc lập",
                          icon: "📘",
                          activeStyle: "border-blue-600 bg-blue-50/90 ring-2 ring-blue-500/30 text-blue-950",
                          badgeColor: "bg-blue-100 text-blue-800 border border-blue-300"
                        },
                        {
                          num: 3,
                          title: "Đề số 3",
                          level: "Khá Giỏi",
                          ratio: "20% NB • 30% TH • 30% VD • 20% VDC",
                          scoreRange: "8.5 - 9.5 điểm",
                          desc: "Phân hóa câu cuối, bám sát SGK",
                          icon: "🚀",
                          activeStyle: "border-purple-600 bg-purple-50/90 ring-2 ring-purple-500/30 text-purple-950",
                          badgeColor: "bg-purple-100 text-purple-800 border border-purple-300"
                        },
                        {
                          num: 4,
                          title: "Đề số 4",
                          level: "Chuẩn ma trận",
                          ratio: "30% NB • 30% TH • 20% VD • 20% VDC",
                          scoreRange: "8.0 - 9.0 điểm",
                          desc: "Toàn diện các dạng bài trong chương",
                          icon: "🎯",
                          activeStyle: "border-indigo-600 bg-indigo-50/90 ring-2 ring-indigo-500/30 text-indigo-950",
                          badgeColor: "bg-indigo-100 text-indigo-800 border border-indigo-300"
                        },
                        {
                          num: 5,
                          title: "Đề số 5",
                          level: "Vận dụng thực tế",
                          ratio: "30% NB • 30% TH • 20% VD • 20% VDC",
                          scoreRange: "8.0 - 9.0 điểm",
                          desc: "Liên hệ ứng dụng thực tiễn",
                          icon: "💡",
                          activeStyle: "border-amber-600 bg-amber-50/90 ring-2 ring-amber-500/30 text-amber-950",
                          badgeColor: "bg-amber-100 text-amber-800 border border-amber-300"
                        },
                        {
                          num: 6,
                          title: "Đề số 6",
                          level: "Phân hóa Nâng cao",
                          ratio: "30% NB • 30% TH • 20% VD • 20% VDC",
                          scoreRange: "8.5 - 9.5 điểm",
                          desc: "Thử thách tư duy logic & biến đổi",
                          icon: "🔥",
                          activeStyle: "border-rose-600 bg-rose-50/90 ring-2 ring-rose-500/30 text-rose-950",
                          badgeColor: "bg-rose-100 text-rose-800 border border-rose-300"
                        },
                        {
                          num: 7,
                          title: "Đề số 7",
                          level: "Chinh phục điểm 10",
                          ratio: "30% NB • 30% TH • 20% VD • 20% VDC",
                          scoreRange: "9.0 - 10.0 điểm",
                          desc: "Câu hỏi chốt điểm 10 phân hóa cao",
                          icon: "🏆",
                          activeStyle: "border-teal-600 bg-teal-50/90 ring-2 ring-teal-500/30 text-teal-950",
                          badgeColor: "bg-teal-100 text-teal-800 border border-teal-300"
                        }
                      ] : [
                        {
                          num: 1,
                          title: "Đề số 1",
                          level: "Chuẩn cơ bản SGK",
                          ratio: "70% CB • 20% VD • 10% TT",
                          scoreRange: "7 - 8 điểm (Khá - TB)",
                          desc: "Bám sát ví dụ & bài tập SGK",
                          icon: "🌱",
                          activeStyle: "border-emerald-600 bg-emerald-50/90 ring-2 ring-emerald-500/30 text-emerald-950",
                          badgeColor: "bg-emerald-100 text-emerald-800 border border-emerald-300"
                        },
                        {
                          num: 2,
                          title: "Đề số 2",
                          level: "Tương đương Đề 1",
                          ratio: "70% CB • 20% VD • 10% TT",
                          scoreRange: "7 - 8 điểm (Khá - TB)",
                          desc: "Rèn luyện mô hình song song",
                          icon: "📘",
                          activeStyle: "border-blue-600 bg-blue-50/90 ring-2 ring-blue-500/30 text-blue-950",
                          badgeColor: "bg-blue-100 text-blue-800 border border-blue-300"
                        },
                        {
                          num: 3,
                          title: "Đề số 3",
                          level: "Phân hóa nhẹ",
                          ratio: "60% CB • 30% VD • 10% VDC",
                          scoreRange: "8.5 - 9.5 điểm",
                          desc: "Phân hóa câu cuối, bám sát SGK",
                          icon: "🚀",
                          activeStyle: "border-purple-600 bg-purple-50/90 ring-2 ring-purple-500/30 text-purple-950",
                          badgeColor: "bg-purple-100 text-purple-800 border border-purple-300"
                        }
                      ];

                      return (
                        <div>
                          <label className="block text-xs font-bold uppercase text-slate-700 mb-2 flex items-center justify-between">
                            <span>{isChapterExam ? "4. Chọn Đề kiểm tra cuối Chương (7 mã đề chuẩn ma trận độc lập 100%)" : "4. Chọn Đề kiểm tra bài học SGK (3 mã đề chuẩn hóa theo độ dốc)"}</span>
                            <span className="text-[11px] font-normal text-indigo-600 lowercase bg-indigo-50 px-2 py-0.5 rounded border border-indigo-200">
                              {isChapterExam ? "Đề 1 - Đề 7 mở tự do • Chuẩn 30% NB, 30% TH, 20% VD, 20% VDC" : "Đề 1 & 2 tương đương • Đề 3 phân hóa nhẹ"}
                            </span>
                          </label>
                          <div className={`grid ${isChapterExam ? "grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-7" : "grid-cols-1 sm:grid-cols-3"} gap-2.5`}>
                            {lessonTests.map((item) => (
                              <button
                                key={item.num}
                                type="button"
                                onClick={() => setSelectedTestNum(item.num)}
                                className={`p-3 rounded-xl border-2 text-left sm:text-center transition flex flex-col justify-between gap-1.5 relative shadow-xs ${
                                  selectedTestNum === item.num
                                    ? `${item.activeStyle} shadow-md`
                                    : "border-slate-200 bg-white hover:border-slate-300 hover:bg-slate-50 text-slate-800"
                                }`}
                              >
                                <div className="flex items-center sm:justify-center gap-1.5 w-full">
                                  <span className="text-lg">{item.icon}</span>
                                  <span className="text-sm font-black text-slate-900">{item.title}</span>
                                  {selectedTestNum === item.num && (
                                    <span className="ml-auto sm:hidden text-[10px] font-black text-emerald-700 bg-emerald-100 px-1.5 py-0.5 rounded">
                                      ✓ Đang chọn
                                    </span>
                                  )}
                                </div>
                                <span className={`text-[11px] font-bold px-2 py-0.5 rounded-full inline-block sm:mx-auto ${item.badgeColor}`}>
                                  {item.level}
                                </span>
                                <div className="text-[11px] text-slate-600 font-medium">
                                  Tỉ lệ: <b>{item.ratio}</b>
                                </div>
                                <div className="text-[11px] font-bold text-indigo-700 bg-indigo-50/80 px-2 py-0.5 rounded border border-indigo-100">
                                  Mục tiêu: {item.scoreRange}
                                </div>
                                <p className="text-[10px] text-slate-500 italic mt-0.5">
                                  {item.desc}
                                </p>
                                {selectedTestNum === item.num && (
                                  <div className="hidden sm:flex text-[11px] font-black text-emerald-700 items-center justify-center gap-0.5 mt-0.5">
                                    <span>✓ Đang chọn</span>
                                  </div>
                                )}
                              </button>
                            ))}
                          </div>
                        </div>
                      );
                    })()}"""

        content = content[:div_start] + new_selector_code + "\n\n                    " + content[idx_end:]

# 6. RESET selectedTestNum KHI ĐỔI BÀI HỌC
eff_search = "const [selectedTestNum, setSelectedTestNum] = useState(1);"
eff_replace = """const [selectedTestNum, setSelectedTestNum] = useState(1);

      // Tự động điều chỉnh mã đề khi đổi bài học
      useEffect(() => {
        const isEnd = selectedLesson && selectedLesson.toLowerCase().includes("cuối chương");
        if (!isEnd && selectedTestNum > 3) {
          setSelectedTestNum(1);
        }
      }, [selectedLesson]);"""

content = content.replace(eff_search, eff_replace)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ ĐÃ PATCH index.html THÀNH CÔNG VỚI TẤT CẢ CẢI TIẾN!")
