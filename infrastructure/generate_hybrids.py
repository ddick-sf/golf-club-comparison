import json
import re
import os

file_path = 'c:/Users/ddick/Desktop/golf-club-comparison/data.js'
sql_path = 'c:/Users/ddick/Desktop/golf-club-comparison/infrastructure/setup_hybrids_04_06.sql'

def create_hybrid(manu, year, model, type="Hybrid"):
    return {
        "Manufacturer": manu,
        "Release Year": year,
        "Model Name": model,
        "Category": "Driving Iron" if "Iron" in type else "Versatile Hybrid",
        "Standard Loft": "19, 22" if "Hybrid" in type else "18, 20",
        "Face Material": "Maraging Steel" if "Hybrid" in type else "Forged",
        "Adjustability": "+/- 1.5" if "Hybrid" in type else "Fixed",
        "Length": "40.25\"" if "Hybrid" in type else "39.5\"",
        "Swing Weight": "D2",
        "Target Player Profile": "All Skill Levels" if "Hybrid" in type else "Low-Mid HCP",
        "Bias": "Neutral",
        "Cost": "$250",
        "Left Handed": "Yes"
    }

hybrid_list = [
    # TaylorMade
    ("TaylorMade", "2024", "Qi10 Rescue", "Hybrid"), ("TaylorMade", "2024", "P DHY", "Driving Iron"),
    ("TaylorMade", "2023", "Stealth 2 Rescue", "Hybrid"), ("TaylorMade", "2023", "Stealth UDI", "Driving Iron"),
    ("TaylorMade", "2022", "Stealth Rescue", "Hybrid"), ("TaylorMade", "2020", "SIM Max Rescue", "Hybrid"),
    # Callaway
    ("Callaway", "2024", "Paradym Ai Smoke Hybrid", "Hybrid"), ("Callaway", "2024", "X Forged UT", "Driving Iron"),
    ("Callaway", "2023", "Paradym Hybrid", "Hybrid"), ("Callaway", "2021", "Apex UW", "Hybrid"),
    ("Callaway", "2020", "Mavrik Hybrid", "Hybrid"),
    # Titleist
    ("Titleist", "2024", "TSR2 Hybrid", "Hybrid"), ("Titleist", "2023", "T200 Utility", "Driving Iron"),
    ("Titleist", "2022", "TSR3 Hybrid", "Hybrid"), ("Titleist", "2021", "TSi2 Hybrid", "Hybrid"),
    # PING
    ("PING", "2024", "G430 Hybrid", "Hybrid"), ("PING", "2024", "iCrossover", "Driving Iron"),
    ("PING", "2021", "G425 Hybrid", "Hybrid"),
    # Cobra
    ("Cobra", "2024", "Darkspeed Hybrid", "Hybrid"), ("Cobra", "2023", "Aerojet Hybrid", "Hybrid"),
    ("Cobra", "2022", "LTDx Hybrid", "Hybrid"), ("Cobra", "2020", "Speedzone Hybrid", "Hybrid"),
    # Mizuno
    ("Mizuno", "2024", "ST-MAX 230 Hybrid", "Hybrid"), ("Mizuno", "2023", "CLK Hybrid", "Hybrid"),
    ("Mizuno", "2022", "Mizuno Pro Fli-Hi", "Driving Iron"), ("Mizuno", "2020", "CLK Hybrid", "Hybrid"),
    # Srixon
    ("Srixon", "2023", "ZX Mk II Hybrid", "Hybrid"), ("Srixon", "2023", "ZX Mk II Utility", "Driving Iron"),
    ("Srixon", "2021", "ZX Hybrid", "Hybrid"), ("Srixon", "2021", "ZX Utility", "Driving Iron"),
    # PXG
    ("PXG", "2024", "Black Ops Hybrid", "Hybrid"), ("PXG", "2023", "0311 GEN6 Hybrid", "Hybrid"),
    ("PXG", "2023", "0311 X Driving Iron", "Driving Iron"), ("PXG", "2021", "0317 X GEN4", "Hybrid")
]

new_hybrids = [create_hybrid(*h) for h in hybrid_list]

# UPDATE data.js
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const golfData = ({.*?});', text, re.DOTALL)
if m:
    data = json.loads(m.group(1))
    data["Hybrids"] = new_hybrids
    # Sort
    data["Hybrids"].sort(key=lambda x: (x.get('Manufacturer', ''), x.get('Release Year', '9999')), reverse=True)
    new_text = text[:m.start()] + 'const golfData = ' + json.dumps(data, indent=2) + ';' + text[m.end():]
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Injected Hybrids into data.js")
    
# GENERATE SQL
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

sql = f"""-- Create Table for Hybrids
CREATE TABLE IF NOT EXISTS "Hybrids" (
    id SERIAL PRIMARY KEY,
"""
# Get keys
keys = list(new_hybrids[0].keys())
for k in keys:
    sql += f'    "{k}" TEXT,\n'
sql = sql.rstrip(',\n') + '\n);\n\n'

sql += f'ALTER TABLE "Hybrids" ENABLE ROW LEVEL SECURITY;\n'
sql += f'DROP POLICY IF EXISTS "Public Select" ON "Hybrids";\n'
sql += f'CREATE POLICY "Public Select" ON "Hybrids" FOR SELECT USING (true);\n\n'
sql += f'TRUNCATE TABLE "Hybrids";\n\n'

sql += format_insert("Hybrids", new_hybrids)

with open(sql_path, 'w', encoding='utf-8') as f:
    f.write(sql)
print("Generated setup_hybrids_04_06.sql")
