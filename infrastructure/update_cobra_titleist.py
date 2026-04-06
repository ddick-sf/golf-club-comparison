import json, csv, re

# Read data.js and extract the JSON string
with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

json_str = re.sub(r'^const golfData = ', '', content)
json_str = re.sub(r';$', '', json_str.strip())
data = json.loads(json_str)
drivers_orig = data['Drivers']

# Filter out old Cobra and Titleist models
remaining_drivers = [d for d in drivers_orig if d['Manufacturer'] not in ['Cobra', 'Titleist']]

new_rows = [
    # Cobra
    {'Manufacturer': 'Cobra', 'Release Year': '2026', 'Model Name': 'OPTM X', 'Category': 'Versatile Forgiveness', 'CC': '460', 'Standard Loft': '9, 10.5, 12', 'Face Material': 'H.O.T. Face Insert', 'Adjustability': '+/- 1.5', 'Weight System': 'Mid-high toe & back', 'Weight Range': 'Adjustable', 'Cost (MSRP)': '$549', 'Stock Length': '45.5"', 'Swing Weight': 'D3', 'Target Player Profile': 'All Skill Levels', 'Spin Profile': 'Mid', 'Bias': 'Neutral', 'Offset': 'None', 'Left Handed': '✓'},
    {'Manufacturer': 'Cobra', 'Release Year': '2026', 'Model Name': 'OPTM LS', 'Category': 'Low Spin Tour', 'CC': '460', 'Standard Loft': '8, 9, 10.5', 'Face Material': 'H.O.T. Face Insert', 'Adjustability': '+/- 1.5', 'Weight System': '3-Port (Toe, Heel, Back)', 'Weight Range': 'Adjustable', 'Cost (MSRP)': '$549', 'Stock Length': '45.5"', 'Swing Weight': 'D4', 'Target Player Profile': '0-5 HCP', 'Spin Profile': 'Very Low', 'Bias': 'Fade Bias', 'Offset': 'None', 'Left Handed': '✓'},
    {'Manufacturer': 'Cobra', 'Release Year': '2026', 'Model Name': 'OPTM Max-K', 'Category': 'Max Stability (High MOI)', 'CC': '460', 'Standard Loft': '9, 10.5, 12', 'Face Material': 'H.O.T. Face Insert', 'Adjustability': '+/- 1.5', 'Weight System': '11g Rear Weight', 'Weight Range': 'Fixed', 'Cost (MSRP)': '$549', 'Stock Length': '45.75"', 'Swing Weight': 'D2', 'Target Player Profile': '10+ HCP', 'Spin Profile': 'Mid-High', 'Bias': 'Neutral / Draw', 'Offset': 'Slight', 'Left Handed': '✓'},
    {'Manufacturer': 'Cobra', 'Release Year': '2026', 'Model Name': 'OPTM Max-D', 'Category': 'Draw Bias', 'CC': '460', 'Standard Loft': '9, 10.5, 12', 'Face Material': 'H.O.T. Face Insert', 'Adjustability': '+/- 1.5', 'Weight System': 'Heel Biased', 'Weight Range': 'Fixed', 'Cost (MSRP)': '$549', 'Stock Length': '45.75"', 'Swing Weight': 'D2', 'Target Player Profile': '15+ HCP (Slicer)', 'Spin Profile': 'Mid-High', 'Bias': 'Draw Bias', 'Offset': 'Moderate', 'Left Handed': '✓'},

    # Titleist
    {'Manufacturer': 'Titleist', 'Release Year': '2024/2026', 'Model Name': 'GT2', 'Category': 'Maximum Forgiveness', 'CC': '460', 'Standard Loft': '8, 9, 10.5, 11.5', 'Face Material': 'Proprietary Matrix Polymer', 'Adjustability': '+/- 1.5', 'Weight System': 'Rear Weight (High MOI)', 'Weight Range': 'Interchangeable', 'Cost (MSRP)': '$649', 'Stock Length': '45.5"', 'Swing Weight': 'D3', 'Target Player Profile': 'All Skill Levels', 'Spin Profile': 'Mid', 'Bias': 'Neutral', 'Offset': 'None', 'Left Handed': '✓'},
    {'Manufacturer': 'Titleist', 'Release Year': '2024/2026', 'Model Name': 'GT3', 'Category': 'Precision and Control', 'CC': '460', 'Standard Loft': '8, 9, 10.5, 11.5', 'Face Material': 'Proprietary Matrix Polymer', 'Adjustability': '+/- 1.5', 'Weight System': 'Front Sliding Track', 'Weight Range': 'Adjustable', 'Cost (MSRP)': '$649', 'Stock Length': '45.5"', 'Swing Weight': 'D3', 'Target Player Profile': '0-10 HCP', 'Spin Profile': 'Low', 'Bias': 'Adjustable', 'Offset': 'None', 'Left Handed': '✓'},
    {'Manufacturer': 'Titleist', 'Release Year': '2024/2026', 'Model Name': 'GT4', 'Category': 'Maximum Spin Reduction', 'CC': '430', 'Standard Loft': '8, 9, 10', 'Face Material': 'Proprietary Matrix Polymer', 'Adjustability': '+/- 1.5', 'Weight System': 'Dual (Front/Back)', 'Weight Range': '11g & 3g', 'Cost (MSRP)': '$649', 'Stock Length': '45.5"', 'Swing Weight': 'D4', 'Target Player Profile': '0-5 HCP (High Speed)', 'Spin Profile': 'Lowest', 'Bias': 'Neutral', 'Offset': 'None', 'Left Handed': '✓'}
]

final_drivers = remaining_drivers + new_rows
# Optionally, sort by manufacturer to keep things neat
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

print("Updated Cobra and Titleist in Drivers.csv and data.js successfully.")
