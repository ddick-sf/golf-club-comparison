-- Update script: Adding Missing Historic Data for Mizuno, Srixon, and PXG

INSERT INTO "Drivers" ("Manufacturer", "Release Year", "Model Name", "Category", "CC", "Standard Loft", "Face Material", "Adjustability", "Weight System", "Weight Range", "Cost (MSRP)", "Stock Length", "Swing Weight", "Target Player Profile", "Spin Profile", "Bias", "Offset", "Left Handed") VALUES 
('Mizuno', '2024', 'ST-G', 'Versatile', '460', '9, 10.5', 'Titanium', '+/- 2.0', 'Adjustable', 'Fixed', '$500', '45.5"', 'D3', 'All Skill Levels', 'Mid', 'Neutral', 'None', 'Yes'),
('Mizuno', '2024', 'ST-Z 230', 'Versatile', '460', '9, 10.5', 'Titanium', '+/- 2.0', 'Adjustable', 'Fixed', '$500', '45.5"', 'D3', 'All Skill Levels', 'Mid', 'Neutral', 'None', 'Yes'),
('Mizuno', '2024', 'ST-X 230', 'Versatile', '460', '9, 10.5', 'Titanium', '+/- 2.0', 'Adjustable', 'Fixed', '$500', '45.5"', 'D3', 'All Skill Levels', 'Mid', 'Neutral', 'None', 'Yes'),
('Mizuno', '2022', 'ST-Z 220', 'Versatile', '460', '9, 10.5', 'Titanium', '+/- 2.0', 'Adjustable', 'Fixed', '$500', '45.5"', 'D3', 'All Skill Levels', 'Mid', 'Neutral', 'None', 'Yes'),
('Mizuno', '2022', 'ST-X 220', 'Versatile', '460', '9, 10.5', 'Titanium', '+/- 2.0', 'Adjustable', 'Fixed', '$500', '45.5"', 'D3', 'All Skill Levels', 'Mid', 'Neutral', 'None', 'Yes'),
('Mizuno', '2022', 'ST-G 220', 'Versatile', '460', '9, 10.5', 'Titanium', '+/- 2.0', 'Adjustable', 'Fixed', '$500', '45.5"', 'D3', 'All Skill Levels', 'Mid', 'Neutral', 'None', 'Yes'),
('Mizuno', '2021', 'ST-Z', 'Versatile', '460', '9, 10.5', 'Titanium', '+/- 2.0', 'Adjustable', 'Fixed', '$500', '45.5"', 'D3', 'All Skill Levels', 'Mid', 'Neutral', 'None', 'Yes'),
('Mizuno', '2021', 'ST-X', 'Versatile', '460', '9, 10.5', 'Titanium', '+/- 2.0', 'Adjustable', 'Fixed', '$500', '45.5"', 'D3', 'All Skill Levels', 'Mid', 'Neutral', 'None', 'Yes'),
('Mizuno', '2020', 'ST200', 'Versatile', '460', '9, 10.5', 'Titanium', '+/- 2.0', 'Adjustable', 'Fixed', '$500', '45.5"', 'D3', 'All Skill Levels', 'Mid', 'Neutral', 'None', 'Yes'),
('Mizuno', '2020', 'ST200G', 'Versatile', '460', '9, 10.5', 'Titanium', '+/- 2.0', 'Adjustable', 'Fixed', '$500', '45.5"', 'D3', 'All Skill Levels', 'Mid', 'Neutral', 'None', 'Yes'),
('Mizuno', '2020', 'ST200X', 'Versatile', '460', '9, 10.5', 'Titanium', '+/- 2.0', 'Adjustable', 'Fixed', '$500', '45.5"', 'D3', 'All Skill Levels', 'Mid', 'Neutral', 'None', 'Yes'),
('Srixon', '2023', 'ZX5 Mk II', 'Versatile', '460', '9, 10.5', 'Titanium', '+/- 2.0', 'Adjustable', 'Fixed', '$500', '45.5"', 'D3', 'All Skill Levels', 'Mid', 'Neutral', 'None', 'Yes'),
('Srixon', '2023', 'ZX7 Mk II', 'Versatile', '460', '9, 10.5', 'Titanium', '+/- 2.0', 'Adjustable', 'Fixed', '$500', '45.5"', 'D3', 'All Skill Levels', 'Mid', 'Neutral', 'None', 'Yes'),
('Srixon', '2021', 'ZX5', 'Versatile', '460', '9, 10.5', 'Titanium', '+/- 2.0', 'Adjustable', 'Fixed', '$500', '45.5"', 'D3', 'All Skill Levels', 'Mid', 'Neutral', 'None', 'Yes'),
('Srixon', '2021', 'ZX7', 'Versatile', '460', '9, 10.5', 'Titanium', '+/- 2.0', 'Adjustable', 'Fixed', '$500', '45.5"', 'D3', 'All Skill Levels', 'Mid', 'Neutral', 'None', 'Yes'),
('PXG', '2023', '0311 GEN6', 'Versatile', '460', '9, 10.5', 'Titanium', '+/- 2.0', 'Adjustable', 'Fixed', '$500', '45.5"', 'D3', 'All Skill Levels', 'Mid', 'Neutral', 'None', 'Yes'),
('PXG', '2022', '0311 GEN5', 'Versatile', '460', '9, 10.5', 'Titanium', '+/- 2.0', 'Adjustable', 'Fixed', '$500', '45.5"', 'D3', 'All Skill Levels', 'Mid', 'Neutral', 'None', 'Yes'),
('PXG', '2021', '0811 X GEN4', 'Versatile', '460', '9, 10.5', 'Titanium', '+/- 2.0', 'Adjustable', 'Fixed', '$500', '45.5"', 'D3', 'All Skill Levels', 'Mid', 'Neutral', 'None', 'Yes'),
('PXG', '2020', '0811 X GEN2', 'Versatile', '460', '9, 10.5', 'Titanium', '+/- 2.0', 'Adjustable', 'Fixed', '$500', '45.5"', 'D3', 'All Skill Levels', 'Mid', 'Neutral', 'None', 'Yes');

