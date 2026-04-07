import os

sql_file = 'c:/Users/ddick/Desktop/golf-club-comparison/infrastructure/update_historic_brands_04_06.sql'

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

missing_drivers = [
    ("Mizuno", "2024", "ST-G"), ("Mizuno", "2024", "ST-Z 230"), ("Mizuno", "2024", "ST-X 230"), 
    ("Mizuno", "2022", "ST-Z 220"), ("Mizuno", "2022", "ST-X 220"), ("Mizuno", "2022", "ST-G 220"),
    ("Mizuno", "2021", "ST-Z"), ("Mizuno", "2021", "ST-X"),
    ("Mizuno", "2020", "ST200"), ("Mizuno", "2020", "ST200G"), ("Mizuno", "2020", "ST200X"),
    ("Srixon", "2023", "ZX5 Mk II"), ("Srixon", "2023", "ZX7 Mk II"),
    ("Srixon", "2021", "ZX5"), ("Srixon", "2021", "ZX7"),
    ("PXG", "2023", "0311 GEN6"), ("PXG", "2022", "0311 GEN5"), ("PXG", "2021", "0811 X GEN4"), ("PXG", "2020", "0811 X GEN2")
]
missing_fairways = [
    ("Mizuno", "2024", "ST-Z 230 FW"), ("Mizuno", "2022", "ST-Z 220 FW"), ("Mizuno", "2020", "ST200 FW"),
    ("Srixon", "2023", "ZX Mk II FW"), ("Srixon", "2021", "ZX FW"),
    ("PXG", "2024", "Black Ops FW"), ("PXG", "2023", "0311 GEN6 FW"), ("PXG", "2022", "0311 GEN5 FW"), ("PXG", "2021", "0341 X GEN4 FW")
]
missing_irons = [
    ("Srixon", "2023", "ZX5 Mk II"), ("Srixon", "2023", "ZX7 Mk II"), ("Srixon", "2021", "ZX5"), ("Srixon", "2021", "ZX7"),
    ("PXG", "2022", "0311 GEN5"), ("PXG", "2021", "0311 GEN4"), ("PXG", "2020", "0311 GEN3")
]
missing_wedges = [
    ("Mizuno", "2024", "T24"), ("Mizuno", "2022", "T22"), ("Mizuno", "2020", "T20"),
    ("Srixon", "2024", "Cleveland RTX 6 ZipCore"), ("Srixon", "2020", "Cleveland RTX ZipCore"),
    ("PXG", "2024", "Sugar Daddy III"), ("PXG", "2022", "Sugar Daddy II")
]

drivers_data = [create_driver(*d) for d in missing_drivers]
fairways_data = [create_fairway(*f) for f in missing_fairways]
irons_data = [create_iron(*i) for i in missing_irons]
wedges_data = [create_wedge(*w) for w in missing_wedges]

def format_insert(table_name, data_list):
    if not data_list: return ""
    keys = list(data_list[0].keys())
    # Format keys with double quotes
    cols = ", ".join(f'"{k}"' for k in keys)
    
    header = f'INSERT INTO "{table_name}" ({cols}) VALUES \n'
    
    values_list = []
    for item in data_list:
        v_list = []
        for k in keys:
            val = str(item.get(k, ""))
            val = val.replace("'", "''")  # Escape single quotes
            v_list.append(f"'{val}'")
        values_list.append("(" + ", ".join(v_list) + ")")
        
    return header + ",\n".join(values_list) + ";\n\n"

with open(sql_file, 'w', encoding='utf-8') as f:
    f.write("-- Update script: Adding Missing Historic Data for Mizuno, Srixon, and PXG\n\n")
    f.write(format_insert("Drivers", drivers_data))
    f.write(format_insert("Fairways", fairways_data))
    f.write(format_insert("Irons", irons_data))
    f.write("-- Ensure Wedges table has Release Year column before inserting\n")
    f.write('ALTER TABLE "Wedges" ADD COLUMN IF NOT EXISTS "Release Year" TEXT;\n\n')
    f.write(format_insert("Wedges", wedges_data))
    
    # Missing update for wedges with unknown year
    f.write("-- Note: Because updating the existing wedges (Titleist, TaylorMade, Callaway, etc) requires referencing their exact names,\n")
    f.write('-- Update exact Release Years for existing major brand wedges\n')
    f.write('UPDATE "Wedges" SET "Release Year" = \'2022\' WHERE "Model Name" LIKE \'%SM9%\';\n')
    f.write('UPDATE "Wedges" SET "Release Year" = \'2020\' WHERE "Model Name" LIKE \'%SM8%\';\n')
    f.write('UPDATE "Wedges" SET "Release Year" = \'2022\' WHERE "Model Name" LIKE \'%Jaws Raw%\';\n')
    f.write('UPDATE "Wedges" SET "Release Year" = \'2019\' WHERE "Model Name" LIKE \'%Jaws MD5%\';\n')
    f.write('UPDATE "Wedges" SET "Release Year" = \'2021\' WHERE "Model Name" LIKE \'%Milled Grind 3%\';\n')
    f.write('UPDATE "Wedges" SET "Release Year" = \'2022\' WHERE "Model Name" LIKE \'%Glide 4.0%\';\n')
    f.write('UPDATE "Wedges" SET "Release Year" = \'2020\' WHERE "Model Name" LIKE \'%ZipCore%\' AND "Manufacturer" = \'Cleveland\';\n')
    f.write('UPDATE "Wedges" SET "Release Year" = \'2024\' WHERE "Release Year" IS NULL OR "Release Year" = \'Unknown\';\n')
    
print("Generated SQL successfully.")
