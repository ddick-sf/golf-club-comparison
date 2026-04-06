import csv, json

new_irons = [
    # Cobra
    {'Manufacturer': 'Cobra', 'Year': '2026', 'Model': 'KING Tour', 'Category': 'Tour Player', 'Head Material (Body/Face)': 'Forged 1025 Carbon Steel', 'Loft Array (4-PW)': '24/27/30/34/38/42/46', '7i Loft / Lie': '34.0° / 62.5°', 'Topline / Blade (7i)': '5.0mm / 75mm', 'Finish Options': 'Satin Chrome', 'Price (7pc)': '$1,300', 'Stock Length': '37.0" (7i)', 'Swing Weight': 'D2', 'Target Player Profile': '0-5 HCP', 'Spin Profile': 'High', 'Bias': 'Neutral', 'Offset': 'Minimal (1.5mm)', 'Left Handed': '✓'},
    {'Manufacturer': 'Cobra', 'Year': '2026', 'Model': 'OPTM Forged Tec', 'Category': 'Players Distance', 'Head Material (Body/Face)': 'Forged 1025 / PWRSHELL', 'Loft Array (4-PW)': '21/23/26/29.5/34/39/44', '7i Loft / Lie': '29.5° / 62.5°', 'Topline / Blade (7i)': '7.0mm / 78mm', 'Finish Options': 'Chrome', 'Price (7pc)': '$1,300', 'Stock Length': '37.0" (7i)', 'Swing Weight': 'D2', 'Target Player Profile': '5-15 HCP', 'Spin Profile': 'Low-Mid', 'Bias': 'Neutral', 'Offset': 'Slight (2.3mm)', 'Left Handed': '✓'},
    
    # Srixon
    {'Manufacturer': 'Srixon', 'Year': '2026', 'Model': 'ZXi7', 'Category': 'Tour Cavity', 'Head Material (Body/Face)': 'Forged 1020 Carbon', 'Loft Array (4-PW)': '23/26/29/33/37/41/46', '7i Loft / Lie': '33.0° / 62.0°', 'Topline / Blade (7i)': '5.5mm / 76mm', 'Finish Options': 'Tour Satin', 'Price (7pc)': '$1,200', 'Stock Length': '37.0" (7i)', 'Swing Weight': 'D3', 'Target Player Profile': '0-5 HCP', 'Spin Profile': 'High', 'Bias': 'Neutral', 'Offset': 'Minimal (2.0mm)', 'Left Handed': '✓'},
    {'Manufacturer': 'Srixon', 'Year': '2026', 'Model': 'ZXi5', 'Category': 'Players Distance', 'Head Material (Body/Face)': 'Forged Carbon / SUP10 Face', 'Loft Array (4-PW)': '22/24/27/31/35/39/44', '7i Loft / Lie': '31.0° / 62.0°', 'Topline / Blade (7i)': '7.0mm / 79mm', 'Finish Options': 'Tour Satin', 'Price (7pc)': '$1,200', 'Stock Length': '37.0" (7i)', 'Swing Weight': 'D2', 'Target Player Profile': '5-15 HCP', 'Spin Profile': 'Mid', 'Bias': 'Neutral', 'Offset': 'Slight (2.8mm)', 'Left Handed': '✓'},

    # PXG
    {'Manufacturer': 'PXG', 'Year': '2026', 'Model': '0311 P Gen7', 'Category': 'Players Distance', 'Head Material (Body/Face)': 'Forged 8620 / HT1770 Face', 'Loft Array (4-PW)': '21/24/27/30/34/39/44', '7i Loft / Lie': '30.0° / 62.5°', 'Topline / Blade (7i)': '6.5mm / 78mm', 'Finish Options': 'Xtreme Dark / Chrome', 'Price (7pc)': '$1,399', 'Stock Length': '37.0" (7i)', 'Swing Weight': 'D2', 'Target Player Profile': '0-10 HCP', 'Spin Profile': 'Mid', 'Bias': 'Neutral', 'Offset': 'Slight (2.5mm)', 'Left Handed': '✓'},

    # Wilson
    {'Manufacturer': 'Wilson', 'Year': '2026', 'Model': 'Staff Model Blades', 'Category': 'Tour Blade', 'Head Material (Body/Face)': 'Forged 8620 Carbon Steel', 'Loft Array (4-PW)': '25/28/31/35/39/43/47', '7i Loft / Lie': '35.0° / 62.0°', 'Topline / Blade (7i)': '4.5mm / 72mm', 'Finish Options': 'Satin', 'Price (7pc)': '$1,199', 'Stock Length': '37.0" (7i)', 'Swing Weight': 'D3', 'Target Player Profile': '0-3 HCP', 'Spin Profile': 'High', 'Bias': 'Neutral', 'Offset': 'Minimal (1.2mm)', 'Left Handed': '✓'},
    {'Manufacturer': 'Wilson', 'Year': '2026', 'Model': 'Dynapower Forged', 'Category': 'Players Distance', 'Head Material (Body/Face)': 'Forged 8620 Face', 'Loft Array (4-PW)': '21.5/24/27/30.5/35/40/45', '7i Loft / Lie': '30.5° / 62.0°', 'Topline / Blade (7i)': '7.0mm / 78mm', 'Finish Options': 'Chrome', 'Price (7pc)': '$999', 'Stock Length': '37.0" (7i)', 'Swing Weight': 'D2', 'Target Player Profile': '5-15 HCP', 'Spin Profile': 'Mid', 'Bias': 'Neutral', 'Offset': 'Slight (2.7mm)', 'Left Handed': 'No'},

    # Takomo
    {'Manufacturer': 'Takomo', 'Year': '2026', 'Model': '101', 'Category': 'Game Improv.', 'Head Material (Body/Face)': '431 Stainless Hollow', 'Loft Array (4-PW)': '20/22.5/25.5/29/33/38/43', '7i Loft / Lie': '29.0° / 62.0°', 'Topline / Blade (7i)': '8.0mm / 81mm', 'Finish Options': 'Satin Chrome', 'Price (7pc)': '$489', 'Stock Length': '37.0" (7i)', 'Swing Weight': 'D2', 'Target Player Profile': '10+ HCP', 'Spin Profile': 'Low-Mid', 'Bias': 'Neutral / Draw', 'Offset': 'Moderate (4.0mm)', 'Left Handed': '✓'},
    {'Manufacturer': 'Takomo', 'Year': '2026', 'Model': '201', 'Category': 'Players Cavity', 'Head Material (Body/Face)': 'Forged S20C Carbon', 'Loft Array (4-PW)': '22/25/28/31/35/40/45', '7i Loft / Lie': '31.0° / 62.5°', 'Topline / Blade (7i)': '6.0mm / 75mm', 'Finish Options': 'Satin Chrome', 'Price (7pc)': '$589', 'Stock Length': '37.0" (7i)', 'Swing Weight': 'D2', 'Target Player Profile': '0-10 HCP', 'Spin Profile': 'Mid', 'Bias': 'Neutral', 'Offset': 'Minimal (2.0mm)', 'Left Handed': '✓'},
    {'Manufacturer': 'Takomo', 'Year': '2026', 'Model': '301 CB', 'Category': 'Tour Player', 'Head Material (Body/Face)': 'Forged S20C Carbon', 'Loft Array (4-PW)': '24/27/30/34/38/42/46', '7i Loft / Lie': '34.0° / 62.5°', 'Topline / Blade (7i)': '4.8mm / 73mm', 'Finish Options': 'Satin Chrome', 'Price (7pc)': '$649', 'Stock Length': '37.0" (7i)', 'Swing Weight': 'D3', 'Target Player Profile': '0-5 HCP', 'Spin Profile': 'High', 'Bias': 'Neutral', 'Offset': 'Minimal (1.5mm)', 'Left Handed': '✓'},

    # Sub 70
    {'Manufacturer': 'Sub 70', 'Year': '2026', 'Model': '699 Pro V2', 'Category': 'Players Distance', 'Head Material (Body/Face)': '431 Stainless Hollow / TPE', 'Loft Array (4-PW)': '21/24/27/31/35/40/45', '7i Loft / Lie': '31.0° / 62.0°', 'Topline / Blade (7i)': '6.8mm / 77mm', 'Finish Options': 'Satin / Black DLC', 'Price (7pc)': '$599', 'Stock Length': '37.0" (7i)', 'Swing Weight': 'D2', 'Target Player Profile': '0-15 HCP', 'Spin Profile': 'Mid', 'Bias': 'Neutral', 'Offset': 'Slight (2.2mm)', 'Left Handed': '✓'},
    {'Manufacturer': 'Sub 70', 'Year': '2026', 'Model': 'TAIII Forged', 'Category': 'Tour Blade', 'Head Material (Body/Face)': 'Forged DT-4 Steel', 'Loft Array (4-PW)': '24/27/30/34/38/42/46', '7i Loft / Lie': '34.0° / 62.0°', 'Topline / Blade (7i)': '4.5mm / 72mm', 'Finish Options': 'Raw / Satin', 'Price (7pc)': '$750', 'Stock Length': '37.0" (7i)', 'Swing Weight': 'D3', 'Target Player Profile': '0-3 HCP', 'Spin Profile': 'High', 'Bias': 'Neutral', 'Offset': 'Minimal (1.2mm)', 'Left Handed': '✓'},

    # Mizuno additions
    {'Manufacturer': 'Mizuno', 'Year': '2026', 'Model': 'Pro 263', 'Category': 'Players Cavity', 'Head Material (Body/Face)': '1025E / 4120 Chromoly', 'Loft Array (4-PW)': '22/25/28/32/36/40/44', '7i Loft / Lie': '32.0° / 61.5°', 'Topline / Blade (7i)': '5.5mm / 75mm', 'Finish Options': 'Satin Chrome', 'Price (7pc)': '$1,505', 'Stock Length': '37.0" (7i)', 'Swing Weight': 'D2', 'Target Player Profile': '0-8 HCP', 'Spin Profile': 'Mid-High', 'Bias': 'Neutral', 'Offset': 'Minimal (1.8mm)', 'Left Handed': '✓'},
    {'Manufacturer': 'Mizuno', 'Year': '2026', 'Model': 'Pro 265', 'Category': 'Players Distance', 'Head Material (Body/Face)': '4135 Chromoly / Hollow', 'Loft Array (4-PW)': '21.5/24/27/30/34/39/44', '7i Loft / Lie': '30.0° / 61.5°', 'Topline / Blade (7i)': '6.5mm / 78mm', 'Finish Options': 'Satin Chrome', 'Price (7pc)': '$1,505', 'Stock Length': '37.0" (7i)', 'Swing Weight': 'D2', 'Target Player Profile': '5-15 HCP', 'Spin Profile': 'Mid', 'Bias': 'Neutral', 'Offset': 'Slight (2.5mm)', 'Left Handed': '✓'},

    # TaylorMade additions
    {'Manufacturer': 'TaylorMade', 'Year': '2026', 'Model': 'P·7CB', 'Category': 'Tour Cavity', 'Head Material (Body/Face)': 'Compact Forged 1025', 'Loft Array (4-PW)': '24/27/30/34/38/42/46', '7i Loft / Lie': '34.0° / 62.5°', 'Topline / Blade (7i)': '5.5mm / 74mm', 'Finish Options': 'Satin Chrome', 'Price (7pc)': '$1,399', 'Stock Length': '37.0" (7i)', 'Swing Weight': 'D3', 'Target Player Profile': '0-3 HCP', 'Spin Profile': 'High', 'Bias': 'Fade Bias', 'Offset': 'Minimal (1.5mm)', 'Left Handed': '✓'},
    
    # Callaway additions
    {'Manufacturer': 'Callaway', 'Year': '2026', 'Model': 'Apex Ai300', 'Category': 'Game Improv.', 'Head Material (Body/Face)': 'Forged Hollow / AI Face', 'Loft Array (4-PW)': '19/21.5/24/28/32/37/42', '7i Loft / Lie': '28.0° / 62.0°', 'Topline / Blade (7i)': '8.5mm / 81mm', 'Finish Options': 'Satin/Chrome', 'Price (7pc)': '$1,450', 'Stock Length': '37.0" (7i)', 'Swing Weight': 'D1', 'Target Player Profile': '15+ HCP', 'Spin Profile': 'Low', 'Bias': 'Draw Bias', 'Offset': 'Moderate (4.0mm)', 'Left Handed': '✓'},

    # PING additions
    {'Manufacturer': 'PING', 'Year': '2026', 'Model': 'G440 Irons', 'Category': 'Game Improv.', 'Head Material (Body/Face)': '17-4 Stainless Steel / VFT', 'Loft Array (4-PW)': '20/23/26/29.5/34/39/44', '7i Loft / Lie': '29.5° / 62.0°', 'Topline / Blade (7i)': '8.0mm / 82mm', 'Finish Options': 'Hydropearl 2.0', 'Price (7pc)': '$1,100', 'Stock Length': '37.0" (7i)', 'Swing Weight': 'D1', 'Target Player Profile': '10+ HCP', 'Spin Profile': 'Low-Mid', 'Bias': 'Neutral / Draw', 'Offset': 'Moderate (4.5mm)', 'Left Handed': '✓'}
]

with open('Data/Golf Comparison - Irons.csv', 'r', encoding='utf-8') as f:
    orig_irons = list(csv.DictReader(f))

# Deduplicate just in case
existing_models = [f"{i['Manufacturer']} {i['Model']}" for i in orig_irons]
to_add = [i for i in new_irons if f"{i['Manufacturer']} {i['Model']}" not in existing_models]

final_irons = orig_irons + to_add
final_irons.sort(key=lambda x: x['Manufacturer'])

with open('Data/Golf Comparison - Irons.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=list(final_irons[0].keys()))
    writer.writeheader()
    writer.writerows(final_irons)

# update JS
with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

import re
json_str = re.sub(r'^const golfData = ', '', content)
json_str = re.sub(r';$', '', json_str.strip())
data = json.loads(json_str)

data['Irons'] = final_irons

with open('data.js', 'w', encoding='utf-8') as f:
    f.write('const golfData = ' + json.dumps(data, indent=2) + ';')

print("Added more 2026 Irons (incl Cobra, DTC, etc.) successfully!")
