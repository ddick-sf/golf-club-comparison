import csv, json

fairways = [
    # Callaway
    {'Manufacturer': 'Callaway', 'Year': '2026', 'Model Name': 'Quantum Max', 'Release Year': '2026', 'Category': 'Max Launch', 'CC': '185', 'Standard Loft': '15, 18, 21', 'Face Material': 'Tri-Force Face', 'Adjustability': '+/- 2.0', 'Weight System': 'Heel-Biased', 'Weight Range': 'Fixed', 'Cost (MSRP)': '$349', 'Stock Length': '43.25"', 'Swing Weight': 'D2', 'Target Player Profile': '15+ HCP', 'Spin Profile': 'Mid-High', 'Bias': 'Draw Bias', 'Offset': 'Slight', 'Left Handed': '✓'},
    {'Manufacturer': 'Callaway', 'Year': '2026', 'Model Name': 'Quantum TD', 'Release Year': '2026', 'Category': 'Tour Performance', 'CC': '170', 'Standard Loft': '13.5, 15, 18', 'Face Material': 'Tri-Force Face', 'Adjustability': '+/- 2.0', 'Weight System': 'Front/Back Pods', 'Weight Range': '10g/4g', 'Cost (MSRP)': '$349', 'Stock Length': '43.0"', 'Swing Weight': 'D3', 'Target Player Profile': '0-5 HCP', 'Spin Profile': 'Low', 'Bias': 'Neutral', 'Offset': 'None', 'Left Handed': '✓'},
    # TaylorMade
    {'Manufacturer': 'TaylorMade', 'Year': '2026', 'Model Name': 'Qi4D Core', 'Release Year': '2026', 'Category': 'Versatile', 'CC': '180', 'Standard Loft': '15, 16.5, 18', 'Face Material': 'C300 Maraging', 'Adjustability': 'Fixed', 'Weight System': 'Speed Pocket', 'Weight Range': 'Fixed', 'Cost (MSRP)': '$349', 'Stock Length': '43.25"', 'Swing Weight': 'D2', 'Target Player Profile': 'All Skill Levels', 'Spin Profile': 'Mid', 'Bias': 'Neutral', 'Offset': 'None', 'Left Handed': '✓'},
    {'Manufacturer': 'TaylorMade', 'Year': '2026', 'Model Name': 'Qi4D Tour', 'Release Year': '2026', 'Category': 'Low Spin', 'CC': '175', 'Standard Loft': '15, 18', 'Face Material': 'Titanium/Tungsten', 'Adjustability': '+/- 2.0', 'Weight System': '50g Sliding Weight', 'Weight Range': 'Adjustable', 'Cost (MSRP)': '$449', 'Stock Length': '43.25"', 'Swing Weight': 'D3', 'Target Player Profile': '0-5 HCP', 'Spin Profile': 'Very Low', 'Bias': 'Adjustable', 'Offset': 'None', 'Left Handed': '✓'},
    # Titleist
    {'Manufacturer': 'Titleist', 'Year': '2026', 'Model Name': 'GT2', 'Release Year': '2026', 'Category': 'High Launch', 'CC': '180', 'Standard Loft': '13.5, 15, 16.5, 18', 'Face Material': 'Forged L-Cup', 'Adjustability': '+/- 1.5', 'Weight System': 'Rear Weight', 'Weight Range': '9g Fixed', 'Cost (MSRP)': '$349', 'Stock Length': '43.0"', 'Swing Weight': 'D3', 'Target Player Profile': 'All Skill Levels', 'Spin Profile': 'Mid', 'Bias': 'Neutral', 'Offset': 'None', 'Left Handed': '✓'},
    {'Manufacturer': 'Titleist', 'Year': '2026', 'Model Name': 'GT3', 'Category': 'Precision', 'Release Year': '2026', 'CC': '175', 'Standard Loft': '15, 16.5, 18', 'Face Material': 'Forged L-Cup', 'Adjustability': '+/- 1.5', 'Weight System': 'SureFit CG Track', 'Weight Range': 'Adjustable', 'Cost (MSRP)': '$349', 'Stock Length': '43.0"', 'Swing Weight': 'D3', 'Target Player Profile': '0-10 HCP', 'Spin Profile': 'Low', 'Bias': 'Adjustable', 'Offset': 'None', 'Left Handed': '✓'},
    # PING
    {'Manufacturer': 'PING', 'Year': '2026', 'Model Name': 'G440 MAX', 'Release Year': '2026', 'Category': 'All-Around', 'CC': '174', 'Standard Loft': '15, 18, 21', 'Face Material': 'Maraging Steel', 'Adjustability': '+/- 1.5', 'Weight System': 'Tungsten Rear Weight', 'Weight Range': 'Fixed', 'Cost (MSRP)': '$349', 'Stock Length': '43.0"', 'Swing Weight': 'D2', 'Target Player Profile': 'All Skill Levels', 'Spin Profile': 'Mid', 'Bias': 'Neutral', 'Offset': 'None', 'Left Handed': '✓'},
    {'Manufacturer': 'PING', 'Year': '2026', 'Model Name': 'G440 LST', 'Release Year': '2026', 'Category': 'Low Spin', 'CC': '165', 'Standard Loft': '15', 'Face Material': 'Titanium/Tungsten', 'Adjustability': '+/- 1.5', 'Weight System': 'Tungsten Sole Weight', 'Weight Range': 'Fixed', 'Cost (MSRP)': '$429', 'Stock Length': '43.0"', 'Swing Weight': 'D3', 'Target Player Profile': '0-5 HCP', 'Spin Profile': 'Low', 'Bias': 'Fade Bias', 'Offset': 'None', 'Left Handed': '✓'},
    # Cobra
    {'Manufacturer': 'Cobra', 'Year': '2026', 'Model Name': 'OPTM X', 'Release Year': '2026', 'Category': 'Forgiveness', 'CC': '180', 'Standard Loft': '15, 18', 'Face Material': 'H.O.T. Face Steel', 'Adjustability': '+/- 1.5', 'Weight System': 'Rear Weight', 'Weight Range': 'Fixed', 'Cost (MSRP)': '$329', 'Stock Length': '43.25"', 'Swing Weight': 'D2', 'Target Player Profile': '10+ HCP', 'Spin Profile': 'Mid', 'Bias': 'Neutral', 'Offset': 'None', 'Left Handed': '✓'},
    {'Manufacturer': 'Cobra', 'Year': '2026', 'Model Name': 'OPTM LS', 'Release Year': '2026', 'Category': 'Tour Performance', 'CC': '175', 'Standard Loft': '14.5, 17.5', 'Face Material': 'Titanium', 'Adjustability': '+/- 1.5', 'Weight System': '3-Port System', 'Weight Range': 'Adjustable', 'Cost (MSRP)': '$379', 'Stock Length': '43.0"', 'Swing Weight': 'D3', 'Target Player Profile': '0-5 HCP', 'Spin Profile': 'Low', 'Bias': 'Adjustable', 'Offset': 'None', 'Left Handed': '✓'},
]

