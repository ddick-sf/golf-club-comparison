document.addEventListener("DOMContentLoaded", () => {
    // 1. Initialize Supabase Client
    const supabaseUrl = 'https://dlzuupgceexxvqmwzehz.supabase.co';
    const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRsenV1cGdjZWV4eHZxbXd6ZWh6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzQ5ODY2NDIsImV4cCI6MjA5MDU2MjY0Mn0.UFmiDRZ1OSMxZHdTSCZxT1CXLgt1vQKX0vETRHIRkJc';
    const supabase = window.supabase.createClient(supabaseUrl, supabaseKey);

    const clubTypeSelect = document.getElementById("club-type");
    const gridContainer = document.getElementById("compare-grid");
    const headerRow = document.getElementById("header-row");
    const attributesContainer = document.getElementById("attributes-container");
    
    // Cached Global Data
    const golfData = {
        "Drivers": [],
        "Fairways": [],
        "Irons": [],
        "Wedges": []
    };

    // We have 3 columns to compare
    const cols = 3;
    let currentCategory = "";
    
    // Array to store selected club object for each column (0, 1, 2)
    let selectedClubs = [null, null, null];
    
    // Key names that identify the model/brand, plus supabase standard identifiers that shouldn't show as generic attributes
    const ignoreKeys = ["id", "created_at", "Manufacturer", "Model", "Model Name"];

    // Setup event listeners
    clubTypeSelect.addEventListener("change", handleCategoryChange);

    // Setup column selector listeners
    for (let i = 0; i < cols; i++) {
        const colCell = document.querySelector(`.col-cell[data-col="${i}"]`);
        const brandSelect = colCell.querySelector(".brand-select");
        const modelSelect = colCell.querySelector(".model-select");

        brandSelect.addEventListener("change", (e) => handleBrandChange(i, e.target.value));
        modelSelect.addEventListener("change", (e) => handleModelChange(i, e.target.value));
    }

    async function handleCategoryChange(e) {
        currentCategory = e.target.value;
        
        // GTM Event
        window.dataLayer = window.dataLayer || [];
        window.dataLayer.push({
            'event': 'category_selected',
            'category': currentCategory
        });

        selectedClubs = [null, null, null];
        
        // Expose grid framing
        gridContainer.style.display = "flex";

        // Reset all selectors while loading
        for (let i = 0; i < cols; i++) {
            const colCell = document.querySelector(`.col-cell[data-col="${i}"]`);
            const brandSelect = colCell.querySelector(".brand-select");
            const modelSelect = colCell.querySelector(".model-select");
            brandSelect.innerHTML = '<option value="">Brand...</option>';
            brandSelect.disabled = true;
            modelSelect.innerHTML = '<option value="">Model...</option>';
            modelSelect.disabled = true;
        }
        
        // Fetch from Supabase if we don't have it cached
        if (golfData[currentCategory].length === 0) {
            attributesContainer.innerHTML = '<div style="padding: 4rem 2rem; text-align: center; color: var(--text-secondary);"><span class="animate-pulse">Loading live specifications from database...</span></div>';
            
            const { data, error } = await supabase.from(currentCategory).select('*');
            
            if (error) {
                console.error("Error fetching data:", error);
                attributesContainer.innerHTML = `<div style="padding: 4rem 2rem; text-align: center; color: #f87171;">Failed to connect to Specification Database. Support has been notified.</div>`;
                return;
            }
            if (data && data.length > 0) {
                golfData[currentCategory] = data;
            } else {
                attributesContainer.innerHTML = `<div style="padding: 4rem 2rem; text-align: center; color: var(--text-secondary);">No catalog data found for ${currentCategory}. Check back later.</div>`;
                return;
            }
        }

        // We have the data, populate the brand selectors
        const data = golfData[currentCategory];
        const brands = [...new Set(data.map(item => item.Manufacturer))].sort();
        
        for (let i = 0; i < cols; i++) {
            const colCell = document.querySelector(`.col-cell[data-col="${i}"]`);
            const brandSelect = colCell.querySelector(".brand-select");

            brandSelect.disabled = false;
            brands.forEach(b => {
                const opt = document.createElement("option");
                opt.value = b;
                opt.textContent = b;
                brandSelect.appendChild(opt);
            });
        }

        renderGrid();
    }

    function handleBrandChange(colIndex, brandValue) {
        const colCell = document.querySelector(`.col-cell[data-col="${colIndex}"]`);
        const modelSelect = colCell.querySelector(".model-select");
        
        // Reset selected club for this column
        selectedClubs[colIndex] = null;
        
        if (!brandValue) {
            modelSelect.innerHTML = '<option value="">Select Model...</option>';
            modelSelect.disabled = true;
            renderGrid();
            return;
        }

        // GTM Event
        window.dataLayer = window.dataLayer || [];
        window.dataLayer.push({
            'event': 'brand_selected',
            'category': currentCategory,
            'column': colIndex + 1,
            'brand': brandValue
        });

        // Get models for brand
        const data = golfData[currentCategory];
        const models = data.filter(item => item.Manufacturer === brandValue);
        
        modelSelect.innerHTML = '<option value="">Select Model...</option>';
        models.forEach(m => {
            const modelName = m["Model Name"] || m["Model"];
            const opt = document.createElement("option");
            opt.value = modelName;
            opt.textContent = modelName;
            modelSelect.appendChild(opt);
        });
        
        modelSelect.disabled = false;
        renderGrid();
    }

    function handleModelChange(colIndex, modelValue) {
        if (!modelValue) {
            selectedClubs[colIndex] = null;
        } else {
            const data = golfData[currentCategory];
            const colBrand = document.querySelector(`.col-cell[data-col="${colIndex}"] .brand-select`).value;
            const club = data.find(item => item.Manufacturer === colBrand && (item["Model Name"] === modelValue || item["Model"] === modelValue));
            selectedClubs[colIndex] = club || null;

            // GTM Event
            window.dataLayer = window.dataLayer || [];
            window.dataLayer.push({
                'event': 'model_selected',
                'category': currentCategory,
                'column': colIndex + 1,
                'brand': colBrand,
                'model': modelValue
            });
        }
        renderGrid();
    }

    function getAttributeKeys() {
        if (!currentCategory || !golfData[currentCategory].length) return [];
        // Extract all keys from the first item
        const firstItem = golfData[currentCategory][0];
        return Object.keys(firstItem).filter(key => !ignoreKeys.includes(key) && firstItem[key] !== undefined && firstItem[key] !== null);
    }

    function renderGrid() {
        const keys = getAttributeKeys();
        attributesContainer.innerHTML = "";

        // First row for nice display (Brand + Model Text)
        const nameRow = document.createElement("div");
        nameRow.className = "grid-row animate-in";
        nameRow.innerHTML = `<div class="grid-cell label-cell" style="background: transparent; border-bottom: 2px solid var(--glass-border);"></div>`;
        
        for (let i = 0; i < cols; i++) {
            const club = selectedClubs[i];
            const content = club 
                ? `<div class="club-preview">
                     <div class="club-brand-display">${club.Manufacturer}</div>
                     <div class="club-name-display">${club["Model Name"] || club["Model"]}</div>
                   </div>`
                : `<div class="club-preview empty-state">No club selected...</div>`;
            
            nameRow.innerHTML += `<div class="grid-cell" style="border-bottom: 2px solid var(--glass-border);">${content}</div>`;
        }
        attributesContainer.appendChild(nameRow);

        // Now render each attribute
        keys.forEach((key, index) => {
            const rowDiv = document.createElement("div");
            rowDiv.className = "grid-row animate-in";
            rowDiv.style.animationDelay = `${index * 50}ms`;
            
            let rowHtml = `<div class="grid-cell label-cell">${key}</div>`;
            
            for (let i = 0; i < cols; i++) {
                const club = selectedClubs[i];
                const value = club ? club[key] : "-";
                // Colorize the cell text based on empty state
                const classStr = club ? "value-cell" : "value-cell empty-state";
                rowHtml += `<div class="grid-cell"><div class="${classStr}">${value || "-"}</div></div>`;
            }
            
            rowDiv.innerHTML = rowHtml;
            attributesContainer.appendChild(rowDiv);
        });
    }
});
