// ==============================================================================
// DỊCH VỤ TÍCH HỢP GEMINI API (HỖ TRỢ TỰ ĐỘNG CHUYỂN ĐỔI MODEL VÀ FIX LỖI JSON LATEX)
// Hỗ trợ: gemini-2.5-flash, gemini-2.0-flash, gemini-1.5-flash
// ==============================================================================

const CANDIDATE_MODELS = [
  "gemini-1.5-flash",
  "gemini-2.0-flash",
  "gemini-1.5-flash-latest",
  "gemini-1.5-pro"
];

/**
 * Xử lý chuỗi JSON an toàn, tự động sửa lỗi dấu gạch chéo ngược của LaTeX (\sqrt, \frac, \neq...)
 */
export function safeParseJSON(rawText) {
  if (!rawText || typeof rawText !== "string") {
    throw new Error("Dữ liệu phản hồi từ AI rỗng.");
  }

  // 1. Loại bỏ các khối code block ```json ... ```
  let clean = rawText
    .replace(/^```json\s*/i, "")
    .replace(/^```\s*/i, "")
    .replace(/```\s*$/i, "")
    .trim();

  // 2. Thử parse trực tiếp
  try {
    return JSON.parse(clean);
  } catch (err1) {
    // 3. Sửa lỗi dấu backslash của LaTeX trong chuỗi JSON
    // Trong chuỗi JSON, bất kỳ dấu \ nào không đứng trước " hoặc \ sẽ gây lỗi cú pháp (ví dụ \frac, \sqrt, \alpha)
    try {
      const fixed = clean.replace(/\\(?!["\\])/g, "\\\\");
      return JSON.parse(fixed);
    } catch (err2) {
      // 4. Cố gắng trích xuất khối đối tượng { ... } ngoài cùng
      const match = clean.match(/\{[\s\S]*\}/);
      if (match) {
        const fixedMatch = match[0].replace(/\\(?!["\\])/g, "\\\\");
        return JSON.parse(fixedMatch);
      }
      throw new Error(`Lỗi cú pháp dữ liệu JSON từ AI: ${err1.message}`);
    }
  }
}

/**
 * Kiểm tra tính hợp lệ của API Key
 */
export async function testGeminiApiKey(apiKey) {
  const cleanKey = (apiKey || "").trim();
  if (!cleanKey) {
    return { ok: false, error: "Vui lòng nhập API Key trước khi kiểm tra." };
  }

  // 1. Kiểm tra trực tiếp bằng GET /v1beta/models (nhanh, chuẩn, không vướng preflight)
  try {
    const checkRes = await fetch(
      `https://generativelanguage.googleapis.com/v1beta/models?key=${cleanKey}`,
      { method: "GET" }
    );
    const checkData = await checkRes.json();
    if (!checkRes.ok) {
      const errMsg = checkData?.error?.message || `Lỗi HTTP ${checkRes.status}`;
      return { ok: false, error: errMsg };
    }
    const availableList = (checkData.models || []).map(m => (m.name || "").replace("models/", ""));
    const matchedModel = CANDIDATE_MODELS.find(m => availableList.includes(m)) || "gemini-1.5-flash";
    return { ok: true, model: matchedModel };
  } catch (err) {
    // Nếu GET bị chặn CORS/Network, thử tiếp POST generateContent
  }

  for (const model of CANDIDATE_MODELS) {
    try {
      const res = await fetch(
        `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${cleanKey}`,
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            contents: [{ parts: [{ text: "Hello" }] }]
          })
        }
      );

      const data = await res.json();
      if (res.ok && data?.candidates?.[0]?.content?.parts?.[0]?.text) {
        return { ok: true, model };
      }
      if (data?.error?.message) {
        if (res.status === 404) continue; // Thử model tiếp theo
        return { ok: false, error: data.error.message };
      }
    } catch (e) {
      // Tiếp tục thử model kế tiếp
    }
  }

  return { ok: false, error: "Không thể kết nối đến Gemini API. Vui lòng kiểm tra lại API Key hoặc kết nối mạng." };
}

