import json, csv, re

# Read data.js and extract the JSON string
with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the 'const golfData = ' prefix and ';' suffix
json_str = re.sub(r'^const golfData = ', '', content)
json_str = re.sub(r';$', '', json_str.strip())

data = json.loads(json_str)
drivers_orig = data['Drivers']

# Filter out old models
remaining_drivers = [d for d in drivers_orig if d['Manufacturer'] not in ['TaylorMade', 'Callaway', 'PING']]

new_rows = [
    # TaylorMade
    {'Manufacturer': 'TaylorMade', 'Release Year': '2026', 'Model Name': 'Qi4D Driver', 'Category': 'Versatile', 'CC': '460', 'Standard Loft': '9, 10.5, 12', 'Face Material': '60x Carbon Twist', 'Adjustability': '+/- 2.0', 'Weight System': '4-Port TAS', 'Weight Range': '26g', 'Cost (MSRP)': '$629', 'Stock Length': '45.75"', 'Swing Weight': 'D3', 'Target Player Profile': '5-15 HCP', 'Spin Profile': 'Mid', 'Bias': 'Neutral', 'Offset': 'None', 'Left Handed': '✓'},
    {'Manufacturer': 'TaylorMade', 'Release Year': '2026', 'Model Name': 'Qi4D LS', 'Category': 'Low Spin', 'CC': '460', 'Standard Loft': '8, 9, 10.5', 'Face Material': '60x Carbon Twist', 'Adjustability': '+/- 2.0', 'Weight System': '2-Port TAS', 'Weight Range': '19g', 'Cost (MSRP)': '$649', 'Stock Length': '45.5"', 'Swing Weight': 'D4', 'Target Player Profile': '0-5 HCP', 'Spin Profile': 'Low', 'Bias': 'Fade', 'Offset': 'None', 'Left Handed': '✓'},
    {'Manufacturer': 'TaylorMade', 'Release Year': '2026', 'Model Name': 'Qi4D Max', 'Category': 'Max Forgiveness', 'CC': '460', 'Standard Loft': '9, 10.5, 12', 'Face Material': '60x Carbon Twist', 'Adjustability': '+/- 2.0', 'Weight System': '2-Port System', 'Weight Range': 'Fixed', 'Cost (MSRP)': '$599', 'Stock Length': '45.75"', 'Swing Weight': 'D4', 'Target Player Profile': '15+ HCP', 'Spin Profile': 'Mid-High', 'Bias': 'Draw Bias', 'Offset': 'None', 'Left Handed': '✓'},
    {'Manufacturer': 'TaylorMade', 'Release Year': '2026', 'Model Name': 'Qi4D Max Lite', 'Category': 'Max Speed / Lightweight', 'CC': '460', 'Standard Loft': '10.5, 12', 'Face Material': '60x Carbon Twist', 'Adjustability': '+/- 2.0', 'Weight System': 'Lightweight', 'Weight Range': 'Fixed', 'Cost (MSRP)': '$599', 'Stock Length': '45.75"', 'Swing Weight': 'D1', 'Target Player Profile': '15+ HCP (Slow Swing)', 'Spin Profile': 'High', 'Bias': 'Draw Bias', 'Offset': 'None', 'Left Handed': '✓'},

    # Callaway
    {'Manufacturer': 'Callaway', 'Release Year': '2026', 'Model Name': 'Quantum Max', 'Category': 'Versatile Forgiveness', 'CC': '460', 'Standard Loft': '9, 10.5, 12', 'Face Material': 'Tri-Force Face', 'Adjustability': '+/- 2.0', 'Weight System': 'Sliding Track', 'Weight Range': '12g', 'Cost (MSRP)': '$649', 'Stock Length': '45.75"', 'Swing Weight': 'D3', 'Target Player Profile': 'All Skill Levels', 'Spin Profile': 'Mid', 'Bias': 'Neutral', 'Offset': 'None', 'Left Handed': '✓'},
    {'Manufacturer': 'Callaway', 'Release Year': '2026', 'Model Name': 'Quantum Max D', 'Category': 'Draw Bias', 'CC': '460', 'Standard Loft': '9, 10.5, 12', 'Face Material': 'Tri-Force Face', 'Adjustability': '+/- 2.0', 'Weight System': 'Heel Weight', 'Weight Range': 'Fixed', 'Cost (MSRP)': '$649', 'Stock Length': '45.75"', 'Swing Weight': 'D3', 'Target Player Profile': '15+ HCP', 'Spin Profile': 'Mid-High', 'Bias': 'Draw Bias', 'Offset': 'Slight', 'Left Handed': '✓'},
    {'Manufacturer': 'Callaway', 'Release Year': '2026', 'Model Name': 'Quantum Max Fast', 'Category': 'Lightweight', 'CC': '460', 'Standard Loft': '10.5, 12', 'Face Material': 'Tri-Force Face', 'Adjustability': 'Fixed Hosel', 'Weight System': 'Lightweight', 'Weight Range': 'Fixed', 'Cost (MSRP)': '$649', 'Stock Length': '45.75"', 'Swing Weight': 'D0', 'Target Player Profile': '15+ HCP (Slow Swing)', 'Spin Profile': 'High', 'Bias': 'Draw Bias', 'Offset': 'Slight', 'Left Handed': '✓'},
    {'Manufacturer': 'Callaway', 'Release Year': '2026', 'Model Name': 'Quantum Triple Diamond', 'Category': 'Tour Performance', 'CC': '450', 'Standard Loft': '8, 9, 10.5', 'Face Material': 'Tri-Force Face', 'Adjustability': '+/- 2.0', 'Weight System': 'Front/Back Pods', 'Weight Range': '10g/4g', 'Cost (MSRP)': '$649', 'Stock Length': '45.5"', 'Swing Weight': 'D4', 'Target Player Profile': '0-5 HCP', 'Spin Profile': 'Very Low', 'Bias': 'Fade', 'Offset': 'None', 'Left Handed': 'No'},
    {'Manufacturer': 'Callaway', 'Release Year': '2026', 'Model Name': 'Quantum Triple Diamond Max', 'Category': 'Tour Forgiveness', 'CC': '460', 'Standard Loft': '9, 10.5', 'Face Material': 'Tri-Force Face', 'Adjustability': '+/- 2.0', 'Weight System': 'Front/Back Pods', 'Weight Range': '10g/4g', 'Cost (MSRP)': '$649', 'Stock Length': '45.5"', 'Swing Weight': 'D4', 'Target Player Profile': '0-10 HCP', 'Spin Profile': 'Low', 'Bias': 'Neutral', 'Offset': 'None', 'Left Handed': 'No'},

    # PING
    {'Manufacturer': 'PING', 'Release Year': '2026', 'Model Name': 'G440 MAX', 'Category': 'Versatile Forgiveness', 'CC': '460', 'Standard Loft': '9, 10.5, 12', 'Face Material': 'Forged VFT Ti', 'Adjustability': '+/- 1.5', 'Weight System': 'Tungsten Back Weight', 'Weight Range': 'High MOI', 'Cost (MSRP)': '$599', 'Stock Length': '45.75"', 'Swing Weight': 'D3', 'Target Player Profile': 'All Skill Levels', 'Spin Profile': 'Mid', 'Bias': 'Neutral', 'Offset': 'None', 'Left Handed': '✓'},
    {'Manufacturer': 'PING', 'Release Year': '2026', 'Model Name': 'G440 K', 'Category': 'Maximum Stability', 'CC': '460', 'Standard Loft': '9, 10.5, 12', 'Face Material': 'Forged VFT Ti', 'Adjustability': '+/- 1.5', 'Weight System': '32g Back Weight', 'Weight Range': 'Adjustable', 'Cost (MSRP)': '$649', 'Stock Length': '45.75"', 'Swing Weight': 'D3', 'Target Player Profile': '10+ HCP', 'Spin Profile': 'Mid-High', 'Bias': 'Adjustable', 'Offset': 'None', 'Left Handed': '✓'},
    {'Manufacturer': 'PING', 'Release Year': '2026', 'Model Name': 'G440 LST', 'Category': 'Low Spin', 'CC': '445', 'Standard Loft': '9, 10.5', 'Face Material': 'Forged VFT', 'Adjustability': '+/- 1.5', 'Weight System': 'Tungsten Weight', 'Weight Range': 'Adjustable', 'Cost (MSRP)': '$629', 'Stock Length': '45.25"', 'Swing Weight': 'D4', 'Target Player Profile': '0-5 HCP', 'Spin Profile': 'Low', 'Bias': 'Neutral/Fade', 'Offset': 'None', 'Left Handed': '✓'},
    {'Manufacturer': 'PING', 'Release Year': '2026', 'Model Name': 'G440 SFT', 'Category': 'Straight Flight Tech', 'CC': '460', 'Standard Loft': '10.5, 12', 'Face Material': 'Forged VFT', 'Adjustability': '+/- 1.5', 'Weight System': 'Heel Weight', 'Weight Range': 'Adjustable', 'Cost (MSRP)': '$599', 'Stock Length': '45.75"', 'Swing Weight': 'D2', 'Target Player Profile': '15+ HCP (Slicer)', 'Spin Profile': 'Mid-High', 'Bias': 'Draw Bias', 'Offset': 'Slight', 'Left Handed': '✓'}
]

final_drivers = new_rows + remaining_drivers
data['Drivers'] = final_drivers

# Rewrite Drivers CSV
with open('Data/Golf Comparison - Drivers.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=list(final_drivers[0].keys()))
    writer.writeheader()
    writer.writerows(final_drivers)

# Rewrite data.js
with open('data.js', 'w', encoding='utf-8') as f:
    f.write('const golfData = ' + json.dumps(data, indent=2) + ';')

print("Recovered and Updated Drivers.csv and data.js successfully.")
