import csv
import os

drivers_data = [
    # 2024
    ["TaylorMade", "2024", "Qi10", "All-Around", "460", "9, 10.5, 12", "60X Carbon Twist Face", "+/- 2.0", "Fixed Back Weight", "Fixed", "$599", "45.75\"", "D4", "All Skill Levels", "Mid-Low", "Neutral", "None", "✓"],
    ["Callaway", "2024", "Paradym Ai Smoke Max", "All-Around", "460", "9, 10.5, 12", "Ai Smart Face", "+/- 2.0", "Adjustable Perimeter Track", "14g", "$599", "45.75\"", "D3", "All Skill Levels", "Mid", "Neutral", "None", "✓"],
    ["PING", "2024", "G430 Max 10K", "Max Forgiveness", "460", "9, 10.5, 12", "Forged T9S+ Titanium", "+/- 1.5", "Fixed Back Weight", "28g", "$599", "45.75\"", "D3", "All Skill Levels", "Low", "Neutral", "None", "✓"],
    ["Cobra", "2024", "Darkspeed X", "Speed/Forgiveness", "460", "9, 10.5, 12", "H.O.T. Face", "+/- 1.5", "Front/Back", "Adjustable", "$549", "45.5\"", "D3", "All Skill Levels", "Mid-Low", "Neutral", "None", "✓"],
    ["Titleist", "2024", "GT2", "Distance/Forgiveness", "460", "8, 9, 10.5, 11.5", "Proprietary Matrix Polymer", "+/- 1.5", "Interchangeable Back Weight", "Available", "$649", "45.5\"", "D3", "All Skill Levels", "Mid", "Neutral", "None", "✓"],
    
    # 2023
    ["TaylorMade", "2023", "Stealth 2", "All-Around", "460", "9, 10.5, 12", "60X Carbon Twist Face", "+/- 2.0", "Fixed Back Weight", "25g", "$599", "45.75\"", "D3", "All Skill Levels", "Mid", "Neutral", "None", "✓"],
    ["Callaway", "2023", "Paradym", "All-Around", "460", "9, 10.5, 12", "Forged Titanium", "+/- 2.0", "Adjustable Perimeter Track", "15g", "$599", "45.75\"", "D3", "All Skill Levels", "Low-Mid", "Neutral", "None", "✓"],
    ["PING", "2023", "G430 Max", "Max Forgiveness", "460", "9, 10.5, 12", "Forged T9S+ Ti", "+/- 1.5", "Adjustable CG Track", "25g", "$549", "45.75\"", "D3", "All Skill Levels", "Mid", "Neutral", "None", "✓"],
    ["Cobra", "2023", "Aerojet", "Speed", "460", "9, 10.5, 12", "PWRSHELL H.O.T. Face", "+/- 1.5", "Fixed Back/Forward", "12g", "$549", "45.5\"", "D3", "All Skill Levels", "Mid-Low", "Neutral", "None", "✓"],
    
    # 2022
    ["TaylorMade", "2022", "Stealth", "All-Around", "460", "9, 10.5, 12", "60X Carbon Twist Face", "+/- 2.0", "Fixed Back Weight", "Fixed", "$579", "45.75\"", "D4", "All Skill Levels", "Mid-Low", "Neutral", "None", "✓"],
    ["Callaway", "2022", "Rogue ST Max", "All-Around", "460", "9, 10.5, 12", "Flash Face SS22", "+/- 2.0", "Tungsten Speed Cartridge", "26g", "$549", "45.75\"", "D3+", "All Skill Levels", "Mid", "Slight Draw", "None", "✓"],
    ["Titleist", "2022", "TSR2", "Max Performance", "460", "8, 9, 10.5, 11", "ATI 425 Aerospace Ti", "+/- 1.5", "SureFit CG", "Adjustable", "$599", "45.5\"", "D3", "All Skill Levels", "Low-Mid", "Neutral", "None", "✓"],
    ["Cobra", "2022", "LTDx", "Extreme Distance", "460", "9, 10.5, 12", "H.O.T. Face", "+/- 1.5", "PWR-COR Technology", "Fixed", "$499", "45.5\"", "D2", "All Skill Levels", "Mid-Low", "Neutral", "None", "✓"],
    
    # 2021
    ["TaylorMade", "2021", "SIM2", "Tour Performance", "460", "8, 9, 10.5", "Forged Ring Construction", "+/- 2.0", "Rear Weight", "16g", "$529", "45.75\"", "D4", "0-10 HCP", "Low", "Neutral", "None", "✓"],
    ["Callaway", "2021", "Epic Speed", "Aero Speed", "460", "9, 10.5, 12", "Flash Face SS21", "+/- 2.0", "Jailbreak Speed Frame", "Fixed", "$529", "45.75\"", "D3", "All Skill Levels", "Mid-Low", "Neutral", "None", "✓"],
    ["PING", "2021", "G425 Max", "Max Forgiveness", "460", "9, 10.5, 12", "Forged T9S+ Ti", "+/- 1.5", "Adjustable CG Track", "26g", "$549", "45.75\"", "D3", "All Skill Levels", "Mid", "Neutral", "None", "✓"],
    ["Cobra", "2021", "RADSPEED", "Low Spin", "460", "9, 10.5", "CNC Milled Infinity Face", "+/- 1.5", "Radial Weighting", "28g/8g", "$449", "45.5\"", "D3", "0-10 HCP", "Low", "Neutral", "None", "✓"],
    
    # 2020
    ["TaylorMade", "2020", "SIM", "Tour Performance", "460", "8, 9, 10.5", "Injected Twist Face", "+/- 2.0", "Sliding Weight Track", "10g", "$549", "45.75\"", "D4", "0-10 HCP", "Low", "Adjustable", "None", "✓"],
    ["Callaway", "2020", "Mavrik", "Speed/Distance", "460", "9, 10.5, 12", "Flash Face SS20", "+/- 2.0", "Fixed Rear Weight", "Fixed", "$499", "45.75\"", "D3", "All Skill Levels", "Mid", "Neutral", "None", "✓"],
    ["Titleist", "2020", "TSi2", "Distance/Forgiveness", "460", "9, 10.5, 11", "ATI 425 Aerospace Ti", "+/- 1.5", "Fixed Back Weight", "Adjustable", "$549", "45.5\"", "D3", "All Skill Levels", "Mid", "Neutral", "None", "✓"],
    ["Cobra", "2020", "Speedzone", "Extreme Speed", "460", "9, 10.5", "CNC Milled Infinity Face", "+/- 1.5", "Front/Back CG", "Adjustable", "$449", "45.5\"", "D3", "All Skill Levels", "Low-Mid", "Neutral", "None", "✓"]
]

