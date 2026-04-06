-- Update script: Adding Miura, XXIO, Wilson, and Honma to the database

-- Miura Irons (2024/2025)
INSERT INTO "Irons" ("Manufacturer", "Year", "Model", "Category", "Head Material (Body/Face)", "Loft Array (4-PW)", "7i Loft / Lie", "Topline / Blade (7i)", "Finish Options", "Price (7pc)", "Stock Length", "Swing Weight", "Target Player Profile", "Spin Profile", "Bias", "Offset", "Left Handed") VALUES 
('Miura', '2024', 'CB-302', 'Players Cavity', 'Forged Premium S20C Soft Carbon', '23/26/29/33/37/41/45', '33.0° / 61.5°', 'Thin', 'Satin Chrome', '$2,200', '37.0" (7i)', 'D2', '0-10 HCP', 'Mid', 'Neutral', 'Slight', '✓'),
('Miura', '2024', 'KM-700', 'Tour Blade', 'Forged Premium S20C Soft Carbon', '24/27/30/34/38/42/46', '34.0° / 61.5°', 'Thin', 'Satin Chrome', '$2,400', '37.0" (7i)', 'D3', '0-5 HCP', 'High', 'Neutral', 'Minimal', '✓'),
('Miura', '2024', 'MC-502', 'Muscle Cavity', 'Forged Premium S20C Soft Carbon', '24/27/30/34/38/42/46', '34.0° / 61.5°', 'Thin', 'Satin Chrome', '$2,200', '37.0" (7i)', 'D3', '0-5 HCP', 'High', 'Neutral', 'Minimal', '✓'),
('Miura', '2025', 'PI-401', 'Players Distance', 'Cast 8620 Body / Maraging Face', '20/22.5/25/28/32/37/42', '28.0° / 61.5°', 'Medium', 'Satin Chrome', '$2,400', '37.0" (7i)', 'D1', '5-15 HCP', 'Mid', 'Neutral', 'Moderate', 'No');

-- XXIO Drivers (2024/2025)
INSERT INTO "Drivers" ("Manufacturer", "Release Year", "Model Name", "Category", "CC", "Standard Loft", "Face Material", "Adjustability", "Weight System", "Weight Range", "Cost (MSRP)", "Stock Length", "Swing Weight", "Target Player Profile", "Spin Profile", "Bias", "Offset", "Left Handed") VALUES 
('XXIO', '2024', 'XXIO 13', 'Ultra-Lightweight', '460', '9.5, 10.5, 11.5', 'Super-TIX 51AF Titanium', 'Fixed', 'ActivWing Technology', 'Fixed', '$699', '45.75"', 'D3 (Light)', '15+ HCP (Slow Swing)', 'High', 'Draw Bias', 'Slight', '✓'),
('XXIO', '2024', 'XXIO X (Eks)', 'Lightweight Players', '460', '9.5, 10.5', 'Super-TIX 51AF Titanium', 'Fixed', 'ActivWing Technology', 'Fixed', '$699', '45.5"', 'D4 (Light)', '5-15 HCP', 'Mid', 'Neutral', 'None', '✓'),
('XXIO', '2025', 'XXIO Prime', 'Premium Lightweight', '460', '10.5, 11.5', 'Super-TIX 51AF Titanium', 'Fixed', 'Rebound Frame', 'Fixed', '$899', '46.25"', 'D2 (Light)', 'Senior/Slow Swing', 'High', 'Draw Bias', 'Moderate', 'No');

-- XXIO Fairways
INSERT INTO "Fairways" ("Manufacturer", "Year", "Model Name", "Release Year", "Category", "CC", "Standard Loft", "Face Material", "Adjustability", "Weight System", "Weight Range", "Cost (MSRP)", "Stock Length", "Swing Weight", "Target Player Profile", "Spin Profile", "Bias", "Offset", "Left Handed") VALUES 
('XXIO', '2024', 'XXIO 13', '2024', 'Ultra-Lightweight', '180', '15, 18, 20', 'HT1770M Steel', 'Fixed', 'ActivWing Technology', 'Fixed', '$399', '43.25"', 'D3', '15+ HCP (Slow Swing)', 'High', 'Draw Bias', 'Slight', '✓'),
('XXIO', '2024', 'XXIO X (Eks)', '2024', 'Lightweight Players', '175', '15, 18', 'HT1770M Steel', 'Fixed', 'ActivWing Technology', 'Fixed', '$399', '43.0"', 'D3', '5-15 HCP', 'Mid', 'Neutral', 'None', '✓');

-- XXIO Irons
INSERT INTO "Irons" ("Manufacturer", "Year", "Model", "Category", "Head Material (Body/Face)", "Loft Array (4-PW)", "7i Loft / Lie", "Topline / Blade (7i)", "Finish Options", "Price (7pc)", "Stock Length", "Swing Weight", "Target Player Profile", "Spin Profile", "Bias", "Offset", "Left Handed") VALUES 
('XXIO', '2024', 'XXIO 13', 'Game Improv.', 'SUS630 Body / Super-TIX 51AF Face', '22/25/28/31/35/39/44', '28.0° / 62.5°', 'Thick', 'Chrome', '$1,399', '37.0" (7i)', 'C8', '15+ HCP', 'High Launch', 'Draw Bias', 'Moderate', '✓'),
('XXIO', '2024', 'XXIO X (Eks)', 'Players Distance', 'Soft Iron Forged / High Strength Steel', '23/26/29/33/37/41/46', '29.0° / 62.0°', 'Medium', 'Chrome', '$1,399', '37.0" (7i)', 'D0', '5-15 HCP', 'Mid-High', 'Neutral', 'Slight', '✓');

