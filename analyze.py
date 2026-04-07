import json
import re

with open('c:/Users/ddick/Desktop/golf-club-comparison/data.js', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const golfData = ({.*?});', text, re.DOTALL)
if m:
    data = json.loads(m.group(1))
    for category in data:
        items = data[category]
        mizuno_items = [item for item in items if item.get('Manufacturer') == 'Mizuno']
        print(f'{category}: {len(mizuno_items)} Mizuno items out of {len(items)} total')
        if category == 'Drivers' and mizuno_items:
            for d in mizuno_items:
                print(f"  - {d.get('Model Name', 'Unknown')} ({d.get('Release Year','?')})")