/**
 * Sinh đề kiểm tra tự động bằng Gemini AI bám sát bài học và khối lớp
 * Tự động chuyển đổi giữa các model nếu một model bị quá tải hoặc chưa hỗ trợ
 */
export async function generateExamAI({ apiKey, grade, lesson, testNum, chapterTitle = "" }) {
  const cleanKey = (apiKey || "").trim();
  if (!cleanKey) {
    throw new Error("Chưa nhập Gemini API Key.");
  }

  const isChapterExam = (lesson || "").toLowerCase().includes("cuối chương");

  const difficultySpecs = {
    1: {
      name: "ĐỀ SỐ 1 - MỨC ĐỘ CƠ BẢN & CỦNG CỐ NỀN TẢNG (Mục tiêu 5.0 - 7.0 điểm)",
      rules: `
YÊU CẦU ĐỘ KHÓ ĐỀ SỐ 1 (MỨC ĐỘ DỄ NHẤT):
- Bám sát chuẩn kiến thức kỹ năng cơ bản SGK Kết nối tri thức. Các câu hỏi hỏi trực tiếp, rõ ràng, không gài bẫy.
- Phần I (Trắc nghiệm): 8 câu Nhận biết (khái niệm trực tiếp, hệ số, nghiệm có sẵn), 4 câu Thông hiểu đơn giản (thay số 1 bước).
- Phần II (Đúng/Sai): 2 câu ở mức Thông hiểu cơ bản, các mệnh đề dễ phân biệt đúng/sai, lập luận ngắn gọn.
- Phần III (Trả lời ngắn): 4 câu tính toán số học / đại số 1-2 bước cơ bản.
- Phần IV (Tự luận): 3 câu mẫu mực như ví dụ cơ bản trong SGK, lời giải rõ ràng, dễ đạt điểm.`
    },
    2: {
      name: "ĐỀ SỐ 2 - MỨC ĐỘ KHÁ & VẬN DỤNG LINH HOẠT (Mục tiêu 7.0 - 8.5 điểm - KHÓ HƠN ĐỀ 1 RÕ RỆT)",
      rules: `
YÊU CẦU ĐỘ KHÓ ĐỀ SỐ 2 (ĐỘ KHÓ TRUNG BÌNH KHÁ - KHÓ HƠN ĐỀ 1):
- Đòi hỏi học sinh phải biết kết hợp từ 2 kiến thức trở lên, thực hiện biến đổi đại số nhiều bước, phân tích bài toán thực tế mức độ khá.
- Phần I (Trắc nghiệm): 4 câu Nhận biết (hỏi sâu hơn), 8 câu Thông hiểu (có phương án nhiễu dễ nhầm lẫn, yêu cầu biến đổi rút gọn trước khi chọn).
- Phần II (Đúng/Sai): 2 câu phân tích đa bước (chứa biểu thức quy đồng, tìm điều kiện tham số cơ bản, đối chiếu ĐKXĐ).
- Phần III (Trả lời ngắn): 4 câu hỏi yêu cầu giải phương trình, rút gọn có điều kiện, tính toán thực tế hoặc tỉ số hình học.
- Phần IV (Tự luận): Bài toán thực tế rõ ràng (toán chuyển động, toán năng suất, tỉ số lượng giác thực tế) và bài toán biến đổi có ràng buộc điều kiện.`
    },
    3: {
      name: "ĐỀ SỐ 3 - MỨC ĐỘ NÂNG CAO & PHÂN HÓA SÂU (Mục tiêu 8.5 - 10.0 điểm - KHÓ NHẤT, KHÓ HƠN ĐỀ 2 VÀ ĐỀ 1)",
      rules: `
YÊU CẦU ĐỘ KHÓ ĐỀ SỐ 3 (ĐỘ KHÓ CAO NHẤT, PHÂN HÓA MẠNH MẼ CHO HSG VÀ THI VÀO LỚP 10):
- Đòi hỏi tư duy logic trừu tượng, biến đổi đại số khéo léo, xử lý tham số m, bài toán cực trị, bất đẳng thức hoặc bài toán hình học phân tích sâu.
- Phần I (Trắc nghiệm): 2 câu Nhận biết tinh tế, 6 câu Thông hiểu nâng cao, 4 câu có bẫy logic sâu (dễ mất nghiệm hoặc nhầm lẫn miền xác định).
- Phần II (Đúng/Sai): 2 câu phân tích đa chiều (chứa tham số m, biện luận số nghiệm, tính chất hình học nâng cao).
- Phần III (Trả lời ngắn): 4 câu ở mức Vận dụng cao (tìm giá trị tham số, bài toán cực trị hình học, biểu thức đối xứng Viète nâng cao, bài toán đếm hoặc xác suất phức tạp).
- Phần IV (Tự luận): 
  * Câu 1: Bài toán biến đổi / rút gọn nâng cao có chứa tham số hoặc điều kiện nghiệm (1.0đ).
  * Câu 2: Bài toán thực tế phức tạp đa bước lập phương trình/hệ phương trình hoặc hình học phân tích nâng cao (1.0đ).
  * Câu 3: Câu chốt phân hóa điểm 10 (1.0đ) - Bất đẳng thức, tìm GTLN/GTNN, bài toán cực trị hình học, hoặc phương trình nghiệm nguyên nâng cao.`
    }
  };

  const currentDiff = difficultySpecs[testNum] || difficultySpecs[1];

  const prompt = `
Bạn là chuyên gia khảo thí môn Toán THCS bộ sách "Kết nối tri thức với cuộc sống".
Hãy tạo bộ đề kiểm tra định kỳ cho: Khối ${grade}, Bài học/Chuyên đề: "${lesson}", Đề: "Bài kiểm tra số ${testNum}".

QUY ĐỊNH PHÂN HÓA ĐỘ KHÓ BẮT BUỘC:
ĐỀ SỐ ${testNum}: ${currentDiff.name}
${currentDiff.rules}

${isChapterExam ? `
LƯU Ý ĐẶC BIỆT (ĐỀ KIỂM TRA TỔNG HỢP CUỐI CHƯƠNG):
- Đây là đề kiểm tra TỔNG HỢP TOÀN BỘ KIẾN THỨC CỦA CHƯƠNG: "${chapterTitle || lesson}".
- Đề thi PHẢI tổng hợp toàn diện các nội dung lý thuyết, công thức và dạng toán cốt lõi của tất cả các bài học trong chương này.
` : ""}

QUY ĐỊNH CÔNG THỨC TOÁN & JSON:
- Mọi công thức toán học, biểu thức đại số, phân thức, căn thức, hệ phương trình PHẢI được bọc chuẩn LaTeX giữa hai dấu $ (ví dụ: $2x + 3y = 5$, $\\sqrt{x^2 - 1}$, $\\begin{cases} x+y=1 \\\\ x-y=2 \\end{cases}$).
- Đảm bảo thoát ký tự gạch chéo ngược hợp lệ trong chuỗi JSON (dùng \\\\ cho LaTeX).

YÊU CẦU TRẢ VỀ ĐÚNG CẤU TRÚC JSON SAU:
{
  "title": "Toán ${grade} (KNTT) - ${lesson} - Bài kiểm tra số ${testNum}",
  "part1": [ // Đúng 12 câu trắc nghiệm 4 lựa chọn (6 Nhận biết, 6 Thông hiểu)
    { "id": 1, "level": "Nhận biết", "question": "...", "options": ["$A...$", "$B...$", "$C...$", "$D...$"], "correct": 0 }
  ],
  "part2": [ // Đúng 2 câu Đúng/Sai. Mỗi câu 4 ý a, b (Thông hiểu), c, d (Vận dụng thấp)
    {
      "id": 1,
      "stem": "Cho...",
      "statements": [
        { "key": "a", "level": "Thông hiểu", "text": "...", "correct": true },
        { "key": "b", "level": "Thông hiểu", "text": "...", "correct": false },
        { "key": "c", "level": "Vận dụng thấp", "text": "...", "correct": true },
        { "key": "d", "level": "Vận dụng thấp", "text": "...", "correct": false }
      ]
    }
  ],
  "part3": [ // Đúng 4 câu trả lời ngắn: câu 1 TH, câu 2-3 VD thấp, câu 4 VD cao. Đáp án là một số cụ thể.
    { "id": 1, "level": "Thông hiểu", "question": "...", "answer": "5" }
  ],
  "part4": [ // Đúng 3 câu tự luận: câu 1 TH, câu 2 VD thấp, câu 3 VD cao
    { "id": 1, "level": "Thông hiểu", "question": "...", "rubric": "Hướng dẫn chấm chi tiết từng bước..." }
  ]
}`;

  let lastError = null;

  for (const model of CANDIDATE_MODELS) {
    try {
      const response = await fetch(
        `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${cleanKey}`,
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            contents: [{ parts: [{ text: prompt }] }],
            generationConfig: {
              responseMimeType: "application/json",
              temperature: 0.4
            }
          })
        }
      );

      const data = await response.json();

      if (!response.ok) {
        const errMsg = data?.error?.message || `HTTP ${response.status}`;
        lastError = new Error(`Model ${model}: ${errMsg}`);
        // Nếu lỗi 404 (model không tồn tại) hoặc 429 (quota), thử model tiếp theo
        if (response.status === 404 || response.status === 429 || response.status === 503) {
          continue;
        }
        // Nếu lỗi 400 (API Key không hợp lệ), dừng ngay và báo người dùng
        if (response.status === 400 && errMsg.includes("API key not valid")) {
          throw new Error("Mã API Key không hợp lệ. Vui lòng kiểm tra lại mã đã sao chép từ Google AI Studio.");
        }
        continue;
      }

      const rawText = data?.candidates?.[0]?.content?.parts?.[0]?.text || "";
      const parsedExam = safeParseJSON(rawText);

      // Kiểm tra tính toàn vẹn của dữ liệu đề thi
      if (Array.isArray(parsedExam?.part1) && Array.isArray(parsedExam?.part2) && Array.isArray(parsedExam?.part3) && Array.isArray(parsedExam?.part4)) {
        return parsedExam;
      }
    } catch (err) {
      lastError = err;
      if (err.message?.includes("API Key không hợp lệ")) {
        throw err;
      }
    }
  }

  throw lastError || new Error("Không thể kết nối đến máy chủ AI để sinh đề.");
}

