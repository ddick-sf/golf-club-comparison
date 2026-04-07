-- Create Table for Hybrids
CREATE TABLE IF NOT EXISTS "Hybrids" (
    id SERIAL PRIMARY KEY,
    "Manufacturer" TEXT,
    "Release Year" TEXT,
    "Model Name" TEXT,
    "Category" TEXT,
    "Standard Loft" TEXT,
    "Face Material" TEXT,
    "Adjustability" TEXT,
    "Length" TEXT,
    "Swing Weight" TEXT,
    "Target Player Profile" TEXT,
    "Bias" TEXT,
    "Cost" TEXT,
    "Left Handed" TEXT
);

ALTER TABLE "Hybrids" ENABLE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS "Public Select" ON "Hybrids";
CREATE POLICY "Public Select" ON "Hybrids" FOR SELECT USING (true);

TRUNCATE TABLE "Hybrids";

INSERT INTO "Hybrids" ("Manufacturer", "Release Year", "Model Name", "Category", "Standard Loft", "Face Material", "Adjustability", "Length", "Swing Weight", "Target Player Profile", "Bias", "Cost", "Left Handed") VALUES 
('Titleist', '2024', 'TSR2 Hybrid', 'Versatile Hybrid', '19, 22', 'Maraging Steel', '+/- 1.5', '40.25"', 'D2', 'All Skill Levels', 'Neutral', '$250', 'Yes'),
('Titleist', '2023', 'T200 Utility', 'Driving Iron', '18, 20', 'Forged', 'Fixed', '39.5"', 'D2', 'Low-Mid HCP', 'Neutral', '$250', 'Yes'),
('Titleist', '2022', 'TSR3 Hybrid', 'Versatile Hybrid', '19, 22', 'Maraging Steel', '+/- 1.5', '40.25"', 'D2', 'All Skill Levels', 'Neutral', '$250', 'Yes'),
('Titleist', '2021', 'TSi2 Hybrid', 'Versatile Hybrid', '19, 22', 'Maraging Steel', '+/- 1.5', '40.25"', 'D2', 'All Skill Levels', 'Neutral', '$250', 'Yes'),
('TaylorMade', '2024', 'Qi10 Rescue', 'Versatile Hybrid', '19, 22', 'Maraging Steel', '+/- 1.5', '40.25"', 'D2', 'All Skill Levels', 'Neutral', '$250', 'Yes'),
('TaylorMade', '2024', 'P DHY', 'Driving Iron', '18, 20', 'Forged', 'Fixed', '39.5"', 'D2', 'Low-Mid HCP', 'Neutral', '$250', 'Yes'),
('TaylorMade', '2023', 'Stealth 2 Rescue', 'Versatile Hybrid', '19, 22', 'Maraging Steel', '+/- 1.5', '40.25"', 'D2', 'All Skill Levels', 'Neutral', '$250', 'Yes'),
('TaylorMade', '2023', 'Stealth UDI', 'Driving Iron', '18, 20', 'Forged', 'Fixed', '39.5"', 'D2', 'Low-Mid HCP', 'Neutral', '$250', 'Yes'),
('TaylorMade', '2022', 'Stealth Rescue', 'Versatile Hybrid', '19, 22', 'Maraging Steel', '+/- 1.5', '40.25"', 'D2', 'All Skill Levels', 'Neutral', '$250', 'Yes'),
('TaylorMade', '2020', 'SIM Max Rescue', 'Versatile Hybrid', '19, 22', 'Maraging Steel', '+/- 1.5', '40.25"', 'D2', 'All Skill Levels', 'Neutral', '$250', 'Yes'),
('Srixon', '2023', 'ZX Mk II Hybrid', 'Versatile Hybrid', '19, 22', 'Maraging Steel', '+/- 1.5', '40.25"', 'D2', 'All Skill Levels', 'Neutral', '$250', 'Yes'),
('Srixon', '2023', 'ZX Mk II Utility', 'Driving Iron', '18, 20', 'Forged', 'Fixed', '39.5"', 'D2', 'Low-Mid HCP', 'Neutral', '$250', 'Yes'),
('Srixon', '2021', 'ZX Hybrid', 'Versatile Hybrid', '19, 22', 'Maraging Steel', '+/- 1.5', '40.25"', 'D2', 'All Skill Levels', 'Neutral', '$250', 'Yes'),
('Srixon', '2021', 'ZX Utility', 'Driving Iron', '18, 20', 'Forged', 'Fixed', '39.5"', 'D2', 'Low-Mid HCP', 'Neutral', '$250', 'Yes'),
('PXG', '2024', 'Black Ops Hybrid', 'Versatile Hybrid', '19, 22', 'Maraging Steel', '+/- 1.5', '40.25"', 'D2', 'All Skill Levels', 'Neutral', '$250', 'Yes'),
('PXG', '2023', '0311 GEN6 Hybrid', 'Versatile Hybrid', '19, 22', 'Maraging Steel', '+/- 1.5', '40.25"', 'D2', 'All Skill Levels', 'Neutral', '$250', 'Yes'),
('PXG', '2023', '0311 X Driving Iron', 'Driving Iron', '18, 20', 'Forged', 'Fixed', '39.5"', 'D2', 'Low-Mid HCP', 'Neutral', '$250', 'Yes'),
('PXG', '2021', '0317 X GEN4', 'Versatile Hybrid', '19, 22', 'Maraging Steel', '+/- 1.5', '40.25"', 'D2', 'All Skill Levels', 'Neutral', '$250', 'Yes'),
('PING', '2024', 'G430 Hybrid', 'Versatile Hybrid', '19, 22', 'Maraging Steel', '+/- 1.5', '40.25"', 'D2', 'All Skill Levels', 'Neutral', '$250', 'Yes'),
('PING', '2024', 'iCrossover', 'Driving Iron', '18, 20', 'Forged', 'Fixed', '39.5"', 'D2', 'Low-Mid HCP', 'Neutral', '$250', 'Yes'),
('PING', '2021', 'G425 Hybrid', 'Versatile Hybrid', '19, 22', 'Maraging Steel', '+/- 1.5', '40.25"', 'D2', 'All Skill Levels', 'Neutral', '$250', 'Yes'),
('Mizuno', '2024', 'ST-MAX 230 Hybrid', 'Versatile Hybrid', '19, 22', 'Maraging Steel', '+/- 1.5', '40.25"', 'D2', 'All Skill Levels', 'Neutral', '$250', 'Yes'),
('Mizuno', '2023', 'CLK Hybrid', 'Versatile Hybrid', '19, 22', 'Maraging Steel', '+/- 1.5', '40.25"', 'D2', 'All Skill Levels', 'Neutral', '$250', 'Yes'),
('Mizuno', '2022', 'Mizuno Pro Fli-Hi', 'Driving Iron', '18, 20', 'Forged', 'Fixed', '39.5"', 'D2', 'Low-Mid HCP', 'Neutral', '$250', 'Yes'),
('Mizuno', '2020', 'CLK Hybrid', 'Versatile Hybrid', '19, 22', 'Maraging Steel', '+/- 1.5', '40.25"', 'D2', 'All Skill Levels', 'Neutral', '$250', 'Yes'),
('Cobra', '2024', 'Darkspeed Hybrid', 'Versatile Hybrid', '19, 22', 'Maraging Steel', '+/- 1.5', '40.25"', 'D2', 'All Skill Levels', 'Neutral', '$250', 'Yes'),
('Cobra', '2023', 'Aerojet Hybrid', 'Versatile Hybrid', '19, 22', 'Maraging Steel', '+/- 1.5', '40.25"', 'D2', 'All Skill Levels', 'Neutral', '$250', 'Yes'),
('Cobra', '2022', 'LTDx Hybrid', 'Versatile Hybrid', '19, 22', 'Maraging Steel', '+/- 1.5', '40.25"', 'D2', 'All Skill Levels', 'Neutral', '$250', 'Yes'),
('Cobra', '2020', 'Speedzone Hybrid', 'Versatile Hybrid', '19, 22', 'Maraging Steel', '+/- 1.5', '40.25"', 'D2', 'All Skill Levels', 'Neutral', '$250', 'Yes'),
('Callaway', '2024', 'Paradym Ai Smoke Hybrid', 'Versatile Hybrid', '19, 22', 'Maraging Steel', '+/- 1.5', '40.25"', 'D2', 'All Skill Levels', 'Neutral', '$250', 'Yes'),
('Callaway', '2024', 'X Forged UT', 'Driving Iron', '18, 20', 'Forged', 'Fixed', '39.5"', 'D2', 'Low-Mid HCP', 'Neutral', '$250', 'Yes'),
('Callaway', '2023', 'Paradym Hybrid', 'Versatile Hybrid', '19, 22', 'Maraging Steel', '+/- 1.5', '40.25"', 'D2', 'All Skill Levels', 'Neutral', '$250', 'Yes'),
('Callaway', '2021', 'Apex UW', 'Versatile Hybrid', '19, 22', 'Maraging Steel', '+/- 1.5', '40.25"', 'D2', 'All Skill Levels', 'Neutral', '$250', 'Yes'),
('Callaway', '2020', 'Mavrik Hybrid', 'Versatile Hybrid', '19, 22', 'Maraging Steel', '+/- 1.5', '40.25"', 'D2', 'All Skill Levels', 'Neutral', '$250', 'Yes');

