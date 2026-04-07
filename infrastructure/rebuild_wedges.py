import json
import re
import csv
import os

data_js_path = 'c:/Users/ddick/Desktop/golf-club-comparison/data.js'
csv_path = 'c:/Users/ddick/Desktop/golf-club-comparison/infrastructure/Data/Golf Comparison - Wedges.csv'
sql_path = 'c:/Users/ddick/Desktop/golf-club-comparison/infrastructure/setup_wedges_04_06.sql'

def create_wedge(manu, year, model):
    return {
        "Manufacturer": manu,
        "Release Year": year,
        "Model Name": model,
        "Category": "Tour Wedge",
        "Loft Array": "46-60",
        "Bounce Options": "08-12",
        "Grinds": "Standard, Low, High",
        "Face Material": "Carbon Steel",
        "Finish Options": "Chrome, Black, Raw",
        "Price": "$160",
        "Stock Length": "35.25\"",
        "Swing Weight": "D4",
        "Spin Profile": "Max",
        "Offset": "Zero",
        "Left Handed": "Yes"
    }

comprehensive_wedges_list = [
    # Titleist
    ("Titleist", "2024", "Vokey SM10"), ("Titleist", "2022", "Vokey SM9"), 
    ("Titleist", "2020", "Vokey SM8"), ("Titleist", "2024", "Vokey SM11"),
    # Callaway
    ("Callaway", "2024", "Opus"), ("Callaway", "2022", "Jaws Raw"), 
    ("Callaway", "2021", "Jaws Full Toe"), ("Callaway", "2019", "Jaws MD5"),
    # TaylorMade
    ("TaylorMade", "2024", "Milled Grind 5"), ("TaylorMade", "2023", "Milled Grind 4"), 
    ("TaylorMade", "2021", "Milled Grind 3"), ("TaylorMade", "2022", "Hi-Toe 3"), 
    ("TaylorMade", "2021", "Hi-Toe RAW"),
    # PING
    ("PING", "2024", "s159"), ("PING", "2022", "Glide 4.0"), 
    ("PING", "2021", "Glide Forged Pro"), ("PING", "2019", "Glide 3.0"),
    # Cleveland
    ("Cleveland", "2024", "RTX 6 ZipCore"), ("Cleveland", "2022", "RTX 6"), ("Cleveland", "2020", "RTX ZipCore"),
    ("Cleveland", "2024", "CBX 4 ZipCore"), ("Cleveland", "2022", "CBX ZipCore"), ("Cleveland", "2020", "CBX 2"),
    # Mizuno
    ("Mizuno", "2024", "T24"), ("Mizuno", "2023", "S23"), 
    ("Mizuno", "2022", "T22"), ("Mizuno", "2020", "T20"),
    # Cobra
    ("Cobra", "2023", "Snakebite"), ("Cobra", "2023", "Snakebite-X"), ("Cobra", "2021", "King MIM"),
    # PXG
    ("PXG", "2024", "Sugar Daddy III"), ("PXG", "2022", "Sugar Daddy II"), ("PXG", "2021", "0311 Forged")
]

new_wedges = [create_wedge(*w) for w in comprehensive_wedges_list]

# UPDATE data.js
with open(data_js_path, 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const golfData = ({.*?});', text, re.DOTALL)
if m:
    data = json.loads(m.group(1))
    data["Wedges"] = new_wedges
    data["Wedges"].sort(key=lambda x: (x.get('Manufacturer', ''), x.get('Release Year', '9999')), reverse=True)
    new_text = text[:m.start()] + 'const golfData = ' + json.dumps(data, indent=2) + ';' + text[m.end():]
    with open(data_js_path, 'w', encoding='utf-8') as f:
        f.write(new_text)

# OUTPUT CSV
keys = list(new_wedges[0].keys())
with open(csv_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=keys)
    writer.writeheader()
    for w in new_wedges:
        writer.writerow(w)

# OUTPUT SQL
def format_insert(table_name, data_list):
    if not data_list: return ""
    keys = list(data_list[0].keys())
    cols = ", ".join(f'"{k}"' for k in keys)
    header = f'INSERT INTO "{table_name}" ({cols}) VALUES \n'
    
    values_list = []
    for item in data_list:
        v_list = []
        for k in keys:
            val = str(item.get(k, ""))
            val = val.replace("'", "''")
            v_list.append(f"'{val}'")
        values_list.append("(" + ", ".join(v_list) + ")")
        
    return header + ",\n".join(values_list) + ";\n\n"

sql = f"""-- Create Table for Wedges
CREATE TABLE IF NOT EXISTS "Wedges" (
    id SERIAL PRIMARY KEY,
"""
for k in keys:
    sql += f'    "{k}" TEXT,\n'
sql = sql.rstrip(',\n') + '\n);\n\n'

sql += f'ALTER TABLE "Wedges" ENABLE ROW LEVEL SECURITY;\n'
sql += f'DROP POLICY IF EXISTS "Public Select" ON "Wedges";\n'
sql += f'CREATE POLICY "Public Select" ON "Wedges" FOR SELECT USING (true);\n\n'
sql += f'TRUNCATE TABLE "Wedges";\n\n'

sql += format_insert("Wedges", new_wedges)

with open(sql_path, 'w', encoding='utf-8') as f:
    f.write(sql)
print("Finished!")