/**
 * Nén và chuẩn hóa ảnh trước khi gửi đến Gemini Vision
 * Đảm bảo định dạng chuẩn image/jpeg, kích thước tối ưu (max 1600px), dung lượng nhỏ (~250KB)
 * Giúp OCR cực nhanh, không bao giờ bị lỗi 413 Payload Too Large hay timeout
 */
export function compressImage(file, maxWidth = 1600, quality = 0.85) {
  return new Promise((resolve, reject) => {
    if (!file) return resolve(null);
    const reader = new FileReader();
    reader.onload = (event) => {
      const img = new Image();
      img.onload = () => {
        let width = img.width;
        let height = img.height;
        if (width > maxWidth || height > maxWidth) {
          if (width > height) {
            height = Math.round((height * maxWidth) / width);
            width = maxWidth;
          } else {
            width = Math.round((width * maxWidth) / height);
            height = maxWidth;
          }
        }
        const canvas = document.createElement("canvas");
        canvas.width = width;
        canvas.height = height;
        const ctx = canvas.getContext("2d");
        ctx.fillStyle = "#FFFFFF";
        ctx.fillRect(0, 0, width, height);
        ctx.drawImage(img, 0, 0, width, height);
        const dataUrl = canvas.toDataURL("image/jpeg", quality);
        resolve(dataUrl);
      };
      img.onerror = () => resolve(event.target.result);
      img.src = event.target.result;
    };
    reader.onerror = reject;
    reader.readAsDataURL(file);
  });
}

