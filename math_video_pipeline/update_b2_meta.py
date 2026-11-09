import re
import os

files = [
    r"C:\Users\May Tinh Chau A\.gemini\antigravity\scratch\toan-thcs-kntt\curriculum.js",
    r"C:\Users\May Tinh Chau A\.gemini\antigravity\scratch\toan-thcs-kntt\public\curriculum.js",
    r"C:\Users\May Tinh Chau A\.gemini\antigravity\scratch\toan-thcs-kntt\index.html"
]

old_pattern = re.compile(r'"videoUrl":\s*"/videos/Toan6_Bai2_HoanChinh\.mp4(\?v=\d+)?"')
new_url = '"videoUrl": "/videos/Toan6_Bai2_HoanChinh.mp4?v=2"'

for path in files:
    if not os.path.exists(path):
        continue
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    content = old_pattern.sub(new_url, content)

    def replace_b2_dur(m):
        block = m.group(0)
        block = re.sub(r'"duration":\s*"[^"]+"', '"duration": "14:27"', block)
        return block

    content = re.sub(r'"Bài 2:[^}]+}', replace_b2_dur, content)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated:", path)
