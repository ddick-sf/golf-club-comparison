import csv, json

new_fairways = [
    # Callaway
    {'Manufacturer': 'Callaway', 'Year': '2026', 'Model Name': 'Quantum Max Fast', 'Release Year': '2026', 'Category': 'Lightweight Speed', 'CC': '185', 'Standard Loft': '16, 19, 22', 'Face Material': 'Tri-Force Face', 'Adjustability': 'Fixed Hosel', 'Weight System': 'Lightweight', 'Weight Range': 'Fixed', 'Cost (MSRP)': '$349', 'Stock Length': '43.25"', 'Swing Weight': 'D0', 'Target Player Profile': '15+ HCP (Slow Swing)', 'Spin Profile': 'High', 'Bias': 'Draw Bias', 'Offset': 'Slight', 'Left Handed': '✓'},
    {'Manufacturer': 'Callaway', 'Year': '2026', 'Model Name': 'Quantum Triple Diamond Max', 'Release Year': '2026', 'Category': 'Tour Forgiveness', 'CC': '175', 'Standard Loft': '15, 18', 'Face Material': 'Tri-Force Face', 'Adjustability': '+/- 2.0', 'Weight System': 'Front/Back Pods', 'Weight Range': '10g/4g', 'Cost (MSRP)': '$349', 'Stock Length': '43.0"', 'Swing Weight': 'D3', 'Target Player Profile': '0-10 HCP', 'Spin Profile': 'Mid-Low', 'Bias': 'Neutral', 'Offset': 'None', 'Left Handed': 'No'},
    
    # TaylorMade
    {'Manufacturer': 'TaylorMade', 'Year': '2026', 'Model Name': 'Qi4D Max', 'Release Year': '2026', 'Category': 'Max Forgiveness', 'CC': '185', 'Standard Loft': '15, 16.5, 18', 'Face Material': 'C300 Maraging / Titanium', 'Adjustability': 'Fixed', 'Weight System': 'Rear Inertia Generator', 'Weight Range': 'Fixed', 'Cost (MSRP)': '$349', 'Stock Length': '43.25"', 'Swing Weight': 'D2', 'Target Player Profile': '15+ HCP', 'Spin Profile': 'Mid-High', 'Bias': 'Draw Bias', 'Offset': 'Slight', 'Left Handed': '✓'},
    
    # PING
    {'Manufacturer': 'PING', 'Year': '2026', 'Model Name': 'G440 SFT', 'Release Year': '2026', 'Category': 'Straight Flight Tech', 'CC': '176', 'Standard Loft': '16, 19', 'Face Material': 'Maraging Steel', 'Adjustability': '+/- 1.5', 'Weight System': 'Heel Tungsten Weight', 'Weight Range': 'Fixed', 'Cost (MSRP)': '$349', 'Stock Length': '43.0"', 'Swing Weight': 'D1', 'Target Player Profile': '15+ HCP (Slicer)', 'Spin Profile': 'Mid-High', 'Bias': 'Draw Bias', 'Offset': 'Slight', 'Left Handed': '✓'},
    
    # Cobra
    {'Manufacturer': 'Cobra', 'Year': '2026', 'Model Name': 'OPTM Max-K', 'Release Year': '2026', 'Category': 'Max Stability', 'CC': '185', 'Standard Loft': '15.5, 18.5, 21.5', 'Face Material': 'H.O.T. Face Steel', 'Adjustability': '+/- 1.5', 'Weight System': 'Rear Weight', 'Weight Range': 'Fixed', 'Cost (MSRP)': '$329', 'Stock Length': '43.25"', 'Swing Weight': 'D2', 'Target Player Profile': '10+ HCP', 'Spin Profile': 'Mid', 'Bias': 'Neutral / Draw', 'Offset': 'Slight', 'Left Handed': '✓'},
    {'Manufacturer': 'Cobra', 'Year': '2026', 'Model Name': 'OPTM Max-D', 'Release Year': '2026', 'Category': 'Draw Bias', 'CC': '185', 'Standard Loft': '15.5, 18.5', 'Face Material': 'H.O.T. Face Steel', 'Adjustability': '+/- 1.5', 'Weight System': 'Heel Biased', 'Weight Range': 'Fixed', 'Cost (MSRP)': '$329', 'Stock Length': '43.25"', 'Swing Weight': 'D1', 'Target Player Profile': '15+ HCP (Slicer)', 'Spin Profile': 'Mid-High', 'Bias': 'Draw Bias', 'Offset': 'Moderate', 'Left Handed': '✓'},

    # Srixon
    {'Manufacturer': 'Srixon', 'Year': '2026', 'Model Name': 'ZXi', 'Release Year': '2026', 'Category': 'Versatile Performance', 'CC': '175', 'Standard Loft': '13.5, 15, 18', 'Face Material': 'Ti51AF Titanium Face', 'Adjustability': 'Fixed', 'Weight System': 'Step Crown / Cannon Sole', 'Weight Range': 'Fixed', 'Cost (MSRP)': '$329', 'Stock Length': '43.0"', 'Swing Weight': 'D2', 'Target Player Profile': 'All Skill Levels', 'Spin Profile': 'Mid', 'Bias': 'Neutral', 'Offset': 'None', 'Left Handed': '✓'},
    {'Manufacturer': 'Srixon', 'Year': '2026', 'Model Name': 'ZXi LS', 'Release Year': '2026', 'Category': 'Low Spin', 'CC': '170', 'Standard Loft': '14.5, 15', 'Face Material': 'Ti51AF Titanium Face', 'Adjustability': '+/- 1.5', 'Weight System': 'Low Forward Sole', 'Weight Range': 'Adjustable', 'Cost (MSRP)': '$329', 'Stock Length': '43.0"', 'Swing Weight': 'D3', 'Target Player Profile': '0-5 HCP', 'Spin Profile': 'Low', 'Bias': 'Neutral / Fade', 'Offset': 'None', 'Left Handed': '✓'},
    {'Manufacturer': 'Srixon', 'Year': '2026', 'Model Name': 'ZXi MAX', 'Release Year': '2026', 'Category': 'Max Forgiveness', 'CC': '180', 'Standard Loft': '15, 18, 21', 'Face Material': 'Ti51AF / Rebound Frame', 'Adjustability': 'Fixed', 'Weight System': 'Rear Sole Weighting', 'Weight Range': 'Fixed', 'Cost (MSRP)': '$329', 'Stock Length': '43.0"', 'Swing Weight': 'D2', 'Target Player Profile': '15+ HCP', 'Spin Profile': 'Mid-High', 'Bias': 'Draw Bias', 'Offset': 'Slight', 'Left Handed': '✓'},

    # PXG
    {'Manufacturer': 'PXG', 'Year': '2026', 'Model Name': 'Lightning Tour', 'Release Year': '2026', 'Category': 'Tour Player', 'CC': '170', 'Standard Loft': '13.5, 15', 'Face Material': 'High-Yield Steel', 'Adjustability': '+/- 1.5', 'Weight System': '3-Port Adjustability', 'Weight Range': 'Adjustable', 'Cost (MSRP)': '$349', 'Stock Length': '43.0"', 'Swing Weight': 'D3', 'Target Player Profile': '0-5 HCP', 'Spin Profile': 'Low', 'Bias': 'Neutral / Fade', 'Offset': 'None', 'Left Handed': '✓'},
    {'Manufacturer': 'PXG', 'Year': '2026', 'Model Name': 'Lightning Max 10K+', 'Release Year': '2026', 'Category': 'Ultra-High MOI', 'CC': '185', 'Standard Loft': '15, 17, 19, 21', 'Face Material': 'High-Yield Steel', 'Adjustability': '+/- 1.5', 'Weight System': '3-Port Extreme MOI', 'Weight Range': 'Adjustable', 'Cost (MSRP)': '$329', 'Stock Length': '43.25"', 'Swing Weight': 'D2', 'Target Player Profile': 'All Skill Levels', 'Spin Profile': 'Mid', 'Bias': 'Neutral', 'Offset': 'Slight', 'Left Handed': '✓'},

    # Mizuno
    {'Manufacturer': 'Mizuno', 'Year': '2026', 'Model Name': 'ST-G Titanium', 'Release Year': '2026', 'Category': 'Tour Low Spin', 'CC': '170', 'Standard Loft': '15, 18', 'Face Material': 'Forged Ti/CORTECH', 'Adjustability': '+/- 2.0', 'Weight System': 'Moveable Tracks', 'Weight Range': 'Dual 7g Weights', 'Cost (MSRP)': '$349', 'Stock Length': '43.0"', 'Swing Weight': 'D3', 'Target Player Profile': '0-5 HCP', 'Spin Profile': 'Low', 'Bias': 'Adjustable', 'Offset': 'None', 'Left Handed': '✓'},
    {'Manufacturer': 'Mizuno', 'Year': '2026', 'Model Name': 'ST-MAX 230', 'Release Year': '2026', 'Category': 'Game Improv.', 'CC': '185', 'Standard Loft': '15, 18, 21', 'Face Material': 'MAS1C / CORTECH', 'Adjustability': '+/- 2.0', 'Weight System': 'Massive Deep Rear Weight', 'Weight Range': 'Fixed', 'Cost (MSRP)': '$299', 'Stock Length': '43.25"', 'Swing Weight': 'D2', 'Target Player Profile': '10+ HCP', 'Spin Profile': 'Mid-High', 'Bias': 'Draw Bias', 'Offset': 'Slight', 'Left Handed': '✓'},

    # Sub 70
    {'Manufacturer': 'Sub 70', 'Year': '2026', 'Model Name': '859 Pro', 'Release Year': '2026', 'Category': 'Tour Performance', 'CC': '172', 'Standard Loft': '15', 'Face Material': '455 Carpenter Steel', 'Adjustability': 'Fixed', 'Weight System': 'Dual Sole Port', 'Weight Range': 'Adjustable', 'Cost (MSRP)': '$249', 'Stock Length': '43.0"', 'Swing Weight': 'D3', 'Target Player Profile': '0-5 HCP', 'Spin Profile': 'Low', 'Bias': 'Neutral', 'Offset': 'None', 'Left Handed': 'No'},
    {'Manufacturer': 'Sub 70', 'Year': '2026', 'Model Name': 'ProFairway V3', 'Release Year': '2026', 'Category': 'Versatile', 'CC': '175', 'Standard Loft': '15, 16.5, 18', 'Face Material': '455 Carpenter Steel', 'Adjustability': 'Fixed', 'Weight System': 'Variable Weight Port', 'Weight Range': 'Adjustable', 'Cost (MSRP)': '$199', 'Stock Length': '43.25"', 'Swing Weight': 'D2', 'Target Player Profile': 'All Skill Levels', 'Spin Profile': 'Mid', 'Bias': 'Neutral', 'Offset': 'None', 'Left Handed': '✓'}
]


with open('Data/Golf Comparison - Fairway.csv', 'r', encoding='utf-8') as f:
    orig_fw = list(csv.DictReader(f))

# Deduplicate just in case
existing_models = [f"{i['Manufacturer']} {i['Model Name']}" for i in orig_fw]
to_add = [i for i in new_fairways if f"{i['Manufacturer']} {i['Model Name']}" not in existing_models]

final_fw = orig_fw + to_add
final_fw.sort(key=lambda x: x['Manufacturer'])

with open('Data/Golf Comparison - Fairway.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=list(final_fw[0].keys()))
    writer.writeheader()
    writer.writerows(final_fw)

# update JS
with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

import re
json_str = re.sub(r'^const golfData = ', '', content)
json_str = re.sub(r';$', '', json_str.strip())
data = json.loads(json_str)

data['Fairways'] = final_fw

with open('data.js', 'w', encoding='utf-8') as f:
    f.write('const golfData = ' + json.dumps(data, indent=2) + ';')

print("Added massive 2026 Fairway update successfully!")