irons = [
    # Mizuno
    {'Manufacturer': 'Mizuno', 'Year': '2026', 'Model': 'Pro 261 (Blade)', 'Category': 'Tour Blade', 'Head Material (Body/Face)': '1025E Pure Select Carbon', 'Loft Array (4-PW)': '24/27/30/34/38/42/46', '7i Loft / Lie': '34.0° / 61.5°', 'Topline / Blade (7i)': '4.5mm / 72mm', 'Finish Options': 'Satin Chrome', 'Price (7pc)': '$1,505', 'Stock Length': '37.0" (7i)', 'Swing Weight': 'D3', 'Target Player Profile': '0-3 HCP', 'Spin Profile': 'High', 'Bias': 'None', 'Offset': 'Minimal (1.2mm)', 'Left Handed': '✓'},
    {'Manufacturer': 'Mizuno', 'Year': '2026', 'Model': 'JPX 925 Hot Metal', 'Category': 'Game Improv.', 'Head Material (Body/Face)': '4140M Chromoly / Cavity', 'Loft Array (4-PW)': '19/22/25/29/33/37/42', '7i Loft / Lie': '29.0° / 62.0°', 'Topline / Blade (7i)': '8.0mm / 81mm', 'Finish Options': 'Chrome', 'Price (7pc)': '$1,155', 'Stock Length': '37.0" (7i)', 'Swing Weight': 'D2', 'Target Player Profile': '15+ HCP', 'Spin Profile': 'Low', 'Bias': 'Draw', 'Offset': 'Progressive (5.0mm)', 'Left Handed': '✓'},
    # TaylorMade
    {'Manufacturer': 'TaylorMade', 'Year': '2026', 'Model': 'P·770', 'Category': 'Players', 'Head Material (Body/Face)': '8620 Carbon / Forged 4140 Face', 'Loft Array (4-PW)': '22.5/25.5/29/33/37/41/46', '7i Loft / Lie': '33.0° / 62.5°', 'Topline / Blade (7i)': '6.5mm / 77mm', 'Finish Options': 'Satin Chrome', 'Price (7pc)': '$1,399', 'Stock Length': '37.0" (7i)', 'Swing Weight': 'D2', 'Target Player Profile': '5-10 HCP', 'Spin Profile': 'Mid', 'Bias': 'Neutral', 'Offset': 'Slight (2.0mm)', 'Left Handed': '✓'},
    {'Manufacturer': 'TaylorMade', 'Year': '2026', 'Model': 'P·790', 'Category': 'Players Distance', 'Head Material (Body/Face)': '8620 Carbon / SpeedFoam Air', 'Loft Array (4-PW)': '21/23.5/26.5/30.5/35/40/45', '7i Loft / Lie': '30.5° / 62.5°', 'Topline / Blade (7i)': '7.2mm / 79mm', 'Finish Options': 'Satin Chrome', 'Price (7pc)': '$1,499', 'Stock Length': '37.0" (7i)', 'Swing Weight': 'D2', 'Target Player Profile': '5-15 HCP', 'Spin Profile': 'Low-Mid', 'Bias': 'Neutral', 'Offset': 'Slight (2.7mm)', 'Left Handed': '✓'},
    # Titleist
    {'Manufacturer': 'Titleist', 'Year': '2026', 'Model': 'T100', 'Category': 'Tour Player', 'Head Material (Body/Face)': 'Forged 1025 / Dual Cavity', 'Loft Array (4-PW)': '24/27/30/34/38/42/46', '7i Loft / Lie': '34.0° / 63.0°', 'Topline / Blade (7i)': '5.0mm / 74mm', 'Finish Options': 'Satin Chrome', 'Price (7pc)': '$1,499', 'Stock Length': '37.0" (7i)', 'Swing Weight': 'D3', 'Target Player Profile': '0-5 HCP', 'Spin Profile': 'High', 'Bias': 'Neutral', 'Offset': 'Minimal (1.5mm)', 'Left Handed': '✓'},
    {'Manufacturer': 'Titleist', 'Year': '2026', 'Model': 'T150', 'Category': 'Players Distance', 'Head Material (Body/Face)': 'Forged 1025 / Hollow Muscle', 'Loft Array (4-PW)': '22/25/28/32/36/40/44', '7i Loft / Lie': '32.0° / 63.0°', 'Topline / Blade (7i)': '6.5mm / 78mm', 'Finish Options': 'Satin Chrome', 'Price (7pc)': '$1,499', 'Stock Length': '37.0" (7i)', 'Swing Weight': 'D3', 'Target Player Profile': '0-10 HCP', 'Spin Profile': 'Mid', 'Bias': 'Neutral', 'Offset': 'Slight (2.0mm)', 'Left Handed': '✓'},
    {'Manufacturer': 'Titleist', 'Year': '2026', 'Model': 'T200', 'Category': 'Players Distance', 'Head Material (Body/Face)': 'Forged Face / Max Impact', 'Loft Array (4-PW)': '21/24/27/30.5/34.5/39/43', '7i Loft / Lie': '30.5° / 63.0°', 'Topline / Blade (7i)': '7.5mm / 81mm', 'Finish Options': 'Satin Chrome', 'Price (7pc)': '$1,499', 'Stock Length': '37.0" (7i)', 'Swing Weight': 'D2', 'Target Player Profile': '5-15 HCP', 'Spin Profile': 'Low-Mid', 'Bias': 'Neutral', 'Offset': 'Progressive (3.0mm)', 'Left Handed': '✓'},
    # Callaway
    {'Manufacturer': 'Callaway', 'Year': '2026', 'Model': 'Apex Pro', 'Category': 'Players Cavity', 'Head Material (Body/Face)': 'Forged 1025 Carbon Steel', 'Loft Array (4-PW)': '23/26/29/33/37/41/45', '7i Loft / Lie': '33.0° / 62.0°', 'Topline / Blade (7i)': '5.5mm / 76mm', 'Finish Options': 'Satin', 'Price (7pc)': '$1,500', 'Stock Length': '37.0" (7i)', 'Swing Weight': 'D3', 'Target Player Profile': '0-5 HCP', 'Spin Profile': 'Mid-High', 'Bias': 'Neutral', 'Offset': 'Minimal (1.8mm)', 'Left Handed': '✓'},
    {'Manufacturer': 'Callaway', 'Year': '2026', 'Model': 'Apex Ai200', 'Category': 'Players Distance', 'Head Material (Body/Face)': 'Forged Hollow / AI Face', 'Loft Array (4-PW)': '21/23.5/26/30/34/38/43', '7i Loft / Lie': '30.0° / 62.0°', 'Topline / Blade (7i)': '7.0mm / 79mm', 'Finish Options': 'Satin/Chrome', 'Price (7pc)': '$1,450', 'Stock Length': '37.0" (7i)', 'Swing Weight': 'D2', 'Target Player Profile': '5-15 HCP', 'Spin Profile': 'Mid', 'Bias': 'Neutral', 'Offset': 'Slight (2.5mm)', 'Left Handed': '✓'},
    # PING
    {'Manufacturer': 'PING', 'Year': '2026', 'Model': 'Blueprint S', 'Category': 'Tour Player', 'Head Material (Body/Face)': 'Forged 8620 Carbon Steel', 'Loft Array (4-PW)': '23/26/29.5/33/37/41/45', '7i Loft / Lie': '33.0° / 62.0°', 'Topline / Blade (7i)': '4.8mm / 74mm', 'Finish Options': 'Hydropearl 2.0', 'Price (7pc)': '$1,500', 'Stock Length': '37.0" (7i)', 'Swing Weight': 'D2', 'Target Player Profile': '0-3 HCP', 'Spin Profile': 'High', 'Bias': 'None', 'Offset': 'Minimal (1.5mm)', 'Left Handed': '✓'},
    {'Manufacturer': 'PING', 'Year': '2026', 'Model': 'i230', 'Category': 'Players Cavity', 'Head Material (Body/Face)': '431 Stainless Steel', 'Loft Array (4-PW)': '22.5/26/29.5/33/37/41/45', '7i Loft / Lie': '33.0° / 62.0°', 'Topline / Blade (7i)': '6.0mm / 77mm', 'Finish Options': 'Hydropearl 2.0', 'Price (7pc)': '$1,400', 'Stock Length': '37.0" (7i)', 'Swing Weight': 'D2', 'Target Player Profile': '0-10 HCP', 'Spin Profile': 'Mid', 'Bias': 'Neutral', 'Offset': 'Slight (2.0mm)', 'Left Handed': '✓'}
]