fairways_data = [
    # General rep values for fairways 2020-2024
    ["TaylorMade", "2024", "Qi10 FW", "2024", "All-Around", "190", "15, 18, 21", "C300 Steel", "Fixed", "V Steel Sole", "Fixed", "$349", "43.25\"", "D2", "All Skill Levels", "Mid", "Neutral", "None", "✓"],
    ["Callaway", "2024", "Paradym Ai Smoke FW", "2024", "All-Around", "180", "15, 18, 21", "Ai Smart Face", "Fixed", "Tungsten Speed Cartridge", "Fixed", "$349", "43.25\"", "D2", "All Skill Levels", "Mid", "Neutral", "None", "✓"],
    ["PING", "2023", "G430 Max FW", "2023", "Max Forgiveness", "175", "15, 18, 21", "Maraging Steel", "+/- 1.5", "High Density Tungsten", "Fixed", "$349", "43.0\"", "D1", "All Skill Levels", "Mid", "Neutral", "None", "✓"],
    ["TaylorMade", "2023", "Stealth 2 FW", "2023", "All-Around", "185", "15, 18, 21", "C300 Steel", "Fixed", "V Steel Sole", "Fixed", "$349", "43.25\"", "D2", "All Skill Levels", "Mid", "Neutral", "None", "✓"],
    ["Callaway", "2022", "Rogue ST Max FW", "2022", "All-Around", "175", "15, 18, 21", "C300 Steel", "Fixed", "Batwing Tech", "Fixed", "$349", "43.25\"", "D2", "All Skill Levels", "Mid", "Slight Draw", "None", "✓"],
    ["Titleist", "2022", "TSR2 FW", "2022", "Performance", "175", "15, 16.5, 18", "Stainless Steel", "+/- 1.5", "SureFit CG", "Adjustable", "$349", "43.0\"", "D2", "All Skill Levels", "Mid-Low", "Neutral", "None", "✓"],
    ["TaylorMade", "2021", "SIM2 Max FW", "2021", "All-Around", "190", "15, 18, 21", "C300 Steel", "Fixed", "V Steel Sole", "Fixed", "$299", "43.25\"", "D2", "All Skill Levels", "Mid", "Neutral", "None", "✓"],
    ["PING", "2021", "G425 Max FW", "2021", "Max Forgiveness", "175", "15, 17.5, 20.5", "Maraging Steel", "+/- 1.5", "Tungsten Back Weight", "Fixed", "$299", "43.0\"", "D1", "All Skill Levels", "Mid", "Neutral", "None", "✓"],
    ["Callaway", "2020", "Mavrik FW", "2020", "Distance", "174", "15, 18, 21", "Flash Face SS20", "Fixed", "Standard", "Fixed", "$299", "43.25\"", "D2", "All Skill Levels", "Mid", "Neutral", "None", "✓"],
    ["Titleist", "2020", "TSi2 FW", "2020", "Performance", "175", "15, 16.5, 18, 21", "Stainless Steel", "+/- 1.5", "SureFit CG", "Adjustable", "$299", "43.0\"", "D2", "All Skill Levels", "Mid", "Neutral", "None", "✓"]
]

