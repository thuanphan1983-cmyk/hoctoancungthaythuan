// ==============================================================================
// BUILD SCRIPT CHO VERCEL & GITHUB DEPLOYMENT
// Tự động chuẩn bị thư mục dist/ với đầy đủ index.html, dữ liệu và tài nguyên
// ==============================================================================

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const distDir = path.join(__dirname, 'dist');
if (!fs.existsSync(distDir)) {
  fs.mkdirSync(distDir, { recursive: true });
}

// 1. Sao chép index.html vào dist/
const indexPath = path.join(__dirname, 'index.html');
if (fs.existsSync(indexPath)) {
  fs.copyFileSync(indexPath, path.join(distDir, 'index.html'));
  console.log('✅ Đã xuất bản index.html sang dist/index.html');
}

// 2. Sao chép curriculum.js vào dist/
const currPath = path.join(__dirname, 'curriculum.js');
if (fs.existsSync(currPath)) {
  fs.copyFileSync(currPath, path.join(distDir, 'curriculum.js'));
  console.log('✅ Đã xuất bản curriculum.js sang dist/curriculum.js');
}

// 2b. Sao chép chapter1Toan8Exams.js vào dist/
const c1Path = path.join(__dirname, 'chapter1Toan8Exams.js');
if (fs.existsSync(c1Path)) {
  fs.copyFileSync(c1Path, path.join(distDir, 'chapter1Toan8Exams.js'));
  console.log('✅ Đã xuất bản chapter1Toan8Exams.js sang dist/chapter1Toan8Exams.js');
}

// 2c. Sao chép thư mục dữ liệu đã sinh src/data/generated sang dist/generated (nếu có)
const genDir = path.join(__dirname, 'src', 'data', 'generated');
if (fs.existsSync(genDir)) {
  const distGenDir = path.join(distDir, 'generated');
  fs.cpSync(genDir, distGenDir, { recursive: true });
  console.log('✅ Đã xuất bản toàn bộ đề sinh tự động sang dist/generated/');
}

// 3. Sao chép thư mục public/ (nếu có)
const publicDir = path.join(__dirname, 'public');
if (fs.existsSync(publicDir)) {
  fs.cpSync(publicDir, distDir, { recursive: true });
  console.log('✅ Đã sao chép toàn bộ thư mục public/ sang dist/');
}

console.log('🎉 Bản build đã sẵn sàng xuất sắc cho Vercel / GitHub Pages!');
