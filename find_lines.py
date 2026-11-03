with open('index.html', 'r', encoding='utf-8') as f:
    for i, l in enumerate(f):
        if 'view === "grade10_topic"' in l or 'view === "periodic_exam"' in l or 'view === "grade10_mock"' in l or 'view === "dashboard"' in l:
            print(f"Line {i+1}: {l.strip()[:70]}")