irons_data = [
    ["TaylorMade", "2023", "P790 (2023)", "Players Distance", "8620 Carbon / SpeedFoam", "21/23.5/26.5/30.5/35/40/45", "30.5° / 62.5°", "7.2mm / 79mm", "Satin Chrome", "$1,399", "37.0\" (7i)", "D2", "5-15 HCP", "Mid-Low", "Neutral", "Slight", "✓"],
    ["Callaway", "2023", "Paradym Irons", "Players Distance", "Hollow Body / Forged Face", "20/23/26/29/33/37/42", "29.0° / 62.0°", "8.0mm / 80mm", "Chrome", "$1,400", "37.0\" (7i)", "D2", "5-15 HCP", "Mid", "Neutral", "Moderate", "✓"],
    ["PING", "2023", "G430 Irons", "Game Improv.", "17-4 Stainless Steel", "21/24/27.5/31/35/39.5/45", "29.0° / 62.0°", "9.0mm / 82mm", "Hydropearl 2.0", "$1,100", "37.0\" (7i)", "D1", "10-25 HCP", "Mid-High", "Neutral", "Moderate", "✓"],
    ["Titleist", "2023", "T200 (2023)", "Players Distance", "Forged Face / Max Impact", "21/24/27/30.5/34.5/39/43", "30.5° / 63.0°", "7.5mm / 81mm", "Satin Chrome", "$1,399", "37.0\" (7i)", "D2", "5-15 HCP", "Mid-Low", "Neutral", "Slight", "✓"],
    ["Titleist", "2021", "T100 (2021)", "Tour Player", "Forged 1025 / Dual Cavity", "24/27/30/34/38/42/46", "34.0° / 63.0°", "5.0mm / 74mm", "Satin Chrome", "$1,299", "37.0\" (7i)", "D3", "0-5 HCP", "High", "Neutral", "Minimal", "✓"],
    ["Titleist", "2021", "T200 (2021)", "Players Distance", "Forged Face / Max Impact", "21/24/27/30.5/34.5/39/43", "30.5° / 63.0°", "7.5mm / 81mm", "Satin Chrome", "$1,299", "37.0\" (7i)", "D2", "5-15 HCP", "Mid-Low", "Neutral", "Slight", "✓"],
    ["TaylorMade", "2021", "P790 (2021)", "Players Distance", "8620 Carbon / SpeedFoam", "21/23.5/26.5/30.5/35/40/45", "30.5° / 62.5°", "7.2mm / 79mm", "Satin Chrome", "$1,299", "37.0\" (7i)", "D2", "5-15 HCP", "Mid-Low", "Neutral", "Slight", "✓"],
    ["Callaway", "2020", "Mavrik Irons", "Game Improv.", "Cast / Flash Face Cup", "21/24/27/30/34/38/43", "27.0° / 62.0°", "8.5mm / 82mm", "Chrome", "$899", "37.0\" (7i)", "D2", "10-25 HCP", "Mid", "Neutral", "Moderate", "✓"]
]