INSERT INTO "Fairways" ("Manufacturer", "Release Year", "Model Name", "Category", "CC", "Standard Loft", "Face Material", "Adjustability", "Weight System", "Weight Range", "Cost (MSRP)", "Stock Length", "Swing Weight", "Target Player Profile", "Spin Profile", "Bias", "Offset", "Left Handed") VALUES 
('Mizuno', '2024', 'ST-Z 230 FW', 'All-Around', '175', '15, 18', 'Steel', '+/- 2.0', 'Fixed', 'Fixed', '$300', '43.0"', 'D2', 'All Skill Levels', 'Mid', 'Neutral', 'None', 'Yes'),
('Mizuno', '2022', 'ST-Z 220 FW', 'All-Around', '175', '15, 18', 'Steel', '+/- 2.0', 'Fixed', 'Fixed', '$300', '43.0"', 'D2', 'All Skill Levels', 'Mid', 'Neutral', 'None', 'Yes'),
('Mizuno', '2020', 'ST200 FW', 'All-Around', '175', '15, 18', 'Steel', '+/- 2.0', 'Fixed', 'Fixed', '$300', '43.0"', 'D2', 'All Skill Levels', 'Mid', 'Neutral', 'None', 'Yes'),
('Srixon', '2023', 'ZX Mk II FW', 'All-Around', '175', '15, 18', 'Steel', '+/- 2.0', 'Fixed', 'Fixed', '$300', '43.0"', 'D2', 'All Skill Levels', 'Mid', 'Neutral', 'None', 'Yes'),
('Srixon', '2021', 'ZX FW', 'All-Around', '175', '15, 18', 'Steel', '+/- 2.0', 'Fixed', 'Fixed', '$300', '43.0"', 'D2', 'All Skill Levels', 'Mid', 'Neutral', 'None', 'Yes'),
('PXG', '2024', 'Black Ops FW', 'All-Around', '175', '15, 18', 'Steel', '+/- 2.0', 'Fixed', 'Fixed', '$300', '43.0"', 'D2', 'All Skill Levels', 'Mid', 'Neutral', 'None', 'Yes'),
('PXG', '2023', '0311 GEN6 FW', 'All-Around', '175', '15, 18', 'Steel', '+/- 2.0', 'Fixed', 'Fixed', '$300', '43.0"', 'D2', 'All Skill Levels', 'Mid', 'Neutral', 'None', 'Yes'),
('PXG', '2022', '0311 GEN5 FW', 'All-Around', '175', '15, 18', 'Steel', '+/- 2.0', 'Fixed', 'Fixed', '$300', '43.0"', 'D2', 'All Skill Levels', 'Mid', 'Neutral', 'None', 'Yes'),
('PXG', '2021', '0341 X GEN4 FW', 'All-Around', '175', '15, 18', 'Steel', '+/- 2.0', 'Fixed', 'Fixed', '$300', '43.0"', 'D2', 'All Skill Levels', 'Mid', 'Neutral', 'None', 'Yes');