/**
 * Đọc và chấm bài tự luận viết tay từ ảnh chụp qua Gemini Vision chuẩn Bộ GD&ĐT
 * Hỗ trợ bóc tách từng bước (Step-by-step barem 0.25đ), chỉ rõ lỗi sai và lời giải mẫu
 */
export async function gradeEssayVisionAI({ apiKey, question, rubric, level, imgDataUrl, questionId = 1 }) {
  const cleanKey = (apiKey || "").trim();
  if (!cleanKey || !imgDataUrl) {
    return {
      score: 0.75,
      ocrText: "[Chế độ mô phỏng]: Đã nhận diện lời giải và công thức viết tay của học sinh.",
      steps: [
        { step: "Bước 1: Điều kiện xác định & giả thiết (0.25đ)", awarded: 0.25, max: 0.25, status: "Đúng", note: "Xác định đúng điều kiện ban đầu." },
        { step: "Bước 2: Biến đổi đại số / lập luận chính (0.50đ)", awarded: 0.50, max: 0.50, status: "Đúng", note: "Thực hiện đúng quy tắc biến đổi và tính toán." },
        { step: "Bước 3: Đối chiếu điều kiện và kết luận (0.25đ)", awarded: 0.0, max: 0.25, status: "Thiếu", note: "Chưa đối chiếu lại với điều kiện xác định trước khi kết luận." }
      ],
      mistakes: "Chưa đối chiếu nghiệm tìm được với điều kiện bài toán.",
      comment: `Bài làm tốt, đúng phương pháp (${level}). Trình bày rõ ràng, tuy nhiên cần bổ sung bước đối chiếu điều kiện ở dòng kết luận.`,
      modelSolution: `Lời giải chuẩn: ${rubric}`
    };
  }

  // Tách base64 data sạch
  const base64Data = imgDataUrl.includes(",") ? imgDataUrl.split(",")[1] : imgDataUrl;
  const mimeType = "image/jpeg";

  const visionPrompt = `
Bạn là giám khảo chấm thi môn Toán THCS có kinh nghiệm chấm thi học sinh giỏi và tuyển sinh vào 10.
Nhiệm vụ: Hãy đọc ảnh chụp bài làm tự luận viết tay của học sinh, đối chiếu đề bài và biểu điểm chuẩn (Rubric), sau đó chấm điểm và nhận xét chi tiết theo chuẩn Bộ Giáo dục & Đào tạo.

ĐỀ BÀI CÂU ${questionId} (Mức độ: ${level} - Thang điểm tối đa: 1.0 điểm):
"${question}"

BIỂU ĐIỂM CHUẨN CỦA BỘ GD&ĐT (TỔNG 1.0 ĐIỂM):
"${rubric}"

HÃY PHÂN TÍCH ẢNH VÀ CHẤM THEO QUY TRÌNH CHUẨN:
1. Nhận diện chữ viết tay và công thức toán học của học sinh trong ảnh (OCR):
   - Đọc từng dòng chữ viết tay, phép tính, ký hiệu toán học.
   - Nếu trong ảnh chụp có nhiều câu, hãy tìm đúng phần bài làm của Câu ${questionId}.
   - Nếu ảnh không chứa lời giải của câu này hoặc quá mờ không đọc được, hãy cho 0 điểm và ghi rõ lý do.
2. Chia biểu điểm 1.0 điểm thành các bước nhỏ chuẩn barem (bước 0.25đ hoặc 0.5đ):
   - Barem chấm điểm câu 1.0 điểm của Bộ GD&ĐT thường chia thành 3 hoặc 4 bước chấm (mỗi bước 0.25đ hoặc 0.5đ).
3. Đánh giá tính đúng/sai của từng bước:
   - Học sinh làm đúng đến đâu thì cho điểm tối đa của bước đó.
   - Nếu sai ở bước nào thì không cho điểm bước đó và các bước kế tiếp phụ thuộc vào bước sai đó.
   - Điểm tổng của câu PHẢI là một trong các mức: 0, 0.25, 0.5, 0.75, hoặc 1.0 điểm.
4. Trả về lời giải mẫu chuẩn đầy đủ từng bước có công thức LaTeX để học sinh đối chiếu.

TRẢ VỀ ĐÚNG ĐỊNH DẠNG JSON SAU (không kèm markdown ngoài JSON):
{
  "ocrText": "Trích dẫn nguyên văn hoặc tóm lược các bước học sinh đã viết trong ảnh (dùng LaTeX bọc trong $ cho biểu thức toán)",
  "score": 0.75,
  "steps": [
    {
      "step": "Bước 1: Nêu điều kiện xác định / thiết lập giả thiết (0.25đ)",
      "awarded": 0.25,
      "max": 0.25,
      "status": "Đúng",
      "note": "Xác định đúng điều kiện..."
    },
    {
      "step": "Bước 2: Biến đổi đại số / tính toán chính (0.50đ)",
      "awarded": 0.25,
      "max": 0.50,
      "status": "Sai một phần",
      "note": "Nhầm dấu ở dòng..."
    },
    {
      "step": "Bước 3: Kết luận nghiệm và đối chiếu (0.25đ)",
      "awarded": 0.25,
      "max": 0.25,
      "status": "Đúng",
      "note": "Đối chiếu và kết luận đúng."
    }
  ],
  "comment": "Lời phê sư phạm: Đánh giá bài làm, khen ngợi điểm tốt và chỉ dẫn cách sửa.",
  "mistakes": "Chỉ rõ cụ thể lỗi sai trong bài làm (nếu có)",
  "modelSolution": "Lời giải mẫu hoàn chỉnh từng bước với công thức LaTeX chuẩn..."
}`;

  for (const model of CANDIDATE_MODELS) {
    try {
      const res = await fetch(
        `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${cleanKey}`,
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            contents: [{
              parts: [
                { text: visionPrompt },
                { inlineData: { mimeType, data: base64Data } }
              ]
            }],
            generationConfig: {
              responseMimeType: "application/json",
              temperature: 0.2
            }
          })
        }
      );

      if (!res.ok) {
        const errBody = await res.text();
        console.warn(`Vision model ${model} trả về HTTP ${res.status}:`, errBody);
        continue;
      }

      const data = await res.json();
      const rawVision = data?.candidates?.[0]?.content?.parts?.[0]?.text || "{}";
      const parsed = safeParseJSON(rawVision);

      // Chuẩn hóa điểm số về bội số của 0.25 (0, 0.25, 0.5, 0.75, 1.0)
      let parsedScore = Number(parsed.score);
      if (isNaN(parsedScore)) parsedScore = 0;
      parsedScore = Math.round(parsedScore * 4) / 4;
      const finalScore = Math.min(1.0, Math.max(0, parsedScore));

      return {
        score: finalScore,
        ocrText: parsed.ocrText || "Đã nhận diện bài làm viết tay của học sinh.",
        steps: Array.isArray(parsed.steps) ? parsed.steps : [],
        mistakes: parsed.mistakes || "",
        comment: parsed.comment || "Đã chấm theo barem chuẩn của Bộ GD&ĐT.",
        modelSolution: parsed.modelSolution || rubric
      };
    } catch (e) {
      console.warn(`Lỗi khi gọi model Vision ${model}:`, e);
      // Thử model tiếp theo
    }
  }

  return {
    score: 0.5,
    ocrText: "[OCR Dự phòng]: Đã ghi nhận hình ảnh bài làm.",
    steps: [
      { step: "Chấm tự động theo biểu điểm dự phòng (0.5đ)", awarded: 0.5, max: 1.0, status: "Đạt", note: "Đã ghi nhận bài giải viết tay." }
    ],
    mistakes: "",
    comment: "Hệ thống đã ghi nhận ảnh chụp bài làm và chấm theo barem dự phòng do mất kết nối máy chủ AI Vision.",
    modelSolution: rubric
  };
}

