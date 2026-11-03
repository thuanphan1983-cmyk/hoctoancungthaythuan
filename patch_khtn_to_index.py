# -*- coding: utf-8 -*-
"""
Script cập nhật index.html tích hợp toàn bộ tính năng MÔN: KHTN
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Thêm thẻ script khtnExamsData.js vào <head>
if "khtnExamsData.js" not in content:
    target_script = '<script src="periodicExamsData.js"></script>'
    replacement_script = '<script src="periodicExamsData.js"></script>\n  <!-- KHTN Database (Hóa học & Vật lý 7, 8, 9 - KNTT) -->\n  <script src="khtnExamsData.js"></script>'
    content = content.replace(target_script, replacement_script)
    print("1. Đã thêm script khtnExamsData.js vào head.")
else:
    print("1. Script khtnExamsData.js đã có sẵn.")

# 2. Thêm CSS ẩn khi in cho KHTN
if "#khtn-banner-card" not in content:
    target_css = "#periodic-filter-card,"
    replacement_css = "#periodic-filter-card,\n      #khtn-banner-card,\n      #khtn-filter-card,"
    content = content.replace(target_css, replacement_css)
    content = content.replace(".topic-printable-exam {", ".topic-printable-exam,\n      .khtn-printable-exam {")
    print("2. Đã thêm quy chuẩn in ấn tiết kiệm giấy cho KHTN.")

# 3. Thêm state và logic KHTN trong App Component
khtn_state_code = """
      // ==============================================================
      // STATE CHUYÊN DỤNG CHO MÔN KHTN (HÓA HỌC & VẬT LÝ 7, 8, 9)
      // ==============================================================
      const [khtnSubject, setKhtnSubject] = useState("chemistry"); // 'chemistry' | 'physics'
      const [khtnGrade, setKhtnGrade] = useState("8"); // '7' | '8' | '9'
      const [khtnChapterId, setKhtnChapterId] = useState("chem8_c1");
      const [khtnLessonId, setKhtnLessonId] = useState("chem8_c1_b2");
      const [khtnTestNum, setKhtnTestNum] = useState(1);
      const [showKhtnSolution, setShowKhtnSolution] = useState(false);
      const [isTakingKhtnOnline, setIsTakingKhtnOnline] = useState(false);
      const [khtnAnswers, setKhtnAnswers] = useState({
        p1: {},
        p2: {},
        p3: {},
        p4: {}
      });
      const [khtnSubmitted, setKhtnSubmitted] = useState(false);
      const [khtnScoreResult, setKhtnScoreResult] = useState(null);

      // Tự động đồng bộ chương và bài học khi đổi môn hoặc khối lớp KHTN
      useEffect(() => {
        const curr = (typeof window !== "undefined" && window.KHTN_CURRICULUM) || {};
        const subjObj = curr[khtnSubject];
        if (!subjObj) return;
        const gradeObj = subjObj.grades?.[khtnGrade];
        if (!gradeObj || !gradeObj.chapters || gradeObj.chapters.length === 0) return;
        
        const ch = gradeObj.chapters.find(c => c.id === khtnChapterId) || gradeObj.chapters[0];
        setKhtnChapterId(ch.id);
        const l = ch.lessons?.find(item => item.id === khtnLessonId) || ch.lessons?.[0];
        if (l) {
          setKhtnLessonId(l.id);
        }
        setKhtnTestNum(1);
        setIsTakingKhtnOnline(false);
        setKhtnSubmitted(false);
        setKhtnScoreResult(null);
      }, [khtnSubject, khtnGrade]);

      const handleSelectKhtnChapter = (chId) => {
        setKhtnChapterId(chId);
        const curr = (typeof window !== "undefined" && window.KHTN_CURRICULUM) || {};
        const ch = curr[khtnSubject]?.grades?.[khtnGrade]?.chapters?.find(c => c.id === chId);
        if (ch && ch.lessons && ch.lessons.length > 0) {
          setKhtnLessonId(ch.lessons[0].id);
        }
        setKhtnTestNum(1);
        setIsTakingKhtnOnline(false);
        setKhtnSubmitted(false);
        setKhtnScoreResult(null);
      };

      const handleSelectKhtnLesson = (lId) => {
        setKhtnLessonId(lId);
        setKhtnTestNum(1);
        setIsTakingKhtnOnline(false);
        setKhtnSubmitted(false);
        setKhtnScoreResult(null);
      };

      const getKhtnExam = () => {
        const examKey = `${khtnLessonId}_test${khtnTestNum}`;
        const bank = (typeof window !== "undefined" && window.KHTN_EXAMS_DATA) || {};
        return bank[examKey] || null;
      };

      const handlePrintKhtnExam = (includeSolution = false) => {
        if (!studentName.trim() || !className.trim()) {
          alert("Vui lòng nhập đầy đủ Họ và tên học sinh cùng Lớp học trước khi in hoặc xuất PDF!");
          return;
        }
        setShowKhtnSolution(includeSolution);
        
        const subjName = khtnSubject === "chemistry" ? "HOA HOC" : "VAT LY";
        const curr = (typeof window !== "undefined" && window.KHTN_CURRICULUM) || {};
        const ch = curr[khtnSubject]?.grades?.[khtnGrade]?.chapters?.find(c => c.id === khtnChapterId);
        const l = ch?.lessons?.find(item => item.id === khtnLessonId);
        const lName = l ? l.name.replace(/[:\/]/g, '_').toUpperCase() : "BAI HOC";
        const solTag = includeSolution ? " - DAP AN VA LOI GIAI" : "";
        const cleanTitle = `KHTN ${khtnGrade} - ${subjName} - ${lName} - DE SO ${khtnTestNum < 10 ? '0' + khtnTestNum : khtnTestNum}${solTag}`.trim();
        
        const origTitle = document.title;
        document.title = cleanTitle;
        setTimeout(() => {
          window.print();
          setTimeout(() => {
            document.title = origTitle;
          }, 1500);
        }, 150);
      };

      const handleGradeKhtnOnline = () => {
        const ex = getKhtnExam();
        if (!ex) return;
        
        let p1Score = 0;
        let p1CorrectCount = 0;
        ex.part1.forEach(q => {
          if (khtnAnswers.p1[q.id] === q.correct) {
            p1Score += 0.25;
            p1CorrectCount++;
          }
        });

        let p2Score = 0;
        let p2SubCorrectTotal = 0;
        ex.part2.forEach(q => {
          const userSub = khtnAnswers.p2[q.id] || {};
          let subCount = 0;
          q.statements.forEach(st => {
            if (userSub[st.subId] === st.correct) {
              subCount++;
              p2SubCorrectTotal++;
            }
          });
          if (subCount === 1) p2Score += 0.1;
          else if (subCount === 2) p2Score += 0.25;
          else if (subCount === 3) p2Score += 0.5;
          else if (subCount === 4) p2Score += 1.0;
        });

        let p3Score = 0;
        let p3CorrectCount = 0;
        ex.part3.forEach(q => {
          const userStr = (khtnAnswers.p3[q.id] || "").trim().toLowerCase();
          const correctStr = String(q.correctAnswer).trim().toLowerCase();
          if (userStr && (userStr === correctStr || (parseFloat(userStr) === parseFloat(correctStr) && !isNaN(parseFloat(userStr))))) {
            p3Score += 0.25;
            p3CorrectCount++;
          }
        });

        let p4Score = 0;
        let p4CorrectCount = 0;
        ex.part4.forEach(q => {
          if (khtnAnswers.p4[q.id] === q.correct) {
            p4Score += 0.375;
            p4CorrectCount++;
          }
        });

        const total = Math.round((p1Score + p2Score + p3Score + p4Score) * 100) / 100;
        setKhtnScoreResult({
          total,
          p1Score: Math.round(p1Score * 100) / 100,
          p2Score: Math.round(p2Score * 100) / 100,
          p3Score: Math.round(p3Score * 100) / 100,
          p4Score: Math.round(p4Score * 100) / 100,
          p1CorrectCount,
          p2SubCorrectTotal,
          p3CorrectCount,
          p4CorrectCount
        });
        setKhtnSubmitted(true);
        setShowKhtnSolution(true);
      };
