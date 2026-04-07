-- Create Table for Wedges
CREATE TABLE IF NOT EXISTS "Wedges" (
    id SERIAL PRIMARY KEY,
    "Manufacturer" TEXT,
    "Release Year" TEXT,
    "Model Name" TEXT,
    "Category" TEXT,
    "Loft Array" TEXT,
    "Bounce Options" TEXT,
    "Grinds" TEXT,
    "Face Material" TEXT,
    "Finish Options" TEXT,
    "Price" TEXT,
    "Stock Length" TEXT,
    "Swing Weight" TEXT,
    "Spin Profile" TEXT,
    "Offset" TEXT,
    "Left Handed" TEXT
);

ALTER TABLE "Wedges" ENABLE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS "Public Select" ON "Wedges";
CREATE POLICY "Public Select" ON "Wedges" FOR SELECT USING (true);

TRUNCATE TABLE "Wedges";

INSERT INTO "Wedges" ("Manufacturer", "Release Year", "Model Name", "Category", "Loft Array", "Bounce Options", "Grinds", "Face Material", "Finish Options", "Price", "Stock Length", "Swing Weight", "Spin Profile", "Offset", "Left Handed") VALUES 
('Titleist', '2024', 'Vokey SM10', 'Tour Wedge', '46-60', '08-12', 'Standard, Low, High', 'Carbon Steel', 'Chrome, Black, Raw', '$160', '35.25"', 'D4', 'Max', 'Zero', 'Yes'),
('Titleist', '2024', 'Vokey SM11', 'Tour Wedge', '46-60', '08-12', 'Standard, Low, High', 'Carbon Steel', 'Chrome, Black, Raw', '$160', '35.25"', 'D4', 'Max', 'Zero', 'Yes'),
('Titleist', '2022', 'Vokey SM9', 'Tour Wedge', '46-60', '08-12', 'Standard, Low, High', 'Carbon Steel', 'Chrome, Black, Raw', '$160', '35.25"', 'D4', 'Max', 'Zero', 'Yes'),
('Titleist', '2020', 'Vokey SM8', 'Tour Wedge', '46-60', '08-12', 'Standard, Low, High', 'Carbon Steel', 'Chrome, Black, Raw', '$160', '35.25"', 'D4', 'Max', 'Zero', 'Yes'),
('TaylorMade', '2024', 'Milled Grind 5', 'Tour Wedge', '46-60', '08-12', 'Standard, Low, High', 'Carbon Steel', 'Chrome, Black, Raw', '$160', '35.25"', 'D4', 'Max', 'Zero', 'Yes'),
('TaylorMade', '2023', 'Milled Grind 4', 'Tour Wedge', '46-60', '08-12', 'Standard, Low, High', 'Carbon Steel', 'Chrome, Black, Raw', '$160', '35.25"', 'D4', 'Max', 'Zero', 'Yes'),
('TaylorMade', '2022', 'Hi-Toe 3', 'Tour Wedge', '46-60', '08-12', 'Standard, Low, High', 'Carbon Steel', 'Chrome, Black, Raw', '$160', '35.25"', 'D4', 'Max', 'Zero', 'Yes'),
('TaylorMade', '2021', 'Milled Grind 3', 'Tour Wedge', '46-60', '08-12', 'Standard, Low, High', 'Carbon Steel', 'Chrome, Black, Raw', '$160', '35.25"', 'D4', 'Max', 'Zero', 'Yes'),
('TaylorMade', '2021', 'Hi-Toe RAW', 'Tour Wedge', '46-60', '08-12', 'Standard, Low, High', 'Carbon Steel', 'Chrome, Black, Raw', '$160', '35.25"', 'D4', 'Max', 'Zero', 'Yes'),
('PXG', '2024', 'Sugar Daddy III', 'Tour Wedge', '46-60', '08-12', 'Standard, Low, High', 'Carbon Steel', 'Chrome, Black, Raw', '$160', '35.25"', 'D4', 'Max', 'Zero', 'Yes'),
('PXG', '2022', 'Sugar Daddy II', 'Tour Wedge', '46-60', '08-12', 'Standard, Low, High', 'Carbon Steel', 'Chrome, Black, Raw', '$160', '35.25"', 'D4', 'Max', 'Zero', 'Yes'),
('PXG', '2021', '0311 Forged', 'Tour Wedge', '46-60', '08-12', 'Standard, Low, High', 'Carbon Steel', 'Chrome, Black, Raw', '$160', '35.25"', 'D4', 'Max', 'Zero', 'Yes'),
('PING', '2024', 's159', 'Tour Wedge', '46-60', '08-12', 'Standard, Low, High', 'Carbon Steel', 'Chrome, Black, Raw', '$160', '35.25"', 'D4', 'Max', 'Zero', 'Yes'),
('PING', '2022', 'Glide 4.0', 'Tour Wedge', '46-60', '08-12', 'Standard, Low, High', 'Carbon Steel', 'Chrome, Black, Raw', '$160', '35.25"', 'D4', 'Max', 'Zero', 'Yes'),
('PING', '2021', 'Glide Forged Pro', 'Tour Wedge', '46-60', '08-12', 'Standard, Low, High', 'Carbon Steel', 'Chrome, Black, Raw', '$160', '35.25"', 'D4', 'Max', 'Zero', 'Yes'),
('PING', '2019', 'Glide 3.0', 'Tour Wedge', '46-60', '08-12', 'Standard, Low, High', 'Carbon Steel', 'Chrome, Black, Raw', '$160', '35.25"', 'D4', 'Max', 'Zero', 'Yes'),
('Mizuno', '2024', 'T24', 'Tour Wedge', '46-60', '08-12', 'Standard, Low, High', 'Carbon Steel', 'Chrome, Black, Raw', '$160', '35.25"', 'D4', 'Max', 'Zero', 'Yes'),
('Mizuno', '2023', 'S23', 'Tour Wedge', '46-60', '08-12', 'Standard, Low, High', 'Carbon Steel', 'Chrome, Black, Raw', '$160', '35.25"', 'D4', 'Max', 'Zero', 'Yes'),
('Mizuno', '2022', 'T22', 'Tour Wedge', '46-60', '08-12', 'Standard, Low, High', 'Carbon Steel', 'Chrome, Black, Raw', '$160', '35.25"', 'D4', 'Max', 'Zero', 'Yes'),
('Mizuno', '2020', 'T20', 'Tour Wedge', '46-60', '08-12', 'Standard, Low, High', 'Carbon Steel', 'Chrome, Black, Raw', '$160', '35.25"', 'D4', 'Max', 'Zero', 'Yes'),
('Cobra', '2023', 'Snakebite', 'Tour Wedge', '46-60', '08-12', 'Standard, Low, High', 'Carbon Steel', 'Chrome, Black, Raw', '$160', '35.25"', 'D4', 'Max', 'Zero', 'Yes'),
('Cobra', '2023', 'Snakebite-X', 'Tour Wedge', '46-60', '08-12', 'Standard, Low, High', 'Carbon Steel', 'Chrome, Black, Raw', '$160', '35.25"', 'D4', 'Max', 'Zero', 'Yes'),
('Cobra', '2021', 'King MIM', 'Tour Wedge', '46-60', '08-12', 'Standard, Low, High', 'Carbon Steel', 'Chrome, Black, Raw', '$160', '35.25"', 'D4', 'Max', 'Zero', 'Yes'),
('Cleveland', '2024', 'RTX 6 ZipCore', 'Tour Wedge', '46-60', '08-12', 'Standard, Low, High', 'Carbon Steel', 'Chrome, Black, Raw', '$160', '35.25"', 'D4', 'Max', 'Zero', 'Yes'),
('Cleveland', '2024', 'CBX 4 ZipCore', 'Tour Wedge', '46-60', '08-12', 'Standard, Low, High', 'Carbon Steel', 'Chrome, Black, Raw', '$160', '35.25"', 'D4', 'Max', 'Zero', 'Yes'),
('Cleveland', '2022', 'RTX 6', 'Tour Wedge', '46-60', '08-12', 'Standard, Low, High', 'Carbon Steel', 'Chrome, Black, Raw', '$160', '35.25"', 'D4', 'Max', 'Zero', 'Yes'),
('Cleveland', '2022', 'CBX ZipCore', 'Tour Wedge', '46-60', '08-12', 'Standard, Low, High', 'Carbon Steel', 'Chrome, Black, Raw', '$160', '35.25"', 'D4', 'Max', 'Zero', 'Yes'),
('Cleveland', '2020', 'RTX ZipCore', 'Tour Wedge', '46-60', '08-12', 'Standard, Low, High', 'Carbon Steel', 'Chrome, Black, Raw', '$160', '35.25"', 'D4', 'Max', 'Zero', 'Yes'),
('Cleveland', '2020', 'CBX 2', 'Tour Wedge', '46-60', '08-12', 'Standard, Low, High', 'Carbon Steel', 'Chrome, Black, Raw', '$160', '35.25"', 'D4', 'Max', 'Zero', 'Yes'),
('Callaway', '2024', 'Opus', 'Tour Wedge', '46-60', '08-12', 'Standard, Low, High', 'Carbon Steel', 'Chrome, Black, Raw', '$160', '35.25"', 'D4', 'Max', 'Zero', 'Yes'),
('Callaway', '2022', 'Jaws Raw', 'Tour Wedge', '46-60', '08-12', 'Standard, Low, High', 'Carbon Steel', 'Chrome, Black, Raw', '$160', '35.25"', 'D4', 'Max', 'Zero', 'Yes'),
('Callaway', '2021', 'Jaws Full Toe', 'Tour Wedge', '46-60', '08-12', 'Standard, Low, High', 'Carbon Steel', 'Chrome, Black, Raw', '$160', '35.25"', 'D4', 'Max', 'Zero', 'Yes'),
('Callaway', '2019', 'Jaws MD5', 'Tour Wedge', '46-60', '08-12', 'Standard, Low, High', 'Carbon Steel', 'Chrome, Black, Raw', '$160', '35.25"', 'D4', 'Max', 'Zero', 'Yes');

