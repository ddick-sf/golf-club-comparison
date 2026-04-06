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
    const ignoreKeys = ["id", "created_at", "Manufacturer", "Model", "Model Name", "Year", "Release Year"];

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

    // Helper to append UTM parameters to any external URL
    function appendUTM(urlString) {
        if (!urlString || urlString === '#') return urlString;
        try {
            const url = new URL(urlString);
            url.searchParams.set('utm_source', 'clubspec');
            url.searchParams.set('utm_medium', 'referral');
            return url.toString();
        } catch (e) {
            return urlString;
        }
    }

    // Generate GlobalGolf search URL for a club
    function getUsedSearchUrl(club) {
        const model = club["Model Name"] || club["Model"];
        const query = encodeURIComponent(model.trim());
        return appendUTM(`https://www.globalgolf.com/search/?term=${query}`);
    }

    // Get manufacturer website URL
    function getManufacturerUrl(club) {
        const url = manufacturerUrls[club.Manufacturer] || '#';
        return appendUTM(url);
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

        // === DESKTOP: Horizontal comparison grid ===
        const desktopGrid = document.createElement("div");
        desktopGrid.className = "desktop-grid";

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
        desktopGrid.appendChild(nameRow);

        // Render each attribute row
        keys.forEach((key, index) => {
            const rowDiv = document.createElement("div");
            rowDiv.className = "grid-row animate-in";
            rowDiv.style.animationDelay = `${index * 50}ms`;
            
            let rowHtml = `<div class="grid-cell label-cell">${key}</div>`;
            
            for (let i = 0; i < cols; i++) {
                const club = selectedClubs[i];
                const value = club ? club[key] : "-";
                const classStr = club ? "value-cell" : "value-cell empty-state";
                rowHtml += `<div class="grid-cell"><div class="${classStr}">${value || "-"}</div></div>`;
            }
            
            rowDiv.innerHTML = rowHtml;
            desktopGrid.appendChild(rowDiv);
        });

        attributesContainer.appendChild(desktopGrid);

        // === MOBILE: Collapsible card view ===
        const mobileCards = document.createElement("div");
        mobileCards.className = "mobile-cards";

        const activeClubs = selectedClubs.filter(c => c !== null);

        if (activeClubs.length === 0) {
            mobileCards.innerHTML = `<div class="mobile-card-empty">Select clubs above to compare</div>`;
        } else {
            selectedClubs.forEach((club, i) => {
                if (!club) return;

                const card = document.createElement("div");
                card.className = "mobile-card animate-in";
                card.style.animationDelay = `${i * 100}ms`;

                const cardHeader = document.createElement("div");
                cardHeader.className = "mobile-card-header";
                cardHeader.innerHTML = `
                    <div class="mobile-card-title">
                        <span class="mobile-card-brand">${club.Manufacturer}</span>
                        <span class="mobile-card-model">${getModelDisplayName(club)}</span>
                    </div>
                    <svg class="mobile-card-chevron" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg>
                `;

                const cardBody = document.createElement("div");
                cardBody.className = "mobile-card-body";

                // Links row
                cardBody.innerHTML = `
                    <div class="mobile-card-links">
                        <a href="${getManufacturerUrl(club)}" target="_blank" rel="noopener noreferrer" class="club-link club-link--oem">
                            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
                            Official Site
                        </a>
                        <a href="${getUsedSearchUrl(club)}" target="_blank" rel="noopener noreferrer" class="club-link club-link--used">
                            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>
                            Shop Used
                        </a>
                    </div>
                `;

                // Attribute rows
                keys.forEach(key => {
                    const value = club[key] || "-";
                    const row = document.createElement("div");
                    row.className = "mobile-card-row";
                    row.innerHTML = `
                        <span class="mobile-card-label">${key}</span>
                        <span class="mobile-card-value">${value}</span>
                    `;
                    cardBody.appendChild(row);
                });

                // Toggle collapse
                cardHeader.addEventListener("click", () => {
                    card.classList.toggle("expanded");
                });

                // First card starts expanded
                if (i === selectedClubs.indexOf(selectedClubs.find(c => c !== null))) {
                    card.classList.add("expanded");
                }

                card.appendChild(cardHeader);
                card.appendChild(cardBody);
                mobileCards.appendChild(card);
            });
        }

        attributesContainer.appendChild(mobileCards);
    }

    // --- News Feed Logic ---
    async function fetchNewsFeed() {
        // We use rss2json API to fetch and parse the feed easily
        const rssUrl = encodeURIComponent('https://golf.com/category/gear/feed/'); // Gear-specific feed
        const apiUrl = `https://api.rss2json.com/v1/api.json?rss_url=${rssUrl}`;
        
        try {
            const response = await fetch(apiUrl);
            if (!response.ok) throw new Error("Network response was not ok");
            const data = await response.json();
            
            if (data.status !== "ok") throw new Error("RSS parsed failed");

            // Render first 4 articles
            renderNews(data.items.slice(0, 4));
        } catch (err) {
            console.error("News fetch error:", err);
            document.getElementById("rss-container").innerHTML = `<div class="news-card-empty">Unable to load news at this time. Please check back later.</div>`;
        }
    }

    function renderNews(items) {
        const container = document.getElementById("rss-container");
        container.innerHTML = "";
        
        items.forEach((item, index) => {
            // Some feeds put images in content, others in thumbnail. We try to extract if needed.
            let imgUrl = item.thumbnail || "";
            if (!imgUrl) {
                // Try to find image in description or content
                const tempDiv = document.createElement("div");
                tempDiv.innerHTML = item.description || item.content;
                const imgElement = tempDiv.querySelector("img");
                if (imgElement && imgElement.src) {
                    imgUrl = imgElement.src;
                } else {
                    // Fallback golf image
                    imgUrl = "https://images.unsplash.com/photo-1593111774240-d529f12eb4d6?auto=format&fit=crop&q=80&w=600";
                }
            }

            // Format date nicely
            const date = new Date(item.pubDate.replace(' ', 'T')).toLocaleDateString(undefined, { 
                month: 'short', 
                day: 'numeric', 
                year: 'numeric' 
            });

            const card = document.createElement("div");
            card.className = "news-card animate-in";
            // Stagger animations
            card.style.animationDelay = `${index * 150}ms`;
            
            card.innerHTML = `
                <img src="${imgUrl}" alt="Article Thumbnail" class="news-card-img" onerror="this.src='https://images.unsplash.com/photo-1593111774240-d529f12eb4d6?auto=format&fit=crop&q=80&w=600'">
                <div class="news-card-content">
                    <span class="news-card-date">${date}</span>
                    <h3 class="news-card-title" title="${item.title}">${item.title.length > 70 ? item.title.substring(0, 70) + '...' : item.title}</h3>
                    <a href="${appendUTM(item.link)}" target="_blank" rel="noopener noreferrer" class="news-card-link">
                        Read Article
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                    </a>
                </div>
            `;
            container.appendChild(card);
        });
    }

    // Initialize the News Feed
    fetchNewsFeed();
});
