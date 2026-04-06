import json, csv, re

# Read data.js and extract the JSON string
with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

json_str = re.sub(r'^const golfData = ', '', content)
json_str = re.sub(r';$', '', json_str.strip())
data = json.loads(json_str)
drivers_orig = data['Drivers']

# Filter out old Srixon and PXG models
remaining_drivers = [d for d in drivers_orig if d['Manufacturer'] not in ['Srixon', 'PXG']]

new_rows = [
    # Srixon
    {'Manufacturer': 'Srixon', 'Release Year': '2026', 'Model Name': 'ZXi', 'Category': 'Versatile Performance', 'CC': '460', 'Standard Loft': '9, 10.5', 'Face Material': 'Ti72S / i-FLEX', 'Adjustability': '+/- 1.5', 'Weight System': 'Heel/Toe Swappable', 'Weight Range': '10g/4g', 'Cost (MSRP)': '$499', 'Stock Length': '45.25"', 'Swing Weight': 'D3', 'Target Player Profile': 'All Skill Levels', 'Spin Profile': 'Mid-Low', 'Bias': 'Neutral', 'Offset': 'None', 'Left Handed': '✓'},
    {'Manufacturer': 'Srixon', 'Release Year': '2026', 'Model Name': 'ZXi LS', 'Category': 'Low Spin', 'CC': '450', 'Standard Loft': '8.5, 9.5, 10.5', 'Face Material': 'Ti72S / i-FLEX', 'Adjustability': '+/- 1.5', 'Weight System': 'Low-Forward Sole', 'Weight Range': 'Adjustable', 'Cost (MSRP)': '$499', 'Stock Length': '45.25"', 'Swing Weight': 'D4', 'Target Player Profile': '0-5 HCP', 'Spin Profile': 'Low', 'Bias': 'Neutral / Fade', 'Offset': 'None', 'Left Handed': '✓'},
    {'Manufacturer': 'Srixon', 'Release Year': '2026', 'Model Name': 'ZXi MAX', 'Category': 'Maximum Forgiveness', 'CC': '460', 'Standard Loft': '9, 10.5, 12', 'Face Material': 'Ti72S / i-FLEX', 'Adjustability': '+/- 1.5', 'Weight System': 'Rear Sole Weight', 'Weight Range': 'Adjustable', 'Cost (MSRP)': '$499', 'Stock Length': '45.25"', 'Swing Weight': 'D2', 'Target Player Profile': '10+ HCP', 'Spin Profile': 'Mid', 'Bias': 'Draw Bias', 'Offset': 'None', 'Left Handed': '✓'},

    # PXG
    {'Manufacturer': 'PXG', 'Release Year': '2026', 'Model Name': 'Lightning Tour', 'Category': 'Low Spin Tour', 'CC': '440', 'Standard Loft': '8, 9, 10', 'Face Material': 'Frequency-Tuned Ti', 'Adjustability': '+/- 1.5', 'Weight System': '3-Port Advanced', 'Weight Range': 'Adjustable', 'Cost (MSRP)': '$649', 'Stock Length': '45.5"', 'Swing Weight': 'D4', 'Target Player Profile': '0-5 HCP', 'Spin Profile': 'Low', 'Bias': 'Fade', 'Offset': 'None', 'Left Handed': '✓'},
    {'Manufacturer': 'PXG', 'Release Year': '2026', 'Model Name': 'Lightning Tour Mid', 'Category': 'Precision / Control', 'CC': '460', 'Standard Loft': '9, 10.5', 'Face Material': 'Frequency-Tuned Ti', 'Adjustability': '+/- 1.5', 'Weight System': '3-Port Advanced', 'Weight Range': 'Adjustable', 'Cost (MSRP)': '$649', 'Stock Length': '45.5"', 'Swing Weight': 'D3', 'Target Player Profile': '0-10 HCP', 'Spin Profile': 'Mid-Low', 'Bias': 'Neutral', 'Offset': 'None', 'Left Handed': '✓'},
    {'Manufacturer': 'PXG', 'Release Year': '2026', 'Model Name': 'Lightning Max 10K+', 'Category': 'Ultra-High MOI', 'CC': '460', 'Standard Loft': '9, 10.5, 12', 'Face Material': 'Frequency-Tuned Ti', 'Adjustability': '+/- 1.5', 'Weight System': 'High MOI 3-Port', 'Weight Range': 'Adjustable', 'Cost (MSRP)': '$599', 'Stock Length': '45.75"', 'Swing Weight': 'D3', 'Target Player Profile': 'All Skill Levels', 'Spin Profile': 'Mid', 'Bias': 'Neutral', 'Offset': 'None', 'Left Handed': '✓'},
    {'Manufacturer': 'PXG', 'Release Year': '2026', 'Model Name': 'Lightning Max Lite', 'Category': 'Lightweight Speed', 'CC': '460', 'Standard Loft': '10.5, 12', 'Face Material': 'Frequency-Tuned Ti', 'Adjustability': '+/- 1.5', 'Weight System': 'Ultralight Sole', 'Weight Range': 'Fixed', 'Cost (MSRP)': '$599', 'Stock Length': '45.75"', 'Swing Weight': 'D0', 'Target Player Profile': '15+ HCP (Slow Swing)', 'Spin Profile': 'Mid-High', 'Bias': 'Draw', 'Offset': 'None', 'Left Handed': '✓'}
]

final_drivers = remaining_drivers + new_rows
final_drivers.sort(key=lambda x: x['Manufacturer'])

data['Drivers'] = final_drivers

# Rewrite Drivers CSV
with open('Data/Golf Comparison - Drivers.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=list(final_drivers[0].keys()))
    writer.writeheader()
    writer.writerows(final_drivers)

# Rewrite data.js
with open('data.js', 'w', encoding='utf-8') as f:
    f.write('const golfData = ' + json.dumps(data, indent=2) + ';')

print("Updated Srixon and PXG in Drivers.csv and data.js successfully.")
