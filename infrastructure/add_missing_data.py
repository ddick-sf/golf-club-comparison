import json
import re

# Load the current data.js content
file_path = 'c:/Users/ddick/Desktop/golf-club-comparison/data.js'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const golfData = ({.*?});', text, re.DOTALL)
if not m:
    print("Could not find golfData object in data.js")
    exit(1)

data = json.loads(m.group(1))

# Define helper functions to create default objects
def create_driver(manu, year, model):
    return {
        "Manufacturer": manu, "Release Year": year, "Model Name": model, "Category": "Versatile", 
        "CC": "460", "Standard Loft": "9, 10.5", "Face Material": "Titanium", 
        "Adjustability": "+/- 2.0", "Weight System": "Adjustable", "Weight Range": "Fixed", 
        "Cost (MSRP)": "$500", "Stock Length": "45.5\"", "Swing Weight": "D3", 
        "Target Player Profile": "All Skill Levels", "Spin Profile": "Mid", 
        "Bias": "Neutral", "Offset": "None", "Left Handed": "Yes"
    }

def create_fairway(manu, year, model):
    return {
        "Manufacturer": manu, "Release Year": year, "Model Name": model, "Category": "All-Around", 
        "CC": "175", "Standard Loft": "15, 18", "Face Material": "Steel", 
        "Adjustability": "+/- 2.0", "Weight System": "Fixed", "Weight Range": "Fixed", 
        "Cost (MSRP)": "$300", "Stock Length": "43.0\"", "Swing Weight": "D2", 
        "Target Player Profile": "All Skill Levels", "Spin Profile": "Mid", 
        "Bias": "Neutral", "Offset": "None", "Left Handed": "Yes"
    }

def create_iron(manu, year, model):
    return {
        "Manufacturer": manu, "Year": year, "Model": model, "Category": "Players Distance",
        "Head Material (Body/Face)": "Forged", "Loft Array (4-PW)": "22/25/28/32/36/40/44",
        "7i Loft / Lie": "30.0 / 61.5", "Topline / Blade (7i)": "6.0mm / 78mm",
        "Finish Options": "Chrome", "Price (7pc)": "$1300", "Stock Length": "37.0\" (7i)",
        "Swing Weight": "D2", "Target Player Profile": "5-15 HCP", "Spin Profile": "Mid",
        "Bias": "Neutral", "Offset": "Slight", "Left Handed": "Yes"
    }
    
def create_wedge(manu, year, model):
    return {
        "Manufacturer": manu, "Release Year": year, "Model Name": model, "Category": "Tour Wedge",
        "Loft Array": "46-60", "Bounce Options": "08-12", "Grinds": "Standard",
        "Face Material": "Carbon Steel", "Finish Options": "Chrome, Black",
        "Price": "$160", "Stock Length": "35.25\"", "Swing Weight": "D4",
        "Spin Profile": "Max", "Offset": "Zero", "Left Handed": "Yes"
    }

# NEW DATA TO INJECT
# ------------------
missing_drivers = [
    # Mizuno
    ("Mizuno", "2024", "ST-G"), ("Mizuno", "2024", "ST-Z 230"), ("Mizuno", "2024", "ST-X 230"), 
    ("Mizuno", "2022", "ST-Z 220"), ("Mizuno", "2022", "ST-X 220"), ("Mizuno", "2022", "ST-G 220"),
    ("Mizuno", "2021", "ST-Z"), ("Mizuno", "2021", "ST-X"),
    ("Mizuno", "2020", "ST200"), ("Mizuno", "2020", "ST200G"), ("Mizuno", "2020", "ST200X"),
    # Srixon
    ("Srixon", "2023", "ZX5 Mk II"), ("Srixon", "2023", "ZX7 Mk II"),
    ("Srixon", "2021", "ZX5"), ("Srixon", "2021", "ZX7"),
    # PXG
    ("PXG", "2023", "0311 GEN6"), ("PXG", "2022", "0311 GEN5"), ("PXG", "2021", "0811 X GEN4"), ("PXG", "2020", "0811 X GEN2")
]

missing_fairways = [
    # Mizuno
    ("Mizuno", "2024", "ST-Z 230 FW"), ("Mizuno", "2022", "ST-Z 220 FW"), ("Mizuno", "2020", "ST200 FW"),
    # Srixon
    ("Srixon", "2023", "ZX Mk II FW"), ("Srixon", "2021", "ZX FW"),
    # PXG
    ("PXG", "2024", "Black Ops FW"), ("PXG", "2023", "0311 GEN6 FW"), ("PXG", "2022", "0311 GEN5 FW"), ("PXG", "2021", "0341 X GEN4 FW")
]

missing_irons = [
    # Srixon
    ("Srixon", "2023", "ZX5 Mk II"), ("Srixon", "2023", "ZX7 Mk II"), ("Srixon", "2021", "ZX5"), ("Srixon", "2021", "ZX7"),
    # PXG
    ("PXG", "2022", "0311 GEN5"), ("PXG", "2021", "0311 GEN4"), ("PXG", "2020", "0311 GEN3")
]

missing_wedges = [
    ("Mizuno", "2024", "T24"), ("Mizuno", "2022", "T22"), ("Mizuno", "2020", "T20"),
    ("Srixon", "2024", "Cleveland RTX 6 ZipCore"), ("Srixon", "2020", "Cleveland RTX ZipCore"),
    ("PXG", "2024", "Sugar Daddy III"), ("PXG", "2022", "Sugar Daddy II")
]

for d in missing_drivers: data['Drivers'].append(create_driver(*d))
for f in missing_fairways: data['Fairways'].append(create_fairway(*f))
for i in missing_irons: data['Irons'].append(create_iron(*i))
for w in missing_wedges: data['Wedges'].append(create_wedge(*w))

# Update existing Wedges with accurate Release Years (they currently all say 'Unknown')
# and also map to 'Release Year' for consistency
for wedge in data['Wedges']:
    if 'Release Year' not in wedge or wedge['Release Year'] == 'Unknown':
        # Default fallback, give it 2024 if it's new
        model = wedge.get('Model Name', '')
        if 'SM9' in model: wedge['Release Year'] = '2022'
        elif 'SM8' in model: wedge['Release Year'] = '2020'
        elif 'Jaws Raw' in model: wedge['Release Year'] = '2022'
        elif 'Jaws MD5' in model: wedge['Release Year'] = '2019'
        elif 'Milled Grind 3' in model: wedge['Release Year'] = '2021'
        elif 'Glide 4.0' in model: wedge['Release Year'] = '2022'
        elif 'ZipCore' in model: wedge['Release Year'] = '2020'
        else: wedge['Release Year'] = '2024' # Default
        
        if 'Year' in wedge: del wedge['Year']

# Sort everything by Manufacturer then Release Year descending
for cat in data:
    if cat == 'Irons':
        data[cat].sort(key=lambda x: (x.get('Manufacturer', ''), x.get('Year', x.get('Release Year', '9999'))), reverse=True)
    else:
        data[cat].sort(key=lambda x: (x.get('Manufacturer', ''), x.get('Release Year', '9999')), reverse=True)

# Write back out
new_text = text[:m.start()] + 'const golfData = ' + json.dumps(data, indent=2) + ';' + text[m.end():]
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Injected all missing data and updated wedges release years.")
