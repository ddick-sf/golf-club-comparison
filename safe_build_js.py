import csv, json

data = {}
with open('infrastructure/Data/Golf Comparison - Drivers.csv', 'r', encoding='utf-8') as f:
    data['Drivers'] = list(csv.DictReader(f))

with open('infrastructure/Data/Golf Comparison - Fairway.csv', 'r', encoding='utf-8') as f:
    data['Fairways'] = list(csv.DictReader(f))

with open('infrastructure/Data/Golf Comparison - Irons.csv', 'r', encoding='utf-8') as f:
    data['Irons'] = list(csv.DictReader(f))

with open('infrastructure/Data/Golf Comparison - Wedges.csv', 'r', encoding='utf-8') as f:
    data['Wedges'] = list(csv.DictReader(f))

with open('data.js', 'w', encoding='utf-8') as f:
    f.write('const golfData = ' + json.dumps(data, indent=2) + ';')

print("Safely converted all CSVs to data.js")
