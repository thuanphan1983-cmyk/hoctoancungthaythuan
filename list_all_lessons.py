import sys
import json
sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/generated/khtn_curriculum.json', 'r', encoding='utf-8') as f:
    curr = json.load(f)

for subj, sdata in curr.items():
    print(f"\n=================== {sdata['name']} ===================")
    for g, gdata in sdata['grades'].items():
        print(f"\n--- {gdata['title']} ---")
        for ch in gdata['chapters']:
            print(f"  {ch['title']}:")
            for l in ch['lessons']:
                print(f"    - {l['id']}: {l['name']} (Review: {l['isReview']})")
