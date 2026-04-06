document.addEventListener("DOMContentLoaded", () => {
    // 1. Initialize Supabase Client
    const supabaseUrl = 'https://dlzuupgceexxvqmwzehz.supabase.co';
    const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRsenV1cGdjZWV4eHZxbXd6ZWh6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzQ5ODY2NDIsImV4cCI6MjA5MDU2MjY0Mn0.UFmiDRZ1OSMxZHdTSCZxT1CXLgt1vQKX0vETRHIRkJc';
    const supabase = window.supabase.createClient(supabaseUrl, supabaseKey);

    const clubTypeSelect = document.getElementById("club-type");
    const gridContainer = document.getElementById("compare-grid");
    const attributesContainer = document.getElementById("attributes-container");
    const shareBtn = document.getElementById("share-link-btn");
    
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
    
    // TomSelect Instances
    let brandSelects = [null, null, null];
    let modelSelects = [null, null, null];

    // Key names that identify the model/brand, plus supabase standard identifiers that shouldn't show as generic attributes
    const ignoreKeys = ["id", "created_at", "Manufacturer", "Model", "Model Name", "Year", "Release Year"];

    function getClubYear(club) {
        return club["Release Year"] || club["Year"] || "";
    }

    function getModelDisplayName(club) {
        const name = club["Model Name"] || club["Model"];
        const year = getClubYear(club);
        return year ? `${name} (${year})` : name;
    }

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

    function getUsedSearchUrl(club) {
        const model = club["Model Name"] || club["Model"];
        const query = encodeURIComponent(model.trim());
        return appendUTM(`https://www.globalgolf.com/search/?term=${query}`);
    }

    function getManufacturerUrl(club) {
        const url = manufacturerUrls[club.Manufacturer] || '#';
        return appendUTM(url);
    }
    
    function getYoutubeSearchUrl(club) {
        const model = club["Model Name"] || club["Model"];
        const query = encodeURIComponent(`${club.Manufacturer} ${model} review`);
        return `https://www.youtube.com/results?search_query=${query}`;
    }

    // Update URL Params
    function updateUrlParams() {
        const url = new URL(window.location);
        url.searchParams.delete('category');
        url.searchParams.delete('c0');
        url.searchParams.delete('c1');
        url.searchParams.delete('c2');

        if (currentCategory) {
            url.searchParams.set('category', currentCategory);
            selectedClubs.forEach((club, i) => {
                if (club) {
                    const modelValue = (club["Model Name"] || club["Model"]) + '||' + getClubYear(club);
                    url.searchParams.set(`c${i}`, `${club.Manufacturer}||${modelValue}`);
                }
            });
        }
        window.history.replaceState({}, '', url);
    }

    // Share Button Event
    if (shareBtn) {
        shareBtn.addEventListener("click", () => {
            navigator.clipboard.writeText(window.location.href).then(() => {
                const originalText = shareBtn.innerHTML;
                shareBtn.innerHTML = `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Copied!`;
                shareBtn.classList.add("copied");
                setTimeout(() => {
                    shareBtn.innerHTML = originalText;
                    shareBtn.classList.remove("copied");
                }, 2000);
            });
        });
    }

    // Initialize TomSelect for columns
    for (let i = 0; i < cols; i++) {
        const colCell = document.querySelector(`.col-cell[data-col="${i}"]`);
        const bSelDom = colCell.querySelector(".brand-select");
        const mSelDom = colCell.querySelector(".model-select");

        brandSelects[i] = new TomSelect(bSelDom, {
            create: false,
            selectOnTab: true,
            maxOptions: null
        });
        
        modelSelects[i] = new TomSelect(mSelDom, {
            create: false,
            selectOnTab: true,
            maxOptions: null
        });

        // Use custom callback hooks because TomSelect change event abstracts DOM
        brandSelects[i].on('change', (value) => handleBrandChange(i, value));
        modelSelects[i].on('change', (value) => handleModelChange(i, value));
    }

    clubTypeSelect.addEventListener("change", (e) => handleCategoryChange(e.target.value));

    async function handleCategoryChange(category, initialClubs = null) {
        currentCategory = category;
        clubTypeSelect.value = category;
        
        // GTM Event
        window.dataLayer = window.dataLayer || [];
        window.dataLayer.push({
            'event': 'category_selected',
            'category': currentCategory
        });

        if (!initialClubs) {
            selectedClubs = [null, null, null];
        }
        
        gridContainer.style.display = "flex";

        for (let i = 0; i < cols; i++) {
            brandSelects[i].clearOptions();
            brandSelects[i].clear(true);
            brandSelects[i].disable();
            
            modelSelects[i].clearOptions();
            modelSelects[i].clear(true);
            modelSelects[i].disable();
        }
        
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

        const data = golfData[currentCategory];
        const brands = [...new Set(data.map(item => item.Manufacturer))].sort();
        
        for (let i = 0; i < cols; i++) {
            brandSelects[i].addOption(brands.map(b => ({value: b, text: b})));
            brandSelects[i].enable();
        }

        if (initialClubs) {
            for (let i = 0; i < cols; i++) {
                if (initialClubs[i]) {
                    const [brand, rawModel, rawYear] = initialClubs[i].split("||");
                    // Suppress change event for initial setup
                    brandSelects[i].setValue(brand, true);
                    
                    // Manually populate models
                    const models = data.filter(item => item.Manufacturer === brand);
                    const options = models.map(m => {
                        const modelName = m["Model Name"] || m["Model"];
                        return {
                            value: modelName + '||' + getClubYear(m),
                            text: getModelDisplayName(m)
                        };
                    });
                    modelSelects[i].addOption(options);
                    modelSelects[i].enable();
                    modelSelects[i].setValue(rawModel + '||' + rawYear, true);
                    
                    const club = data.find(item => item.Manufacturer === brand && (item["Model Name"] === rawModel || item["Model"] === rawModel) && getClubYear(item) === rawYear);
                    selectedClubs[i] = club || null;
                }
            }
        }

        renderGrid();
    }

    function handleBrandChange(colIndex, brandValue) {
        if (!brandValue) {
            modelSelects[colIndex].clearOptions();
            modelSelects[colIndex].clear(true);
            modelSelects[colIndex].disable();
            selectedClubs[colIndex] = null;
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

        // Populate models
        const data = golfData[currentCategory];
        const models = data.filter(item => item.Manufacturer === brandValue);
        
        const options = models.map(m => {
            const modelName = m["Model Name"] || m["Model"];
            return {
                value: modelName + '||' + getClubYear(m),
                text: getModelDisplayName(m)
            };
        });
        
        modelSelects[colIndex].clear(true);
        modelSelects[colIndex].clearOptions();
        modelSelects[colIndex].addOption(options);
        modelSelects[colIndex].enable();
        selectedClubs[colIndex] = null;
        renderGrid();
    }

    function handleModelChange(colIndex, modelValue) {
        if (!modelValue) {
            selectedClubs[colIndex] = null;
        } else {
            const [rawModel, rawYear] = modelValue.split('||');
            const data = golfData[currentCategory];
            const colBrand = brandSelects[colIndex].getValue();
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
        const firstItem = golfData[currentCategory][0];
        return Object.keys(firstItem).filter(key => !ignoreKeys.includes(key) && firstItem[key] !== undefined && firstItem[key] !== null);
    }

    function renderGrid() {
        const keys = getAttributeKeys();
        attributesContainer.innerHTML = "";
        
        updateUrlParams();

        const activeClubs = selectedClubs.filter(c => c !== null);
        
        // Hide/Show Trending Section based on grid populate status
        const trendingSection = document.getElementById("trending-section");
        if (trendingSection) {
            trendingSection.style.display = activeClubs.length > 0 ? "none" : "block";
        }

        // === DESKTOP ===
        const desktopGrid = document.createElement("div");
        desktopGrid.className = "desktop-grid";

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
                         OEM
                       </a>
                       <a href="${getUsedSearchUrl(club)}" target="_blank" rel="noopener noreferrer" class="club-link club-link--used" title="Shop used on GlobalGolf">
                         <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>
                         Used
                       </a>
                       <a href="${getYoutubeSearchUrl(club)}" target="_blank" rel="noopener noreferrer" class="club-link" style="background: rgba(220,38,38,0.08); color: #ef4444; border-color: rgba(220,38,38,0.2);" title="YouTube Reviews">
                         <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33 2.78 2.78 0 0 0 1.94 2c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.33 29 29 0 0 0-.46-5.33z"></path><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"></polygon></svg>
                         YT
                       </a>
                     </div>
                   </div>`
                : `<div class="club-preview empty-state">No club selected...</div>`;
            
            nameRow.innerHTML += `<div class="grid-cell" style="border-bottom: 2px solid var(--glass-border);">${content}</div>`;
        }
        desktopGrid.appendChild(nameRow);

        let rowDelay = 0;
        keys.forEach((key, index) => {
            // Check for differences
            const values = activeClubs.map(c => c[key]);
            const allSame = values.length > 0 && values.every(v => v === values[0]);
            const difference = activeClubs.length > 1 && !allSame;

            const rowDiv = document.createElement("div");
            rowDiv.className = difference ? "grid-row animate-in diff-highlight" : "grid-row animate-in";
            rowDiv.style.animationDelay = `${rowDelay * 50}ms`;
            rowDelay++;
            
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

        // === MOBILE ===
        const mobileCards = document.createElement("div");
        mobileCards.className = "mobile-cards";

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

                cardBody.innerHTML = `
                    <div class="mobile-card-links">
                        <a href="${getManufacturerUrl(club)}" target="_blank" class="club-link club-link--oem">OEM</a>
                        <a href="${getUsedSearchUrl(club)}" target="_blank" class="club-link club-link--used">Used</a>
                        <a href="${getYoutubeSearchUrl(club)}" target="_blank" class="club-link" style="background: rgba(220,38,38,0.08); color: #ef4444; border-color: rgba(220,38,38,0.2);">YouTube</a>
                    </div>
                `;

                keys.forEach(key => {
                    const value = club[key] || "-";
                    
                    // Check diff for mobile highlight
                    const values = activeClubs.map(c => c[key]);
                    const allSame = values.length > 0 && values.every(v => v === values[0]);
                    const isDiff = activeClubs.length > 1 && !allSame;

                    const row = document.createElement("div");
                    row.className = isDiff ? "mobile-card-row diff-highlight" : "mobile-card-row";
                    row.innerHTML = `
                        <span class="mobile-card-label">${key}</span>
                        <span class="mobile-card-value">${value}</span>
                    `;
                    cardBody.appendChild(row);
                });

                cardHeader.addEventListener("click", () => {
                    card.classList.toggle("expanded");
                });

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
        const rssUrl = encodeURIComponent('https://golf.com/category/gear/feed/');
        const apiUrl = `https://api.rss2json.com/v1/api.json?rss_url=${rssUrl}`;
        
        try {
            const response = await fetch(apiUrl);
            if (!response.ok) throw new Error("Network response was not ok");
            const data = await response.json();
            
            if (data.status !== "ok") throw new Error("RSS parsed failed");

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
            let imgUrl = item.thumbnail || "";
            if (!imgUrl && item.enclosure && item.enclosure.link) imgUrl = item.enclosure.link;
            if (!imgUrl) {
                const tempDiv = document.createElement("div");
                tempDiv.innerHTML = item.description || item.content;
                const imgElement = tempDiv.querySelector("img");
                imgUrl = imgElement && imgElement.src ? imgElement.src : "https://images.unsplash.com/photo-1593111774240-d529f12eb4d6?auto=format&fit=crop&q=80&w=600";
            }

            const date = new Date(item.pubDate.replace(' ', 'T')).toLocaleDateString(undefined, { month: 'short', day: 'numeric', year: 'numeric' });

            const card = document.createElement("div");
            card.className = "news-card animate-in";
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

    // --- On Load Init Logic ---
    fetchNewsFeed();

    // Check for URL parameters
    const urlParams = new URLSearchParams(window.location.search);
    const initialCategory = urlParams.get('category');
    
    if (initialCategory) {
        const c0 = urlParams.get('c0');
        const c1 = urlParams.get('c1');
        const c2 = urlParams.get('c2');
        handleCategoryChange(initialCategory, [c0, c1, c2]);
    }

    // Setup Trending Cards
    document.querySelectorAll(".trending-card").forEach(card => {
        card.addEventListener("click", () => {
            const cat = card.dataset.category;
            const c0 = card.dataset.c0 || null;
            const c1 = card.dataset.c1 || null;
            const c2 = card.dataset.c2 || null;
            handleCategoryChange(cat, [c0, c1, c2]);
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    });

});