"""

if "setKhtnSubject" not in content:
    target_state_anchor = "const [topicsData, setTopicsData] = useState("
    content = content.replace(target_state_anchor, khtn_state_code + "\n      " + target_state_anchor)
    print("3. Đã thêm State & Handler KHTN vào App component.")

# 4. Thêm view === 'khtn' vào handleNavigateTab
if 'targetTab === "khtn"' not in content:
    target_nav = 'else if (targetTab === "periodic_exam") {\n          setView("periodic_exam");\n        }'
    replacement_nav = 'else if (targetTab === "periodic_exam") {\n          setView("periodic_exam");\n        } else if (targetTab === "khtn") {\n          setView("khtn");\n        }'
    content = content.replace(target_nav, replacement_nav)
    print("4. Đã thêm targetTab 'khtn' vào handleNavigateTab.")

# 5. Thêm nút MÔN: KHTN vào Navigation bar
if "<span>🔬</span> MÔN: KHTN" not in content:
    target_button = """                {/* NÚT 3: 📝 ÔN TẬP ĐỊNH KỲ */}
                <button
                  onClick={() => handleNavigateTab("periodic_exam")}
                  className={`px-3.5 md:px-4 py-2 rounded-xl text-xs md:text-sm font-bold flex items-center gap-1.5 transition ${
                    view === "periodic_exam"
                      ? "bg-emerald-400 text-slate-950 shadow-md ring-2 ring-emerald-300 font-black"
                      : "bg-indigo-800 hover:bg-indigo-700 text-white"
                  }`}
                >
                  <span>📝</span> ÔN TẬP ĐỊNH KỲ
                </button>"""

    replacement_button = """                {/* NÚT 3: 📝 ÔN TẬP ĐỊNH KỲ */}
                <button
                  onClick={() => handleNavigateTab("periodic_exam")}
                  className={`px-3.5 md:px-4 py-2 rounded-xl text-xs md:text-sm font-bold flex items-center gap-1.5 transition ${
                    view === "periodic_exam"
                      ? "bg-emerald-400 text-slate-950 shadow-md ring-2 ring-emerald-300 font-black"
                      : "bg-indigo-800 hover:bg-indigo-700 text-white"
                  }`}
                >
                  <span>📝</span> ÔN TẬP ĐỊNH KỲ
                </button>

                {/* NÚT 4: 🔬 MÔN: KHTN */}
                <button
                  onClick={() => handleNavigateTab("khtn")}
                  className={`px-3.5 md:px-4 py-2 rounded-xl text-xs md:text-sm font-bold flex items-center gap-1.5 transition ${
                    view === "khtn"
                      ? "bg-teal-400 text-slate-950 shadow-md ring-2 ring-teal-300 font-black"
                      : "bg-indigo-800 hover:bg-indigo-700 text-white"
                  }`}
                  title="Hệ thống đề ôn tập môn Khoa học tự nhiên (Hóa học & Vật lý 7, 8, 9)"
                >
                  <span>🔬</span> MÔN: KHTN
                </button>"""
    content = content.replace(target_button, replacement_button)
    print("5. Đã thêm nút '🔬 MÔN: KHTN' vào Navigation bar.")

# 6. Thêm view === 'khtn' vào student-info-section
if 'view === "khtn"' not in content:
    target_stu = 'view === "periodic_exam"'
    replacement_stu = 'view === "periodic_exam" || view === "khtn"'
    content = content.replace(target_stu, replacement_stu)
    print("6. Đã thêm view 'khtn' vào student-info-section.")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Đã hoàn tất bước 1 cập nhật index.html!")