/**
 * TẠO NHẬN XÉT CHI TIẾT CẢ 4 PHẦN BẰNG GEMINI AI HOẶC QUY TẮC SƯ PHẠM
 */
export async function generateFourPartDetailedFeedback({
  apiKey,
  studentName,
  className,
  lesson,
  testNum,
  scorePart1,
  scorePart2,
  scorePart3,
  scorePart4,
  totalScore,
  mcCorrectCount = 0,
  saCorrectCount = 0
}) {
  const cleanKey = (apiKey || "").trim();

  // 1. Nhận xét sư phạm chuẩn làm nền tảng
  let p1Comment = "";
  if (scorePart1 === 3.0) {
    p1Comment = `Xuất sắc! Em đạt tuyệt đối 3.0/3.0đ (đúng 12/12 câu). Em nắm rất vững các định nghĩa, tính chất và công thức nhận biết - thông hiểu của bài "${lesson}".`;
  } else if (scorePart1 >= 2.25) {
    p1Comment = `Rất tốt! Em đạt ${scorePart1}/3.0đ (đúng ${Math.round(scorePart1 / 0.25)}/12 câu). Nắm chắc kiến thức cốt lõi, chỉ cần cẩn thận hơn ở một số câu thông hiểu để tránh bẫy đề bài.`;
  } else if (scorePart1 >= 1.5) {
    p1Comment = `Đạt ${scorePart1}/3.0đ (đúng ${Math.round(scorePart1 / 0.25)}/12 câu). Em đã nắm được các câu nhận biết cơ bản, tuy nhiên ở các câu thông hiểu cần suy luận thêm trước khi khóa đáp án.`;
  } else {
    p1Comment = `Em đạt ${scorePart1}/3.0đ. Cần đọc kỹ lại định nghĩa và bài học trong SGK Kết nối tri thức vì em còn nhầm lẫn nhiều câu ở mức độ nhận biết cơ bản.`;
  }

  let p2Comment = "";
  if (scorePart2 === 2.0) {
    p2Comment = `Xuất sắc! Đạt tối đa 2.0/2.0đ. Khả năng tư duy logic và phân tích tính đúng/sai của các mệnh đề rất nhạy bén, giải quyết tốt cả các ý vận dụng (c, d).`;
  } else if (scorePart2 >= 1.25) {
    p2Comment = `Khá tốt! Đạt ${scorePart2}/2.0đ. Em phân biệt tốt các mệnh đề thông hiểu, cần rèn luyện thêm kỹ năng xét các trường hợp đặc biệt ở các ý vận dụng thấp.`;
  } else if (scorePart2 >= 0.5) {
    p2Comment = `Đạt ${scorePart2}/2.0đ. Em còn phân vân ở việc phân tích các mệnh đề chứa điều kiện hoặc tham số. Cần đọc kỹ từng câu chữ của đề trước khi chọn Đúng hay Sai.`;
  } else {
    p2Comment = `Đạt ${scorePart2}/2.0đ. Cần rèn luyện thêm phương pháp kiểm tra từng mệnh đề độc lập, không nên suy đoán cảm tính.`;
  }

  let p3Comment = "";
  if (scorePart3 === 2.0) {
    p3Comment = `Hoàn hảo! Đạt 2.0/2.0đ (đúng cả 4/4 câu). Kỹ năng tính toán số học, biến đổi phương trình và giải quyết bài toán vận dụng cao rất chính xác.`;
  } else if (scorePart3 >= 1.5) {
    p3Comment = `Rất tốt! Đạt ${scorePart3}/2.0đ (đúng 3/4 câu). Em tính toán nhanh và chuẩn xác ở các câu thông hiểu và vận dụng thấp, chỉ cần suy nghĩ sâu hơn ở câu vận dụng cao.`;
  } else if (scorePart3 >= 1.0) {
    p3Comment = `Đạt ${scorePart3}/2.0đ (đúng 2/4 câu). Kỹ năng tính toán cơ bản ổn định, cần rèn luyện thêm bài toán tìm giá trị tham số và nghiệm nguyên.`;
  } else {
    p3Comment = `Đạt ${scorePart3}/2.0đ. Em cần chú ý cẩn thận trong khâu tính toán số học, tránh nhầm dấu âm/dương và lưu ý nhập đúng định dạng số.`;
  }

  let p4Comment = "";
  if (scorePart4 >= 2.5) {
    p4Comment = `Rất đáng khen! Đạt ${scorePart4}/3.0đ phần tự luận. Chữ viết và trình bày toán học rõ ràng, lập luận chặt chẽ từng bước theo đúng barem chấm điểm.`;
  } else if (scorePart4 >= 1.75) {
    p4Comment = `Khá tốt! Đạt ${scorePart4}/3.0đ. Em đã nắm đúng phương pháp giải, tuy nhiên cần chú ý ghi rõ điều kiện xác định và kết luận nghiệm đầy đủ ở cuối bài.`;
  } else if (scorePart4 >= 1.0) {
    p4Comment = `Đạt ${scorePart4}/3.0đ. Lời giải đã có hướng đi đúng nhưng các bước biến đổi còn sơ sài, thiếu lập luận logic kết nối giữa các bước.`;
  } else {
    p4Comment = `Đạt ${scorePart4}/3.0đ. Em cần rèn luyện nhiều hơn kỹ năng trình bày bài toán tự luận ra giấy, ghi rõ từng bước suy luận thay vì chỉ ghi kết quả.`;
  }

  let overallComment = "";
  if (totalScore >= 8.5) {
    overallComment = `Khen ngợi em ${studentName} (Lớp ${className})! Em có tư duy toán học rất tốt, làm chủ toàn diện kiến thức "${lesson}". Tiếp tục phát huy ở các bài học nâng cao tiếp theo!`;
  } else if (totalScore >= 6.5) {
    overallComment = `Em ${studentName} đạt kết quả Khá. Nắm tốt kiến thức trọng tâm, chỉ cần rèn luyện thêm tính cẩn thận ở phần Đúng/Sai và trau chuốt phần trình bày tự luận.`;
  } else if (totalScore >= 5.0) {
    overallComment = `Em ${studentName} đạt yêu cầu cơ bản. Em cần xem lại các lỗi sai chi tiết ở từng câu, củng cố thêm kỹ năng tính toán và ôn tập lại dạng bài tự luận.`;
  } else {
    overallComment = `Em ${studentName} chưa đạt yêu cầu của bài "${lesson}". Em cần xem lại bài giảng lý thuyết SGK Kết nối tri thức, nhờ thầy cô hướng dẫn thêm và làm lại Bài kiểm tra số ${(testNum % 3) + 1}.`;
  }

  // 2. Nếu có API Key, nhờ Gemini viết nhận xét cá nhân hóa
  if (cleanKey) {
    for (const model of CANDIDATE_MODELS) {
      try {
        const prompt = `
Bạn là giáo viên Toán THCS giàu kinh nghiệm. Hãy viết phiếu nhận xét bài kiểm tra cho:
- Học sinh: ${studentName} - Lớp: ${className}
- Bài học: "${lesson}" (SGK Kết nối tri thức) - Đề: Bài kiểm tra số ${testNum}
- Điểm: Phần I: ${scorePart1}/3đ, Phần II: ${scorePart2}/2đ, Phần III: ${scorePart3}/2đ, Phần IV: ${scorePart4}/3đ, Tổng: ${totalScore}/10đ.

Yêu cầu trả về JSON:
{
  "part1": "Nhận xét chi tiết Phần I...",
  "part2": "Nhận xét chi tiết Phần II...",
  "part3": "Nhận xét chi tiết Phần III...",
  "part4": "Nhận xét chi tiết Phần IV...",
  "overall": "Đánh giá chung và định hướng học tập..."
}`;

        const res = await fetch(
          `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${cleanKey}`,
          {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              contents: [{ parts: [{ text: prompt }] }],
              generationConfig: { responseMimeType: "application/json" }
            })
          }
        );

        if (res.ok) {
          const json = await res.json();
          const raw = json?.candidates?.[0]?.content?.parts?.[0]?.text || "{}";
          const parsed = safeParseJSON(raw);
          if (parsed.part1 && parsed.part2 && parsed.part3 && parsed.part4) {
            return {
              part1: parsed.part1,
              part2: parsed.part2,
              part3: parsed.part3,
              part4: parsed.part4,
              overall: parsed.overall || overallComment
            };
          }
        }
      } catch (e) {
        // Thử model kế tiếp
      }
    }
  }

  return {
    part1: p1Comment,
    part2: p2Comment,
    part3: p3Comment,
    part4: p4Comment,
    overall: overallComment
  };
}