-- Wilson Drivers
INSERT INTO "Drivers" ("Manufacturer", "Release Year", "Model Name", "Category", "CC", "Standard Loft", "Face Material", "Adjustability", "Weight System", "Weight Range", "Cost (MSRP)", "Stock Length", "Swing Weight", "Target Player Profile", "Spin Profile", "Bias", "Offset", "Left Handed") VALUES 
('Wilson', '2024', 'Dynapower Carbon', 'Performance Speed', '460', '9, 10.5, 12', 'PKR2 Dynamic Face', '+/- 1.5', 'Carbon Panels / CG Weight', 'Fixed', '$499', '45.75"', 'D3', '5-15 HCP', 'Mid-Low', 'Neutral', 'None', '✓'),
('Wilson', '2024', 'Dynapower Titanium', 'Maximum Forgiveness', '460', '9, 10.5, 13', 'PKR2 Titanium Face', '+/- 1.5', 'Titanium Rear Weight', 'Fixed', '$429', '45.75"', 'D2', '12+ HCP', 'Mid-High', 'Draw Bias', 'Slight', '✓');

-- Wilson Irons
INSERT INTO "Irons" ("Manufacturer", "Year", "Model", "Category", "Head Material (Body/Face)", "Loft Array (4-PW)", "7i Loft / Lie", "Topline / Blade (7i)", "Finish Options", "Price (7pc)", "Stock Length", "Swing Weight", "Target Player Profile", "Spin Profile", "Bias", "Offset", "Left Handed") VALUES 
('Wilson', '2024', 'Staff Model Blade', 'Tour Blade', 'Forged 8620 Carbon Steel', '24/27/30/34/38/42/46', '34.0° / 62.0°', 'Thin', 'Chrome/Raw', '$1,199', '37.0" (7i)', 'D3', '0-3 HCP', 'High', 'Neutral', 'Minimal', '✓'),
('Wilson', '2024', 'Staff Model CB', 'Tour Cavity', 'Forged 8620 Carbon Steel', '24/27/30/34/38/42/46', '34.0° / 62.0°', 'Thin', 'Chrome', '$1,199', '37.0" (7i)', 'D3', '0-8 HCP', 'Mid-High', 'Neutral', 'Minimal', '✓'),
('Wilson', '2024', 'Dynapower Forged', 'Players Distance', 'Forged 8620 / Power Hole Tech', '21/24/27/30.5/34.5/39/44', '30.5° / 62.0°', 'Medium', 'Chrome', '$999', '37.0" (7i)', 'D2', '5-15 HCP', 'Mid', 'Neutral', 'Slight', '✓'),
('Wilson', '2024', 'Dynapower', 'Game Improv.', '17-4 Stainless Steel', '18/21/24/27/31.5/36/41', '27.0° / 62.5°', 'Thick', 'Chrome', '$799', '37.0" (7i)', 'D1', '15+ HCP', 'Low-Mid', 'Draw Bias', 'Moderate', '✓');

-- Honma Drivers
INSERT INTO "Drivers" ("Manufacturer", "Release Year", "Model Name", "Category", "CC", "Standard Loft", "Face Material", "Adjustability", "Weight System", "Weight Range", "Cost (MSRP)", "Stock Length", "Swing Weight", "Target Player Profile", "Spin Profile", "Bias", "Offset", "Left Handed") VALUES 
('Honma', '2024', 'TW757 S', 'Low Spin Performance', '450', '9, 10.5', 'Carbon Slot Titanium', '+/- 1.5', 'Adjustable Weights', 'Adjustable', '$715', '45.25"', 'D2', '0-10 HCP', 'Low', 'Neutral/Fade', 'None', '✓'),
('Honma', '2024', 'TW757 D', 'Forgiving Distance', '460', '9, 10.5', 'Carbon Slot Titanium', '+/- 1.5', 'Adjustable Weights', 'Adjustable', '$715', '45.25"', 'D2', 'All Skill Levels', 'Mid', 'Draw Bias', 'None', '✓');

-- Honma Irons
INSERT INTO "Irons" ("Manufacturer", "Year", "Model", "Category", "Head Material (Body/Face)", "Loft Array (4-PW)", "7i Loft / Lie", "Topline / Blade (7i)", "Finish Options", "Price (7pc)", "Stock Length", "Swing Weight", "Target Player Profile", "Spin Profile", "Bias", "Offset", "Left Handed") VALUES 
('Honma', '2024', 'TW757 B', 'Tour Blade', 'S20C Premium Forged', '24/27/30/34/38/42/46', '34.0° / 61.5°', 'Thin', 'Satin Chrome', '$1,275', '37.0" (7i)', 'D2', '0-5 HCP', 'High', 'Neutral', 'Minimal', '✓'),
('Honma', '2024', 'TW757 Vx', 'Players Cavity', 'S20C Forged', '22/24/27/30/34/38/43', '30.0° / 61.5°', 'Medium', 'Satin Chrome', '$1,275', '37.0" (7i)', 'D2', '0-10 HCP', 'Mid', 'Neutral', 'Slight', '✓'),
('Honma', '2024', 'TW757 P', 'Players Distance', 'S35C Undercut / Maraging Face', '20/22.5/25/28.5/33/38/43', '28.5° / 61.5°', 'Medium-Thick', 'Satin Chrome', '$1,275', '37.0" (7i)', 'D1', '5-15 HCP', 'Mid', 'Neutral', 'Moderate', '✓');
