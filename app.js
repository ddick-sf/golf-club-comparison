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

    // Helper to extract year from any club record
    function getClubYear(club) {
        return club["Release Year"] || club["Year"] || "";
    }

    // Helper to get model display name with year
    function getModelDisplayName(club) {
        const name = club["Model Name"] || club["Model"];
        const year = getClubYear(club);
        return year ? `${name} (${year})` : name;
    }

    // Manufacturer website URLs
    const manufacturerUrls = {
        'TaylorMade': 'https://www.taylormadegolf.com',
        'Callaway': 'https://www.callawaygolf.com',
        'PING': 'https://ping.com',
        'Titleist': 'https://www.titleist.com',
        'Cobra': 'https://www.cobragolf.com',
        'Mizuno': 'https://mizunogolf.com',
        'Srixon': 'https://www.srixon.com',
        'PXG': 'https://www.pxg.com',
        'Cleveland': 'https://www.clevelandgolf.com',
        'Sub 70': 'https://www.golfsub70.com',
        'Takomo': 'https://takomogolf.com',
        'Vice Golf': 'https://www.vicegolf.com',
        'Wilson': 'https://www.wilson.com/en-us/golf'
    };

    // Category to search term for used club sites
    const categorySearchTerms = {
        'Drivers': 'driver',
        'Fairways': 'fairway wood',
        'Irons': 'irons',
        'Wedges': 'wedge'
    };

    // Generate GlobalGolf search URL for a club
    function getUsedSearchUrl(club) {
        const model = club["Model Name"] || club["Model"];
        const query = encodeURIComponent(model.trim());
        return `https://www.globalgolf.com/search/?term=${query}`;
    }

    // Get manufacturer website URL
    function getManufacturerUrl(club) {
        return manufacturerUrls[club.Manufacturer] || '#';
    }

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
            opt.value = modelName + '||' + getClubYear(m);
            opt.textContent = getModelDisplayName(m);
            modelSelect.appendChild(opt);
        });
        
        modelSelect.disabled = false;
        renderGrid();
    }

    function handleModelChange(colIndex, modelValue) {
        if (!modelValue) {
            selectedClubs[colIndex] = null;
        } else {
            const [rawModel, rawYear] = modelValue.split('||');
            const data = golfData[currentCategory];
            const colBrand = document.querySelector(`.col-cell[data-col="${colIndex}"] .brand-select`).value;
            const club = data.find(item => item.Manufacturer === colBrand && (item["Model Name"] === rawModel || item["Model"] === rawModel) && getClubYear(item) === rawYear);
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
                     <div class="club-name-display">${getModelDisplayName(club)}</div>
                     <div class="club-links">
                       <a href="${getManufacturerUrl(club)}" target="_blank" rel="noopener noreferrer" class="club-link club-link--oem" title="Visit ${club.Manufacturer}">
                         <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
                         Official Site
                       </a>
                       <a href="${getUsedSearchUrl(club)}" target="_blank" rel="noopener noreferrer" class="club-link club-link--used" title="Shop used on GlobalGolf">
                         <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>
                         Shop Used
                       </a>
                     </div>
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
