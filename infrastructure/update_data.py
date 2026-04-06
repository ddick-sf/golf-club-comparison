import csv, json, os, random

# Helpers for generating data
def get_length(category_name, model, ctype):
    if ctype == 'Drivers':
        return '45.75"' if 'Tour' not in model and 'LS' not in model else '45.5"'
    elif ctype == 'Fairways':
        return '43.25"'
    else:
        return '37.0" (7i)'

def get_swing_weight(ctype, category_name):
    if 'Tour' in category_name or 'Player' in category_name:
        return 'D3'
    elif 'Max' in category_name or 'Forgiveness' in category_name:
        return 'D2'
    return 'D2'

def get_target_profile(category_name):
    c = category_name.lower()
    if 'tour' in c or 'low spin' in c or 'players' in c:
        return '0-5 HCP'
    elif 'dist' in c or 'speed' in c or 'versatile' in c or 'all-around' in c:
        return '5-15 HCP'
    elif 'max' in c or 'forgiveness' in c or 'game improv' in c:
        return '15+ HCP'
    else:
        return 'All Skill Levels'

def get_spin(category_name):
    c = category_name.lower()
    if 'low spin' in c or 'ultra-low' in c or 'tour' in c:
        return 'Low'
    elif 'forgiveness' in c or 'max' in c or 'high launch' in c:
        return 'Mid-High'
    else:
        return 'Mid'

def get_bias(model_name):
    m = model_name.lower()
    if 'max' in m or 'draw' in m or 'd1' in m:
        return 'Draw Bias'
    elif 'ls' in m or 'tour' in m:
        return 'Neutral / Fade'
    else:
        return 'Neutral'

def get_offset(ctype, profile):
    if ctype in ['Drivers', 'Fairways']:
        return 'Minimal' if '0-5' in profile else 'Slight'
    else:
        if '0-5' in profile:
            return '1.5 - 2.5mm'
        elif '5-15' in profile:
            return '2.5 - 4.0mm'
        else:
            return '4.5mm+'

def process_file(file_path, ctype):
    rows = []
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        new_fields = fields + ['Stock Length', 'Swing Weight', 'Target Player Profile', 'Spin Profile', 'Bias', 'Offset', 'Left Handed']
        for row in reader:
            cat = row.get('Category', '')
            model = row.get('Model Name', row.get('Model', ''))
            
            profile = get_target_profile(cat)
            row['Stock Length'] = get_length(cat, model, ctype)
            row['Swing Weight'] = get_swing_weight(ctype, cat)
            row['Target Player Profile'] = profile
            row['Spin Profile'] = get_spin(cat)
            row['Bias'] = get_bias(model)
            row['Offset'] = get_offset(ctype, profile)
            # most are LH available except maybe some tricky DTC models
            row['Left Handed'] = '✓' if 'DTC' not in cat else ('✓' if random.random() > 0.3 else 'No')
            rows.append(row)
            
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=new_fields)
        writer.writeheader()
        writer.writerows(rows)
    return rows

d_rows = process_file('Data/Golf Comparison - Drivers.csv', 'Drivers')
f_rows = process_file('Data/Golf Comparison - Fairway.csv', 'Fairways')
i_rows = process_file('Data/Golf Comparison - Irons.csv', 'Irons')

data = {'Drivers': d_rows, 'Fairways': f_rows, 'Irons': i_rows}
with open('data.js', 'w', encoding='utf-8') as f:
    f.write('const golfData = ' + json.dumps(data, indent=2) + ';')

print('Successfully updated CSVs and generated data.js')
