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



// 2b. Sao chép các ngân hàng đề thi tĩnh vào dist/

const examFiles = [
  'chapter1Toan8Exams.js',
  'chapter2Toan8Exams.js',
  'chapter3Toan8Exams.js',
  'chapter4Toan8Exams.js',
  'chapter6Toan8Exams.js',
  'chapter1Toan6Exams.js',
  'chapter2Toan6Exams.js',
  'chapter3Toan6Exams.js',
  'chapter4Toan6Exams.js',
  'chapter1Toan7Exams.js',
  'chapter2Toan7Exams.js',
  'chapter3Toan7Exams.js',
  'chapter4Toan7Exams.js',
  'chapter1Toan9Exams.js',
  'chapter2Toan9Exams.js',
  'chapter3Toan9Exams.js',
  'chapter4Toan9Exams.js',
  'chapter3_bai10_toan8.js',
  'chapter3_bai11_toan8.js',
  'chapter3_bai12_toan8.js',
  'chapter3_bai13_toan8.js',
  'chapter3_bai14_toan8.js',
  'chapter3_ontap_toan8.js'
];

examFiles.forEach(fileName => {

  const filePath = path.join(__dirname, fileName);

  if (fs.existsSync(filePath)) {

    fs.copyFileSync(filePath, path.join(distDir, fileName));

    console.log(`✅ Đã xuất bản ${fileName} sang dist/${fileName}`);

  }

});



// 2c. Sao chép thư mục dữ liệu đã sinh src/data/generated sang dist/

const genDir = path.join(__dirname, 'src', 'data', 'generated');

if (fs.existsSync(genDir)) {

  const distGenDir = path.join(distDir, 'generated');

  fs.cpSync(genDir, distGenDir, { recursive: true });

  const distSrcGenDir = path.join(distDir, 'src', 'data', 'generated');

  fs.mkdirSync(path.dirname(distSrcGenDir), { recursive: true });

  fs.cpSync(genDir, distSrcGenDir, { recursive: true });

  console.log('✅ Đã xuất bản toàn bộ đề sinh tự động sang dist/generated/ và dist/src/data/generated/');

}

// 2d. Sao chép manifest.json sang dist/manifest.json
const mfSrc = path.join(__dirname, 'src', 'data', 'generated', 'manifest.json');
if (fs.existsSync(mfSrc)) {
  fs.copyFileSync(mfSrc, path.join(distDir, 'manifest.json'));
  console.log('✅ Đã xuất bản manifest.json sang dist/manifest.json');
}



// 3. Sao chép thư mục public/ (nếu có)

const publicDir = path.join(__dirname, 'public');

if (fs.existsSync(publicDir)) {

  fs.cpSync(publicDir, distDir, { recursive: true });

  console.log('✅ Đã sao chép toàn bộ thư mục public/ sang dist/');

}



console.log('🎉 Bản build đã sẵn sàng xuất sắc cho Vercel / GitHub Pages!');