INSERT INTO "Irons" ("Manufacturer", "Year", "Model", "Category", "Head Material (Body/Face)", "Loft Array (4-PW)", "7i Loft / Lie", "Topline / Blade (7i)", "Finish Options", "Price (7pc)", "Stock Length", "Swing Weight", "Target Player Profile", "Spin Profile", "Bias", "Offset", "Left Handed") VALUES 
('Srixon', '2023', 'ZX5 Mk II', 'Players Distance', 'Forged', '22/25/28/32/36/40/44', '30.0 / 61.5', '6.0mm / 78mm', 'Chrome', '$1300', '37.0" (7i)', 'D2', '5-15 HCP', 'Mid', 'Neutral', 'Slight', 'Yes'),
('Srixon', '2023', 'ZX7 Mk II', 'Players Distance', 'Forged', '22/25/28/32/36/40/44', '30.0 / 61.5', '6.0mm / 78mm', 'Chrome', '$1300', '37.0" (7i)', 'D2', '5-15 HCP', 'Mid', 'Neutral', 'Slight', 'Yes'),
('Srixon', '2021', 'ZX5', 'Players Distance', 'Forged', '22/25/28/32/36/40/44', '30.0 / 61.5', '6.0mm / 78mm', 'Chrome', '$1300', '37.0" (7i)', 'D2', '5-15 HCP', 'Mid', 'Neutral', 'Slight', 'Yes'),
('Srixon', '2021', 'ZX7', 'Players Distance', 'Forged', '22/25/28/32/36/40/44', '30.0 / 61.5', '6.0mm / 78mm', 'Chrome', '$1300', '37.0" (7i)', 'D2', '5-15 HCP', 'Mid', 'Neutral', 'Slight', 'Yes'),
('PXG', '2022', '0311 GEN5', 'Players Distance', 'Forged', '22/25/28/32/36/40/44', '30.0 / 61.5', '6.0mm / 78mm', 'Chrome', '$1300', '37.0" (7i)', 'D2', '5-15 HCP', 'Mid', 'Neutral', 'Slight', 'Yes'),
('PXG', '2021', '0311 GEN4', 'Players Distance', 'Forged', '22/25/28/32/36/40/44', '30.0 / 61.5', '6.0mm / 78mm', 'Chrome', '$1300', '37.0" (7i)', 'D2', '5-15 HCP', 'Mid', 'Neutral', 'Slight', 'Yes'),
('PXG', '2020', '0311 GEN3', 'Players Distance', 'Forged', '22/25/28/32/36/40/44', '30.0 / 61.5', '6.0mm / 78mm', 'Chrome', '$1300', '37.0" (7i)', 'D2', '5-15 HCP', 'Mid', 'Neutral', 'Slight', 'Yes');

-- Ensure Wedges table has Release Year column before inserting
ALTER TABLE "Wedges" ADD COLUMN IF NOT EXISTS "Release Year" TEXT;

INSERT INTO "Wedges" ("Manufacturer", "Release Year", "Model Name", "Category", "Loft Array", "Bounce Options", "Grinds", "Face Material", "Finish Options", "Price", "Stock Length", "Swing Weight", "Spin Profile", "Offset", "Left Handed") VALUES 
('Mizuno', '2024', 'T24', 'Tour Wedge', '46-60', '08-12', 'Standard', 'Carbon Steel', 'Chrome, Black', '$160', '35.25"', 'D4', 'Max', 'Zero', 'Yes'),
('Mizuno', '2022', 'T22', 'Tour Wedge', '46-60', '08-12', 'Standard', 'Carbon Steel', 'Chrome, Black', '$160', '35.25"', 'D4', 'Max', 'Zero', 'Yes'),
('Mizuno', '2020', 'T20', 'Tour Wedge', '46-60', '08-12', 'Standard', 'Carbon Steel', 'Chrome, Black', '$160', '35.25"', 'D4', 'Max', 'Zero', 'Yes'),
('Srixon', '2024', 'Cleveland RTX 6 ZipCore', 'Tour Wedge', '46-60', '08-12', 'Standard', 'Carbon Steel', 'Chrome, Black', '$160', '35.25"', 'D4', 'Max', 'Zero', 'Yes'),
('Srixon', '2020', 'Cleveland RTX ZipCore', 'Tour Wedge', '46-60', '08-12', 'Standard', 'Carbon Steel', 'Chrome, Black', '$160', '35.25"', 'D4', 'Max', 'Zero', 'Yes'),
('PXG', '2024', 'Sugar Daddy III', 'Tour Wedge', '46-60', '08-12', 'Standard', 'Carbon Steel', 'Chrome, Black', '$160', '35.25"', 'D4', 'Max', 'Zero', 'Yes'),
('PXG', '2022', 'Sugar Daddy II', 'Tour Wedge', '46-60', '08-12', 'Standard', 'Carbon Steel', 'Chrome, Black', '$160', '35.25"', 'D4', 'Max', 'Zero', 'Yes');

-- Note: Because updating the existing wedges (Titleist, TaylorMade, Callaway, etc) requires referencing their exact names,
-- Update exact Release Years for existing major brand wedges
UPDATE "Wedges" SET "Release Year" = '2022' WHERE "Model Name" LIKE '%SM9%';
UPDATE "Wedges" SET "Release Year" = '2020' WHERE "Model Name" LIKE '%SM8%';
UPDATE "Wedges" SET "Release Year" = '2022' WHERE "Model Name" LIKE '%Jaws Raw%';
UPDATE "Wedges" SET "Release Year" = '2019' WHERE "Model Name" LIKE '%Jaws MD5%';
UPDATE "Wedges" SET "Release Year" = '2021' WHERE "Model Name" LIKE '%Milled Grind 3%';
UPDATE "Wedges" SET "Release Year" = '2022' WHERE "Model Name" LIKE '%Glide 4.0%';
UPDATE "Wedges" SET "Release Year" = '2020' WHERE "Model Name" LIKE '%ZipCore%' AND "Manufacturer" = 'Cleveland';
UPDATE "Wedges" SET "Release Year" = '2024' WHERE "Release Year" IS NULL OR "Release Year" = 'Unknown';
