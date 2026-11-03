# -*- coding: utf-8 -*-
"""
Script chèn toàn bộ giao diện MÀN HÌNH MÔN: KHTN vào index.html
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Đọc khối code giao diện KHTN từ template
khtn_view_jsx = """
            {/* ============================================================== */}
            {/* MÀN HÌNH CHUYÊN BIỆT: MÔN KHOA HỌC TỰ NHIÊN (KHTN 7, 8, 9)       */}
            {/* ============================================================== */}
            {view === "khtn" && (() => {
              const curriculum = (typeof window !== "undefined" && window.KHTN_CURRICULUM) || {};
              const currentSubj = curriculum[khtnSubject] || {};
              const currentGradeData = currentSubj.grades?.[khtnGrade] || {};
              const currentChapters = currentGradeData.chapters || [];
              const currentChapter = currentChapters.find(c => c.id === khtnChapterId) || currentChapters[0] || null;
              const currentLessons = currentChapter?.lessons || [];
              const currentLesson = currentLessons.find(l => l.id === khtnLessonId) || currentLessons[0] || null;
              
              const currentExam = getKhtnExam();
              const maxTests = currentLesson?.isReview ? 5 : 3;

              return (
                <div className="space-y-6">
                  {/* BANNER MÔN KHTN */}
                  <div id="khtn-banner-card" className="bg-gradient-to-r from-teal-900 via-emerald-950 to-slate-900 text-white p-6 md:p-8 rounded-2xl shadow-md space-y-3 no-print print:hidden">
                    <div className="flex flex-wrap items-center justify-between gap-4">
                      <div className="flex items-center gap-3.5">
                        <div className="w-12 h-12 bg-white/10 backdrop-blur rounded-2xl flex items-center justify-center text-2xl shrink-0">
                          {khtnSubject === "chemistry" ? "🧪" : "⚡"}
                        </div>
                        <div>
                          <div className="flex items-center gap-2">
                            <span className="bg-teal-400 text-slate-950 text-[10px] font-black px-2 py-0.5 rounded uppercase tracking-wider">
                              ĐỀ THI KHTN CHUẨN MA TRẬN 2025
                            </span>
                            <span className="text-xs text-teal-300">Khối 7, 8, 9 • Thời gian: 45 phút • 10.0 điểm</span>
                          </div>
                          <h2 className="text-xl md:text-2xl font-black text-amber-300 mt-1 uppercase tracking-wide">
                            HỆ THỐNG ĐỀ ÔN TẬP KHOA HỌC TỰ NHIÊN ({khtnSubject === "chemistry" ? "MÔN HÓA HỌC" : "MÔN VẬT LÝ"})
                          </h2>
                          <p className="text-xs md:text-sm text-slate-300 mt-0.5">
                            Bộ sách Kết nối tri thức với cuộc sống • Chuẩn cấu trúc 4 phần (12 TN + 4 Đúng/Sai + 6 TLN + 4 VDC) • 30% Nhận biết, 30% Thông hiểu, 20% Vận dụng, 20% Vận dụng cao
                          </p>
                        </div>
                      </div>

                      {currentExam && (
                        <div className="flex flex-wrap items-center gap-2">
                          <button
                            onClick={() => handlePrintKhtnExam(false)}
                            className="bg-indigo-600 hover:bg-indigo-500 text-white font-bold px-4 py-2.5 rounded-xl shadow text-xs md:text-sm flex items-center gap-1.5 transition"
                            title="In hoặc Lưu PDF đề thi tối ưu tiết kiệm giấy (không kèm đáp án)"
                          >
                            <span>🖨️</span> In Đề thi (Tiết kiệm giấy)
                          </button>
                          <button
                            onClick={() => handlePrintKhtnExam(true)}
                            className="bg-emerald-600 hover:bg-emerald-500 text-white font-bold px-3.5 py-2.5 rounded-xl shadow text-xs md:text-sm flex items-center gap-1.5 transition"
                            title="In hoặc Lưu PDF đề thi kèm đáp án và hướng dẫn giải chi tiết"
                          >
                            <span>📄</span> Xuất PDF Đề & Lời giải
                          </button>
                        </div>
                      )}
                    </div>
                  </div>

                  {/* BẢNG CHỌN PHÂN MÔN, KHỐI LỚP, CHƯƠNG & BÀI HỌC */}
                  <div id="khtn-filter-card" className="bg-white p-5 md:p-6 rounded-2xl shadow-sm border border-slate-200 space-y-5 no-print print:hidden">
                    {/* HÀNG 1: 2 TÙY CHỌN PHÂN MÔN */}
                    <div>
                      <label className="block text-xs font-bold uppercase text-slate-700 mb-2">
                        1. CHỌN PHÂN MÔN KHOA HỌC TỰ NHIÊN:
                      </label>
                      <div className="grid grid-cols-2 gap-3">
                        <button
                          onClick={() => setKhtnSubject("chemistry")}
                          className={`py-3 px-4 rounded-xl font-black text-sm md:text-base border transition flex items-center justify-center gap-2 ${
                            khtnSubject === "chemistry"
                              ? "bg-gradient-to-r from-teal-600 to-emerald-600 text-white shadow-md ring-2 ring-teal-300"
                              : "bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100"
                          }`}
                        >
                          <span className="text-xl">🧪</span>
                          <span>MÔN HÓA HỌC</span>
                        </button>
                        <button
                          onClick={() => setKhtnSubject("physics")}
                          className={`py-3 px-4 rounded-xl font-black text-sm md:text-base border transition flex items-center justify-center gap-2 ${
                            khtnSubject === "physics"
                              ? "bg-gradient-to-r from-amber-500 to-orange-600 text-white shadow-md ring-2 ring-amber-300"
                              : "bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100"
                          }`}
                        >
                          <span className="text-xl">⚡</span>
                          <span>MÔN VẬT LÝ</span>
                        </button>
                      </div>
                    </div>

                    {/* HÀNG 2: BỐ TRÍ 2 CỘT (CỘT TRÁI: KHỐI, CHƯƠNG, BÀI & 4 NÚT HÀNH ĐỘNG; CỘT PHẢI: MÃ ĐỀ) */}
                    <div className="grid grid-cols-1 md:grid-cols-12 gap-5 pt-3 border-t border-slate-100">
                      {/* CỘT TRÁI (md:col-span-5) */}
                      <div className="md:col-span-5 space-y-4">
                        {/* CHỌN KHỐI LỚP */}
                        <div>
                          <label className="block text-xs font-bold uppercase text-slate-700 mb-1.5">
                            2. Khối lớp:
                          </label>
                          <div className="grid grid-cols-3 gap-2">
                            {["7", "8", "9"].map((g) => (
                              <button
                                key={g}
                                onClick={() => setKhtnGrade(g)}
                                className={`py-2 px-3 rounded-xl font-bold text-xs md:text-sm border transition flex items-center justify-center gap-1 ${
                                  khtnGrade === g
                                    ? "bg-indigo-600 text-white border-indigo-600 shadow-sm"
                                    : "bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100"
                                }`}
                              >
                                <span>Lớp {g}</span>
                              </button>
                            ))}
                          </div>
                        </div>

                        {/* CHỌN CHƯƠNG */}
                        <div>
                          <label className="block text-xs font-bold uppercase text-slate-700 mb-1.5">
                            3. Chọn chương học:
                          </label>
                          <select
                            value={khtnChapterId}
                            onChange={(e) => handleSelectKhtnChapter(e.target.value)}
                            className="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs md:text-sm font-semibold text-slate-800 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                          >
                            {currentChapters.map(ch => (
                              <option key={ch.id} value={ch.id}>{ch.title}</option>
                            ))}
                          </select>
                        </div>

                        {/* CHỌN BÀI HỌC */}
                        <div>
                          <label className="block text-xs font-bold uppercase text-slate-700 mb-1.5">
                            4. Chọn bài học cụ thể:
                          </label>
                          <select
                            value={khtnLessonId}
                            onChange={(e) => handleSelectKhtnLesson(e.target.value)}
                            className="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs md:text-sm font-semibold text-slate-800 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                          >
                            {currentLessons.map(l => (
                              <option key={l.id} value={l.id}>
                                {l.isReview ? "⭐ " : ""}{l.name}
                              </option>
                            ))}
                          </select>
                        </div>

                        {/* 4 NÚT HÀNH ĐỘNG GỌN GÀNG ĐẶT PHÍA DƯỚI BÊN TRÁI */}
                        <div className="pt-2">
                          <div className="grid grid-cols-2 gap-2">
                            <button
                              onClick={() => {
                                setIsTakingKhtnOnline(!isTakingKhtnOnline);
                                setShowKhtnSolution(false);
                                setKhtnSubmitted(false);
                              }}
                              className="bg-indigo-600 hover:bg-indigo-500 text-white font-black text-xs p-2.5 rounded-xl shadow transition flex flex-col items-center justify-center gap-1 text-center"
                            >
                              <span>{isTakingKhtnOnline ? "📖 Xem đề đọc" : "💻 Vào làm bài"}</span>
                              <span className="text-[10px] opacity-80">Đề số 0{khtnTestNum}</span>
                            </button>

                            <button
                              onClick={() => handlePrintKhtnExam(false)}
                              className="bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs p-2.5 rounded-xl shadow transition flex flex-col items-center justify-center gap-1 text-center"
                              title="In Đề thi A4 chuẩn tiết kiệm giấy"
                            >
                              <span>🖨️ In Đề thi A4</span>
                              <span className="text-[10px] opacity-80">(Tiết kiệm)</span>
                            </button>

                            <button
                              onClick={() => handlePrintKhtnExam(true)}
                              className="bg-teal-600 hover:bg-teal-500 text-white font-bold text-xs p-2.5 rounded-xl shadow transition flex flex-col items-center justify-center gap-1 text-center"
                              title="Xuất PDF kèm đầy đủ đáp án và lời giải chi tiết"
                            >
                              <span>📄 Xuất PDF Đề</span>
                              <span className="text-[10px] opacity-80">& Lời giải</span>
                            </button>

                            <button
                              onClick={() => setShowKhtnSolution(!showKhtnSolution)}
                              className="bg-amber-500 hover:bg-amber-400 text-slate-950 font-black text-xs p-2.5 rounded-xl shadow transition flex flex-col items-center justify-center gap-1 text-center"
                            >
                              <span>{showKhtnSolution ? "Ẩn đáp án" : "💡 Đáp án & Giải"}</span>
                              <span className="text-[10px] opacity-80">Chi tiết 4 phần</span>
                            </button>
                          </div>
                        </div>
                      </div>

                      {/* CỘT PHẢI (md:col-span-7): CHỌN MÃ ĐỀ KIỂM TRA */}
                      <div className="md:col-span-7 bg-slate-50/70 p-4 rounded-xl border border-slate-100 flex flex-col justify-between">
                        <div>
                          <div className="flex items-center justify-between mb-3">
                            <label className="block text-xs font-bold uppercase text-slate-700">
                              5. Chọn mã đề kiểm tra ({currentLesson?.isReview ? "5 mã đề độc lập" : "3 mã đề độc lập"}):
                            </label>
                            <span className="text-[11px] bg-indigo-100 text-indigo-800 font-bold px-2 py-0.5 rounded">
                              Chuẩn ma trận 30/30/20/20
                            </span>
                          </div>

                          <div className={`grid gap-2.5 ${currentLesson?.isReview ? "grid-cols-2 sm:grid-cols-5" : "grid-cols-3"}`}>
                            {Array.from({ length: maxTests }).map((_, idx) => {
                              const tNum = idx + 1;
                              const isCur = khtnTestNum === tNum;
                              return (
                                <button
                                  key={tNum}
                                  onClick={() => {
                                    setKhtnTestNum(tNum);
                                    setIsTakingKhtnOnline(false);
                                    setKhtnSubmitted(false);
                                    setKhtnScoreResult(null);
                                    setShowKhtnSolution(false);
                                  }}
                                  className={`p-3 rounded-xl border text-center transition flex flex-col items-center justify-center gap-1 ${
                                    isCur
                                      ? "bg-indigo-600 text-white border-indigo-600 shadow-md ring-2 ring-indigo-300 font-black"
                                      : "bg-white text-slate-700 border-slate-200 hover:bg-slate-100 font-bold"
                                  }`}
                                >
                                  <span className="text-xs md:text-sm">Đề số 0{tNum}</span>
                                  <span className={`text-[10px] px-1.5 py-0.2 rounded font-semibold ${
                                    isCur ? "bg-white/20 text-white" : "bg-slate-100 text-slate-500"
                                  }`}>
                                    {tNum === 1 ? "Cơ bản - Khá" : tNum === 2 ? "Tương đương" : tNum === 3 ? "Chuẩn ma trận" : tNum === 4 ? "Vận dụng" : "Phân hóa 10"}
                                  </span>
                                </button>
                              );
                            })}
                          </div>

                          <div className="mt-4 p-3.5 bg-white rounded-xl border border-slate-200 text-xs text-slate-600 space-y-1.5">
                            <div className="font-bold text-slate-800 flex items-center gap-1.5">
                              <span>🎯</span>
                              <span>Quy chuẩn ma trận đề thi KHTN Bộ GD&ĐT:</span>
                            </div>
                            <ul className="list-disc list-inside space-y-0.5 text-[11px] text-slate-600">
                              <li><strong>Phần I:</strong> 12 câu trắc nghiệm nhiều lựa chọn (3,0 điểm)</li>
                              <li><strong>Phần II:</strong> 4 câu Đúng / Sai gồm 16 ý a,b,c,d (4,0 điểm)</li>
                              <li><strong>Phần III:</strong> 6 câu trả lời ngắn điền số/kết quả (1,5 điểm)</li>
                              <li><strong>Phần IV:</strong> 4 câu trắc nghiệm nâng cao / thực tế (1,5 điểm)</li>
                              <li>Tỷ lệ mức độ nhận thức: <strong>30% NB • 30% TH • 20% VD • 20% VDC</strong></li>
                            </ul>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>

                  {/* KHUNG HIỂN THỊ ĐỀ THI / LÀM BÀI TRỰC TUYẾN / IN ẤN TIẾT KIỆM GIẤY */}
                  {currentExam ? (
                    <div className="bg-white p-6 md:p-8 rounded-2xl shadow-sm border border-slate-200 space-y-6 khtn-printable-exam">
                      {/* HEADER ĐỀ THI CHUẨN BỘ GD&ĐT */}
                      <div className="border-b border-slate-300 pb-4 text-xs font-times">
                        <div className="flex justify-between items-start text-center">
                          <div className="w-5/12 leading-tight">
                            <div className="uppercase font-bold text-[10pt] md:text-[11pt]">SỞ GIÁO DỤC VÀ ĐÀO TẠO</div>
                            <div className="font-bold text-[10pt] md:text-[11pt]">TRƯỜNG THCS ............................</div>
                            <div className="text-[9pt] italic mt-1 font-semibold">MÃ ĐỀ: 0{khtnTestNum} • (Đề thi gồm 4 phần)</div>
                          </div>
                          <div className="w-7/12 leading-tight">
                            <div className="font-bold uppercase text-[10.5pt] md:text-[11.5pt] text-indigo-950 print:text-black">
                              BÀI KIỂM TRA MÔN KHOA HỌC TỰ NHIÊN
                            </div>
                            <div className="font-bold text-[10pt] md:text-[11pt] text-slate-800 print:text-black">
                              PHÂN MÔN: {khtnSubject === "chemistry" ? "HÓA HỌC" : "VẬT LÝ"} - KHỐI {khtnGrade}
                            </div>
                            <div className="text-[9.5pt] italic text-slate-700 print:text-black mt-0.5">
                              {currentLesson?.name}
                            </div>
                            <div className="text-[9pt] italic text-slate-600 print:text-black">
                              Thời gian làm bài: 45 phút (không kể thời gian phát đề)
                            </div>
                          </div>
                        </div>

                        {/* DÒNG TÊN HỌC SINH */}
                        <div className="flex justify-between items-center mt-3 pt-2 border-t border-slate-200 text-[10pt]">
                          <div>Họ và tên thí sinh: <strong>{studentName || "..................................................."}</strong></div>
                          <div>Lớp: <strong>{className || "..................."}</strong></div>
                          <div>SBD: <strong>...................</strong></div>
                        </div>
                      </div>

                      {/* KẾT QUẢ CHẤM ĐIỂM (NẾU ĐÃ NỘP BÀI) */}
                      {khtnSubmitted && khtnScoreResult && (
                        <div className="bg-emerald-50 border-2 border-emerald-500 rounded-2xl p-5 text-slate-800 space-y-3 no-print">
                          <div className="flex flex-wrap items-center justify-between gap-3 border-b border-emerald-200 pb-3">
                            <div className="flex items-center gap-2">
                              <span className="text-2xl">🎉</span>
                              <div>
                                <h4 className="font-black text-base text-emerald-900">KẾT QUẢ BÀI THI KHTN ONLINE</h4>
                                <p className="text-xs text-emerald-700">Học sinh: {studentName} • Lớp {className}</p>
                              </div>
                            </div>
                            <div className="text-right">
                              <div className="text-3xl font-black text-emerald-700">
                                {khtnScoreResult.total} <span className="text-sm font-bold text-slate-600">/ 10.0 điểm</span>
                              </div>
                              <div className="text-[11px] font-bold text-emerald-800">
                                {khtnScoreResult.total >= 8.0 ? "Xếp loại: Giỏi (Xuất sắc)" : khtnScoreResult.total >= 6.5 ? "Xếp loại: Khá" : khtnScoreResult.total >= 5.0 ? "Xếp loại: Đạt" : "Xếp loại: Chưa đạt"}
                              </div>
                            </div>
                          </div>

                          <div className="grid grid-cols-2 sm:grid-cols-4 gap-2.5 text-xs text-center font-bold">
                            <div className="bg-white p-2.5 rounded-xl border border-emerald-200">
                              <div className="text-slate-500 text-[10px]">Phần I (Trắc nghiệm)</div>
                              <div className="text-emerald-700 text-sm mt-0.5">{khtnScoreResult.p1Score} đ</div>
                              <div className="text-[9px] text-slate-400">Đúng {khtnScoreResult.p1CorrectCount}/12 câu</div>
                            </div>
                            <div className="bg-white p-2.5 rounded-xl border border-emerald-200">
                              <div className="text-slate-500 text-[10px]">Phần II (Đúng/Sai)</div>
                              <div className="text-emerald-700 text-sm mt-0.5">{khtnScoreResult.p2Score} đ</div>
                              <div className="text-[9px] text-slate-400">Đúng {khtnScoreResult.p2SubCorrectTotal}/16 ý</div>
                            </div>
                            <div className="bg-white p-2.5 rounded-xl border border-emerald-200">
                              <div className="text-slate-500 text-[10px]">Phần III (Trả lời ngắn)</div>
                              <div className="text-emerald-700 text-sm mt-0.5">{khtnScoreResult.p3Score} đ</div>
                              <div className="text-[9px] text-slate-400">Đúng {khtnScoreResult.p3CorrectCount}/6 câu</div>
                            </div>
                            <div className="bg-white p-2.5 rounded-xl border border-emerald-200">
                              <div className="text-slate-500 text-[10px]">Phần IV (Vận dụng cao)</div>
                              <div className="text-emerald-700 text-sm mt-0.5">{khtnScoreResult.p4Score} đ</div>
                              <div className="text-[9px] text-slate-400">Đúng {khtnScoreResult.p4CorrectCount}/4 câu</div>
                            </div>
                          </div>
                        </div>
                      )}

                      {/* NỘI DUNG 4 PHẦN THI */}
                      <div className="space-y-6 text-sm font-times leading-relaxed text-slate-900 print:text-black">
                        {/* PHẦN I: TRẮC NGHIỆM NHIỀU LỰA CHỌN */}
                        <div className="space-y-3">
                          <div className="font-bold text-xs md:text-sm uppercase tracking-wider text-indigo-950 print:text-black border-b border-indigo-200 print:border-black pb-1">
                            I. PHẦN TRẮC NGHIỆM NHIỀU LỰA CHỌN (3,0 ĐIỂM - 12 CÂU, MỖI CÂU 0,25 ĐIỂM)
                          </div>
                          <div className="space-y-3.5">
                            {currentExam.part1.map((q, idx) => {
                              const letters = ["A", "B", "C", "D"];
                              const maxLen = Math.max(...q.options.map(o => String(o).length));
                              const gridCols = maxLen <= 16 ? "grid-cols-2 sm:grid-cols-4" : maxLen <= 45 ? "grid-cols-1 sm:grid-cols-2" : "grid-cols-1";
                              const userAns = khtnAnswers.p1[q.id];

                              return (
                                <div key={q.id} className="space-y-1.5 break-inside-avoid">
                                  <div className="font-semibold text-slate-900 print:text-black">
                                    <span className="font-bold">**Câu {idx + 1}:** </span>
                                    <span>{q.question}</span>
                                    <span className="text-[9.5pt] italic text-slate-500 print:hidden ml-1.5 font-normal">({q.level})</span>
                                  </div>

                                  <div className={`grid gap-1.5 ${gridCols}`}>
                                    {q.options.map((opt, oIdx) => {
                                      const isChosen = userAns === oIdx;
                                      const isCorrect = showKhtnSolution && q.correct === oIdx;
                                      const isWrong = showKhtnSolution && isChosen && q.correct !== oIdx;

                                      return (
                                        <div
                                          key={oIdx}
                                          onClick={() => {
                                            if (isTakingKhtnOnline && !khtnSubmitted) {
                                              setKhtnAnswers(prev => ({
                                                ...prev,
                                                p1: { ...prev.p1, [q.id]: oIdx }
                                              }));
                                            }
                                          }}
                                          className={`p-1.5 rounded-lg border text-xs transition flex items-center gap-1.5 ${
                                            isCorrect
                                              ? "bg-emerald-100 border-emerald-500 font-bold text-emerald-950 print:bg-transparent print:border-none"
                                              : isWrong
                                              ? "bg-rose-100 border-rose-400 text-rose-950 print:bg-transparent print:border-none"
                                              : isChosen
                                              ? "bg-indigo-50 border-indigo-500 font-bold text-indigo-950 print:bg-transparent print:border-none"
                                              : "bg-white border-transparent hover:border-slate-300 print:bg-transparent print:border-none"
                                          } ${isTakingKhtnOnline && !khtnSubmitted ? "cursor-pointer" : ""}`}
                                        >
                                          <span className="font-bold min-w-[20px]">{letters[oIdx]}.</span>
                                          <span>{opt}</span>
                                        </div>
                                      );
                                    })}
                                  </div>

                                  {showKhtnSolution && q.explanation && (
                                    <div className="p-2 bg-indigo-50/70 text-indigo-900 rounded-lg text-xs italic mt-1 border-l-2 border-indigo-500 print:hidden">
                                      <strong>Hướng dẫn giải:</strong> {q.explanation}
                                    </div>
                                  )}
                                </div>
                              );
                            })}
                          </div>
                        </div>

                        {/* PHẦN II: TRẮC NGHIỆM ĐÚNG / SAI */}
                        <div className="space-y-3 pt-3 border-t border-slate-200">
                          <div className="font-bold text-xs md:text-sm uppercase tracking-wider text-indigo-950 print:text-black border-b border-indigo-200 print:border-black pb-1">
                            II. PHẦN TRẮC NGHIỆM ĐÚNG / SAI (4,0 ĐIỂM - 4 CÂU, MỖI CÂU 1,0 ĐIỂM)
                          </div>
                          <div className="space-y-4">
                            {currentExam.part2.map((q, idx) => {
                              const userSub = khtnAnswers.p2[q.id] || {};

                              return (
                                <div key={q.id} className="space-y-2 break-inside-avoid">
                                  <div className="font-semibold text-slate-900 print:text-black">
                                    <span className="font-bold">**Câu {idx + 1}:** </span>
                                    <span>{q.question}</span>
                                  </div>

                                  <div className="border border-slate-300 print:border-black rounded-lg overflow-hidden text-xs">
                                    <table className="w-full text-left border-collapse">
                                      <thead>
                                        <tr className="bg-slate-100 print:bg-transparent border-b border-slate-300 print:border-black font-bold">
                                          <th className="p-2 w-8 text-center">Ý</th>
                                          <th className="p-2">Nội dung mệnh đề khẳng định</th>
                                          <th className="p-2 w-28 text-center">Đúng / Sai</th>
                                        </tr>
                                      </thead>
                                      <tbody>
                                        {q.statements.map((st) => {
                                          const userVal = userSub[st.subId];

                                          return (
                                            <tr key={st.subId} className="border-b border-slate-200 print:border-black last:border-b-0">
                                              <td className="p-2 font-bold text-center">{st.subId})</td>
                                              <td className="p-2">{st.text}</td>
                                              <td className="p-2 text-center whitespace-nowrap">
                                                {isTakingKhtnOnline && !khtnSubmitted ? (
                                                  <div className="flex items-center justify-center gap-1.5">
                                                    <button
                                                      onClick={() => {
                                                        setKhtnAnswers(prev => ({
                                                          ...prev,
                                                          p2: {
                                                            ...prev.p2,
                                                            [q.id]: { ...(prev.p2[q.id] || {}), [st.subId]: true }
                                                          }
                                                        }));
                                                      }}
                                                      className={`px-2 py-0.5 rounded text-[11px] font-bold border transition ${
                                                        userVal === true ? "bg-emerald-600 text-white border-emerald-600" : "bg-white text-slate-600 hover:bg-slate-100"
                                                      }`}
                                                    >
                                                      Đ
                                                    </button>
                                                    <button
                                                      onClick={() => {
                                                        setKhtnAnswers(prev => ({
                                                          ...prev,
                                                          p2: {
                                                            ...prev.p2,
                                                            [q.id]: { ...(prev.p2[q.id] || {}), [st.subId]: false }
                                                          }
                                                        }));
                                                      }}
                                                      className={`px-2 py-0.5 rounded text-[11px] font-bold border transition ${
                                                        userVal === false ? "bg-rose-600 text-white border-rose-600" : "bg-white text-slate-600 hover:bg-slate-100"
                                                      }`}
                                                    >
                                                      S
                                                    </button>
                                                  </div>
                                                ) : showKhtnSolution ? (
                                                  <span className={`font-black px-2 py-0.5 rounded text-xs ${
                                                    st.correct ? "bg-emerald-100 text-emerald-800" : "bg-rose-100 text-rose-800"
                                                  }`}>
                                                    {st.correct ? "ĐÚNG" : "SAI"}
                                                  </span>
                                                ) : (
                                                  <span className="text-slate-400 print:text-black">[ Đ / S ]</span>
                                                )}
                                              </td>
                                            </tr>
                                          );
                                        })}
                                      </tbody>
                                    </table>
                                  </div>

                                  {showKhtnSolution && q.explanation && (
                                    <div className="p-2 bg-indigo-50/70 text-indigo-900 rounded-lg text-xs italic mt-1 border-l-2 border-indigo-500 print:hidden">
                                      <strong>Hướng dẫn giải:</strong> {q.explanation}
                                    </div>
                                  )}
                                </div>
                              );
                            })}
                          </div>
                        </div>

                        {/* PHẦN III: TRẢ LỜI NGẮN */}
                        <div className="space-y-3 pt-3 border-t border-slate-200">
                          <div className="font-bold text-xs md:text-sm uppercase tracking-wider text-indigo-950 print:text-black border-b border-indigo-200 print:border-black pb-1">
                            III. PHẦN TRẮC NGHIỆM TRẢ LỜI NGẮN (1,5 ĐIỂM - 6 CÂU, MỖI CÂU 0,25 ĐIỂM)
                          </div>
                          <div className="grid grid-cols-1 md:grid-cols-2 gap-3.5">
                            {currentExam.part3.map((q, idx) => {
                              const userStr = khtnAnswers.p3[q.id] || "";

                              return (
                                <div key={q.id} className="p-2.5 rounded-xl border border-slate-200 print:border-transparent space-y-2 break-inside-avoid">
                                  <div className="font-semibold text-slate-900 print:text-black">
                                    <span className="font-bold">**Câu {idx + 1}:** </span>
                                    <span>{q.question}</span>
                                  </div>

                                  {isTakingKhtnOnline && !khtnSubmitted ? (
                                    <div className="flex items-center gap-2">
                                      <span className="text-xs font-bold text-slate-500">Điền đáp số:</span>
                                      <input
                                        type="text"
                                        value={userStr}
                                        onChange={(e) => {
                                          setKhtnAnswers(prev => ({
                                            ...prev,
                                            p3: { ...prev.p3, [q.id]: e.target.value }
                                          }));
                                        }}
                                        placeholder="Nhập số hoặc từ ngắn..."
                                        className="bg-slate-50 border border-slate-300 rounded-lg px-2.5 py-1 text-xs font-bold text-slate-900 w-44 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                                      />
                                    </div>
                                  ) : showKhtnSolution ? (
                                    <div className="text-xs space-y-1">
                                      <div className="font-bold text-emerald-700">
                                        Đáp án đúng: <span>{q.correctAnswer}</span>
                                      </div>
                                      {q.explanation && (
                                        <div className="text-slate-600 italic text-[11px]">
                                          {q.explanation}
                                        </div>
                                      )}
                                    </div>
                                  ) : null}
                                </div>
                              );
                            })}
                          </div>
                        </div>

                        {/* PHẦN IV: TRẮC NGHIỆM VẬN DỤNG CAO / THỰC TẾ KHTN */}
                        <div className="space-y-3 pt-3 border-t border-slate-200">
                          <div className="font-bold text-xs md:text-sm uppercase tracking-wider text-indigo-950 print:text-black border-b border-indigo-200 print:border-black pb-1">
                            IV. PHẦN TRẮC NGHIỆM VẬN DỤNG CAO & THỰC TIỄN (1,5 ĐIỂM - 4 CÂU, MỖI CÂU 0,375 ĐIỂM)
                          </div>
                          <div className="space-y-3.5">
                            {currentExam.part4.map((q, idx) => {
                              const letters = ["A", "B", "C", "D"];
                              const userAns = khtnAnswers.p4[q.id];

                              return (
                                <div key={q.id} className="space-y-1.5 break-inside-avoid">
                                  <div className="font-semibold text-slate-900 print:text-black">
                                    <span className="font-bold">**Câu {idx + 1}:** </span>
                                    <span>{q.question}</span>
                                    <span className="text-[9.5pt] italic text-amber-600 print:hidden ml-1.5 font-bold">[Vận dụng cao]</span>
                                  </div>

                                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-1.5">
                                    {q.options.map((opt, oIdx) => {
                                      const isChosen = userAns === oIdx;
                                      const isCorrect = showKhtnSolution && q.correct === oIdx;
                                      const isWrong = showKhtnSolution && isChosen && q.correct !== oIdx;

                                      return (
                                        <div
                                          key={oIdx}
                                          onClick={() => {
                                            if (isTakingKhtnOnline && !khtnSubmitted) {
                                              setKhtnAnswers(prev => ({
                                                ...prev,
                                                p4: { ...prev.p4, [q.id]: oIdx }
                                              }));
                                            }
                                          }}
                                          className={`p-1.5 rounded-lg border text-xs transition flex items-center gap-1.5 ${
                                            isCorrect
                                              ? "bg-emerald-100 border-emerald-500 font-bold text-emerald-950 print:bg-transparent print:border-none"
                                              : isWrong
                                              ? "bg-rose-100 border-rose-400 text-rose-950 print:bg-transparent print:border-none"
                                              : isChosen
                                              ? "bg-indigo-50 border-indigo-500 font-bold text-indigo-950 print:bg-transparent print:border-none"
                                              : "bg-white border-transparent hover:border-slate-300 print:bg-transparent print:border-none"
                                          } ${isTakingKhtnOnline && !khtnSubmitted ? "cursor-pointer" : ""}`}
                                        >
                                          <span className="font-bold min-w-[20px]">{letters[oIdx]}.</span>
                                          <span>{opt}</span>
                                        </div>
                                      );
                                    })}
                                  </div>

                                  {showKhtnSolution && q.explanation && (
                                    <div className="p-2 bg-indigo-50/70 text-indigo-900 rounded-lg text-xs italic mt-1 border-l-2 border-indigo-500 print:hidden">
                                      <strong>Hướng dẫn giải:</strong> {q.explanation}
                                    </div>
                                  )}
                                </div>
                              );
                            })}
                          </div>
                        </div>

                        {/* NÚT NỘP BÀI TRỰC TUYẾN KHI ĐANG LÀM BÀI */}
                        {isTakingKhtnOnline && !khtnSubmitted && (
                          <div className="pt-6 text-center no-print">
                            <button
                              onClick={handleGradeKhtnOnline}
                              className="bg-emerald-600 hover:bg-emerald-500 text-white font-black px-8 py-3 rounded-2xl shadow-lg hover:shadow-xl text-base transition duration-200 transform hover:-translate-y-0.5"
                            >
                              🚀 NỘP BÀI & CHẤM ĐIỂM TỰ ĐỘNG
                            </button>
                            <p className="text-xs text-slate-500 mt-2">Hệ thống sẽ chấm điểm 4 phần và hiển thị lời giải chi tiết</p>
                          </div>
                        )}

                        {/* DÒNG HẾT KHI IN */}
                        <div className="text-center font-bold text-[11pt] md:text-[12pt] pt-3 mt-3 border-t border-slate-300 print:border-black font-times">
                          <div>------------------ HẾT ------------------</div>
                          <div className="text-[10pt] font-normal italic mt-0.5 text-slate-600 print:text-black">
                            Thí sinh không được sử dụng tài liệu. Giám thị không giải thích gì thêm.
                          </div>
                        </div>
                      </div>
                    </div>
                  ) : (
                    <div className="bg-white p-8 rounded-2xl border text-center text-slate-500">
                      Đang tải dữ liệu đề thi KHTN...
                    </div>
                  )}
                </div>
              );
            })()}
"""

target_marker = "{/* ============================================================== */}\n            {/* MÀN HÌNH CHUYÊN ĐỀ: ÔN THI VÀO LỚP 10 THEO CHỦ ĐỀ"
if "{view === \"khtn\"" not in content:
    content = content.replace(target_marker, khtn_view_jsx + "\n\n            " + target_marker)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ Đã chèn thành công MÀN HÌNH KHTN vào index.html!")
else:
    print("Màn hình KHTN đã tồn tại trong index.html.")