wedges = [
    {'Manufacturer': 'Titleist', 'Model Name': 'Vokey SM11', 'Category': 'Tour Wedge', 'Loft Array': '46-62', 'Bounce Options': '04-14', 'Grinds': 'F, M, S, D, K, T', 'Face Material': 'Cast Carbon / Spin Milled', 'Finish Options': 'Tour Chrome, Jet Black, Raw', 'Price': '$189', 'Stock Length': '35.25"', 'Swing Weight': 'D3-D5', 'Spin Profile': 'Max', 'Offset': 'Zero', 'Left Handed': '✓'},
    {'Manufacturer': 'Callaway', 'Model Name': 'Opus', 'Category': 'Tour Wedge', 'Loft Array': '48-60', 'Bounce Options': '08-12', 'Grinds': 'S, W, C, T', 'Face Material': 'Milled Carbon / Micro-Grooves', 'Finish Options': 'Platinum Chrome, Black Shadow', 'Price': '$179', 'Stock Length': '35.25"', 'Swing Weight': 'D3-D4', 'Spin Profile': 'Max', 'Offset': 'Zero', 'Left Handed': '✓'},
    {'Manufacturer': 'TaylorMade', 'Model Name': 'Milled Grind 5', 'Category': 'Tour Wedge', 'Loft Array': '46-60', 'Bounce Options': '08-12', 'Grinds': 'Standard, Low, High, TW', 'Face Material': 'Cast Carbon / Laser Etched', 'Finish Options': 'Satin Chrome, Black', 'Price': '$179', 'Stock Length': '35.25"', 'Swing Weight': 'D3-D5', 'Spin Profile': 'Max', 'Offset': 'Zero', 'Left Handed': '✓'},
    {'Manufacturer': 'PING', 'Model Name': 's159', 'Category': 'Specialty Wedge', 'Loft Array': '46-62', 'Bounce Options': '06-14', 'Grinds': 'S, W, T, H, E, B', 'Face Material': '8620 Carbon / Friction Face', 'Finish Options': 'Hydropearl 2.0, Midnight', 'Price': '$179', 'Stock Length': '35.25"', 'Swing Weight': 'D3-D4', 'Spin Profile': 'Max', 'Offset': 'Zero', 'Left Handed': '✓'},
    {'Manufacturer': 'Cleveland', 'Model Name': 'RTX 7 ZipCore', 'Category': 'Tour Wedge', 'Loft Array': '46-60', 'Bounce Options': '06-12', 'Grinds': 'Low, Mid, Full, Mid+', 'Face Material': '8620 Carbon / UltiZip', 'Finish Options': 'Tour Satin, Black Satin, Raw', 'Price': '$169', 'Stock Length': '35.25"', 'Swing Weight': 'D3-D5', 'Spin Profile': 'Max', 'Offset': 'Zero', 'Left Handed': '✓'}
]


with open('Data/Golf Comparison - Fairway.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=list(fairways[0].keys()))
    writer.writeheader()
    writer.writerows(fairways)

with open('Data/Golf Comparison - Irons.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=list(irons[0].keys()))
    writer.writeheader()
    writer.writerows(irons)

with open('Data/Golf Comparison - Wedges.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=list(wedges[0].keys()))
    writer.writeheader()
    writer.writerows(wedges)

# update JS
with open('Data/Golf Comparison - Drivers.csv', 'r', encoding='utf-8') as f:
    d_rows = list(csv.DictReader(f))

data = {'Drivers': d_rows, 'Fairways': fairways, 'Irons': irons, 'Wedges': wedges}
with open('data.js', 'w', encoding='utf-8') as f:
    f.write('const golfData = ' + json.dumps(data, indent=2) + ';')

print("Created Fairways, Irons, and Wedges successfully!")