wedges_data = [
    ["Titleist", "Vokey SM9", "Tour Wedge", "46-62", "04-14", "F, M, S, D, K, T, L", "Cast Carbon / Spin Milled", "Tour Chrome, Brushed Steel, Jet Black", "$179", "35.25\"", "D3-D5", "Max", "Zero", "✓"],
    ["Titleist", "Vokey SM8", "Tour Wedge", "46-62", "04-14", "F, M, S, D, K, L", "Cast Carbon / Spin Milled", "Tour Chrome, Brushed Steel, Jet Black", "$159", "35.25\"", "D3-D5", "Max", "Zero", "✓"],
    ["Callaway", "Jaws Raw", "Tour Wedge", "48-60", "08-12", "S, W, C, X, Z", "Carbon Steel / Raw Face", "Raw, Chrome", "$179", "35.25\"", "D3-D4", "Max", "Zero", "✓"],
    ["Callaway", "Jaws MD5", "Tour Wedge", "46-64", "08-12", "S, W, C, X", "Carbon Steel / Groove-in-Groove", "Platinum Chrome, Tour Grey", "$159", "35.25\"", "D3-D4", "Max", "Zero", "✓"],
    ["TaylorMade", "Milled Grind 3", "Tour Wedge", "46-60", "08-12", "Standard, Low, High, TW", "Cast Carbon / Micro-Ribs", "Satin Chrome, Black", "$179", "35.25\"", "D3-D5", "Max", "Zero", "✓"],
    ["PING", "Glide 4.0", "Specialty Wedge", "46-60", "06-14", "S, W, T, E", "8620 Carbon / Emery Blast", "Hydropearl 2.0", "$169", "35.25\"", "D3-D4", "Max", "Zero", "✓"],
    ["Cleveland", "RTX ZipCore", "Tour Wedge", "46-60", "06-12", "Low, Mid, Full", "8620 Carbon / UltiZip", "Tour Satin, Black Satin", "$149", "35.25\"", "D3-D5", "Max", "Zero", "✓"]
]

def append_to_csv(filename, data_to_append):
    filepath = os.path.join("infrastructure", "Data", filename)
    with open(filepath, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(data_to_append)

print("Appending to Drivers...")
append_to_csv("Golf Comparison - Drivers.csv", drivers_data)

print("Appending to Fairways...")
append_to_csv("Golf Comparison - Fairway.csv", fairways_data)

print("Appending to Irons...")
append_to_csv("Golf Comparison - Irons.csv", irons_data)

print("Appending to Wedges...")
append_to_csv("Golf Comparison - Wedges.csv", wedges_data)

print("Done appending historical data!")
