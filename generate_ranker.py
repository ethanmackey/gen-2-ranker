"""
Pokemon Gen 2 Ranker Generator
Generates a static HTML page for ranking all 100 Gen 2 Pokemon (152-251)
"""

# Gen 2 Pokemon data (ID, Name, Types, Species)
GEN2_POKEMON = [
    (152, "Chikorita", ["Grass"], "Leaf Pokémon"),
    (153, "Bayleef", ["Grass"], "Leaf Pokémon"),
    (154, "Meganium", ["Grass"], "Herb Pokémon"),
    (155, "Cyndaquil", ["Fire"], "Fire Mouse Pokémon"),
    (156, "Quilava", ["Fire"], "Volcano Pokémon"),
    (157, "Typhlosion", ["Fire"], "Volcano Pokémon"),
    (158, "Totodile", ["Water"], "Big Jaw Pokémon"),
    (159, "Croconaw", ["Water"], "Big Jaw Pokémon"),
    (160, "Feraligatr", ["Water"], "Big Jaw Pokémon"),
    (161, "Sentret", ["Normal"], "Scout Pokémon"),
    (162, "Furret", ["Normal"], "Long Body Pokémon"),
    (163, "Hoothoot", ["Normal", "Flying"], "Owl Pokémon"),
    (164, "Noctowl", ["Normal", "Flying"], "Owl Pokémon"),
    (165, "Ledyba", ["Bug", "Flying"], "Five Star Pokémon"),
    (166, "Ledian", ["Bug", "Flying"], "Five Star Pokémon"),
    (167, "Spinarak", ["Bug", "Poison"], "String Spit Pokémon"),
    (168, "Ariados", ["Bug", "Poison"], "Long Leg Pokémon"),
    (169, "Crobat", ["Poison", "Flying"], "Bat Pokémon"),
    (170, "Chinchou", ["Water", "Electric"], "Angler Pokémon"),
    (171, "Lanturn", ["Water", "Electric"], "Light Pokémon"),
    (172, "Pichu", ["Electric"], "Tiny Mouse Pokémon"),
    (173, "Cleffa", ["Fairy"], "Star Shape Pokémon"),
    (174, "Igglybuff", ["Normal", "Fairy"], "Balloon Pokémon"),
    (175, "Togepi", ["Fairy"], "Spike Ball Pokémon"),
    (176, "Togetic", ["Fairy", "Flying"], "Happiness Pokémon"),
    (177, "Natu", ["Psychic", "Flying"], "Tiny Bird Pokémon"),
    (178, "Xatu", ["Psychic", "Flying"], "Mystic Pokémon"),
    (179, "Mareep", ["Electric"], "Wool Pokémon"),
    (180, "Flaaffy", ["Electric"], "Wool Pokémon"),
    (181, "Ampharos", ["Electric"], "Light Pokémon"),
    (182, "Bellossom", ["Grass"], "Flower Pokémon"),
    (183, "Marill", ["Water", "Fairy"], "Aqua Mouse Pokémon"),
    (184, "Azumarill", ["Water", "Fairy"], "Aqua Rabbit Pokémon"),
    (185, "Sudowoodo", ["Rock"], "Imitation Pokémon"),
    (186, "Politoed", ["Water"], "Frog Pokémon"),
    (187, "Hoppip", ["Grass", "Flying"], "Cottonweed Pokémon"),
    (188, "Skiploom", ["Grass", "Flying"], "Cottonweed Pokémon"),
    (189, "Jumpluff", ["Grass", "Flying"], "Cottonweed Pokémon"),
    (190, "Aipom", ["Normal"], "Long Tail Pokémon"),
    (191, "Sunkern", ["Grass"], "Seed Pokémon"),
    (192, "Sunflora", ["Grass"], "Sun Pokémon"),
    (193, "Yanma", ["Bug", "Flying"], "Clear Wing Pokémon"),
    (194, "Wooper", ["Water", "Ground"], "Water Fish Pokémon"),
    (195, "Quagsire", ["Water", "Ground"], "Water Fish Pokémon"),
    (196, "Espeon", ["Psychic"], "Sun Pokémon"),
    (197, "Umbreon", ["Dark"], "Moonlight Pokémon"),
    (198, "Murkrow", ["Dark", "Flying"], "Darkness Pokémon"),
    (199, "Slowking", ["Water", "Psychic"], "Royal Pokémon"),
    (200, "Misdreavus", ["Ghost"], "Screech Pokémon"),
    (201, "Unown", ["Psychic"], "Symbol Pokémon"),
    (202, "Wobbuffet", ["Psychic"], "Patient Pokémon"),
    (203, "Girafarig", ["Normal", "Psychic"], "Long Neck Pokémon"),
    (204, "Pineco", ["Bug"], "Bagworm Pokémon"),
    (205, "Forretress", ["Bug", "Steel"], "Bagworm Pokémon"),
    (206, "Dunsparce", ["Normal"], "Land Snake Pokémon"),
    (207, "Gligar", ["Ground", "Flying"], "Fly Scorpion Pokémon"),
    (208, "Steelix", ["Steel", "Ground"], "Iron Snake Pokémon"),
    (209, "Snubbull", ["Fairy"], "Fairy Pokémon"),
    (210, "Granbull", ["Fairy"], "Fairy Pokémon"),
    (211, "Qwilfish", ["Water", "Poison"], "Balloon Pokémon"),
    (212, "Scizor", ["Bug", "Steel"], "Pincer Pokémon"),
    (213, "Shuckle", ["Bug", "Rock"], "Mold Pokémon"),
    (214, "Heracross", ["Bug", "Fighting"], "Single Horn Pokémon"),
    (215, "Sneasel", ["Dark", "Ice"], "Sharp Claw Pokémon"),
    (216, "Teddiursa", ["Normal"], "Little Bear Pokémon"),
    (217, "Ursaring", ["Normal"], "Hibernator Pokémon"),
    (218, "Slugma", ["Fire"], "Lava Pokémon"),
    (219, "Magcargo", ["Fire", "Rock"], "Lava Pokémon"),
    (220, "Swinub", ["Ice", "Ground"], "Pig Pokémon"),
    (221, "Piloswine", ["Ice", "Ground"], "Swine Pokémon"),
    (222, "Corsola", ["Water", "Rock"], "Coral Pokémon"),
    (223, "Remoraid", ["Water"], "Jet Pokémon"),
    (224, "Octillery", ["Water"], "Jet Pokémon"),
    (225, "Delibird", ["Ice", "Flying"], "Delivery Pokémon"),
    (226, "Mantine", ["Water", "Flying"], "Kite Pokémon"),
    (227, "Skarmory", ["Steel", "Flying"], "Armor Bird Pokémon"),
    (228, "Houndour", ["Dark", "Fire"], "Dark Pokémon"),
    (229, "Houndoom", ["Dark", "Fire"], "Dark Pokémon"),
    (230, "Kingdra", ["Water", "Dragon"], "Dragon Pokémon"),
    (231, "Phanpy", ["Ground"], "Long Nose Pokémon"),
    (232, "Donphan", ["Ground"], "Armor Pokémon"),
    (233, "Porygon2", ["Normal"], "Virtual Pokémon"),
    (234, "Stantler", ["Normal"], "Big Horn Pokémon"),
    (235, "Smeargle", ["Normal"], "Painter Pokémon"),
    (236, "Tyrogue", ["Fighting"], "Scuffle Pokémon"),
    (237, "Hitmontop", ["Fighting"], "Handstand Pokémon"),
    (238, "Smoochum", ["Ice", "Psychic"], "Kiss Pokémon"),
    (239, "Elekid", ["Electric"], "Electric Pokémon"),
    (240, "Magby", ["Fire"], "Live Coal Pokémon"),
    (241, "Miltank", ["Normal"], "Milk Cow Pokémon"),
    (242, "Blissey", ["Normal"], "Happiness Pokémon"),
    (243, "Raikou", ["Electric"], "Thunder Pokémon"),
    (244, "Entei", ["Fire"], "Volcano Pokémon"),
    (245, "Suicune", ["Water"], "Aurora Pokémon"),
    (246, "Larvitar", ["Rock", "Ground"], "Rock Skin Pokémon"),
    (247, "Pupitar", ["Rock", "Ground"], "Hard Shell Pokémon"),
    (248, "Tyranitar", ["Rock", "Dark"], "Armor Pokémon"),
    (249, "Lugia", ["Psychic", "Flying"], "Diving Pokémon"),
    (250, "Ho-Oh", ["Fire", "Flying"], "Rainbow Pokémon"),
    (251, "Celebi", ["Psychic", "Grass"], "Time Travel Pokémon")
]

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Gen 2 Pokemon Ranker</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            -webkit-tap-highlight-color: transparent;
        }
        
        html, body {
            height: 100vh;
            height: 100dvh;
            overflow: hidden;
            position: fixed;
            width: 100%;
            background: #667eea;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 0.5vh;
            padding-top: max(0.5vh, env(safe-area-inset-top));
            padding-bottom: max(0.5vh, env(safe-area-inset-bottom));
            height: 100dvh;
            max-height: 100dvh;
            overflow: hidden;
        }
        
        h1 {
            color: white;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.3);
            margin-bottom: 0.3vh;
            text-align: center;
            font-size: 2.5vh;
        }
        
        .progress {
            color: white;
            font-size: 1.8vh;
            margin-bottom: 0.3vh;
        }
        
        .progress-bar {
            width: 80%;
            max-width: 30vh;
            height: 1vh;
            background: rgba(255,255,255,0.3);
            border-radius: 0.5vh;
            margin-bottom: 0.5vh;
            overflow: hidden;
        }
        
        .progress-fill {
            height: 100%;
            background: #4ade80;
            transition: width 0.3s ease;
        }
        
        .instructions {
            color: white;
            text-align: center;
            margin-bottom: 0.3vh;
            font-size: 1.8vh;
            padding: 0 5px;
        }
        
        .selection-count {
            color: #4ade80;
            font-size: 2vh;
            font-weight: bold;
            margin-bottom: 0.2vh;
        }
        
        .hint {
            color: rgba(255,255,255,0.7);
            font-size: 1.5vh;
            margin-bottom: 0.5vh;
            font-style: italic;
        }
        
        .batch-container {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            grid-template-rows: repeat(5, 1fr);
            gap: 0.5vh;
            width: 100%;
            max-width: 50vh;
            flex: 1;
            min-height: 0;
        }
        
        .pokemon-card {
            background: white;
            border-radius: 0.8vh;
            padding: 0.3vh;
            cursor: pointer;
            transition: all 0.1s ease;
            box-shadow: 0 0.3vh 1vh rgba(0,0,0,0.2);
            text-align: center;
            touch-action: manipulation;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }
        
        .pokemon-card:active {
            transform: scale(0.95);
        }
        
        .pokemon-card.selected {
            background: #4ade80;
            border: 3px solid #22c55e;
        }
        
        .pokemon-card.selected .name,
        .pokemon-card.selected .number {
            color: white;
        }
        
        .pokemon-card img {
            max-height: 7vh;
            max-width: 100%;
            width: auto;
            height: auto;
            image-rendering: pixelated;
            margin-top: 0.3vh;
        }
        
        .pokemon-card .name {
            color: #333;
            font-size: 1.4vh;
            font-weight: bold;
            line-height: 1;
            margin-top: 0.5vh;
        }
        
        .pokemon-card .species {
            color: #333;
            font-size: 1.2vh;
            font-style: italic;
            line-height: 1;
            margin-top: 0.2vh;
        }
        
        .pokemon-card.selected .species {
            color: rgba(255,255,255,0.85);
        }
        
        .pokemon-card .number {
            display: none;
        }
        
        .round-info {
            color: white;
            font-size: 2.2vh;
            font-weight: bold;
            margin-bottom: 0.3vh;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.3);
        }
        
        .btn-row {
            display: flex;
            gap: 1.5vh;
            justify-content: center;
            margin-top: 0.8vh;
        }
        
        .next-btn, .back-btn, .undo-btn {
            padding: 1.2vh 2.5vh;
            font-size: 2vh;
            color: white;
            border: none;
            border-radius: 1vh;
            cursor: pointer;
            box-shadow: 0 0.3vh 1vh rgba(0,0,0,0.2);
            touch-action: manipulation;
        }
        
        .next-btn {
            background: linear-gradient(135deg, #4ade80 0%, #22c55e 100%);
        }
        
        .back-btn {
            background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        }
        
        .undo-btn {
            background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        }
        
        .next-btn:active, .back-btn:active, .undo-btn:active {
            transform: scale(0.95);
        }
        
        .next-btn:disabled, .back-btn:disabled, .undo-btn:disabled {
            background: #888;
            cursor: not-allowed;
            opacity: 0.6;
        }
        
        /* Pairwise battle styles */
        .battle-container {
            display: none;
            flex-direction: row;
            gap: 2vh;
            align-items: center;
            justify-content: center;
            flex: 1;
            width: 100%;
        }
        
        .battle-card {
            background: white;
            border-radius: 1.5vh;
            padding: 1vh 0.8vh;
            cursor: pointer;
            transition: all 0.15s ease;
            box-shadow: 0 0.8vh 2.5vh rgba(0,0,0,0.25);
            text-align: center;
            flex: 1;
            max-width: 42vw;
            touch-action: manipulation;
        }
        
        .battle-card:active {
            transform: scale(0.95);
            background: #4ade80;
        }
        
        .battle-card:active .name,
        .battle-card:active .number {
            color: white;
        }
        
        .battle-card img {
            max-height: 35vh;
            max-width: 100%;
            width: auto;
            height: auto;
            image-rendering: pixelated;
        }
        
        .battle-card .name {
            margin-top: 0.5vh;
            color: #333;
            font-size: 2.2vh;
            font-weight: bold;
        }
        
        .battle-card .number {
            color: #888;
            font-size: 1.8vh;
        }
        
        .battle-card .desc {
            color: #666;
            font-size: 1.3vh;
            font-style: italic;
            margin-top: 0.5vh;
            line-height: 1.3;
            max-height: 5vh;
            overflow: hidden;
        }
        
        /* Type badge styles */
        .type-container {
            display: flex;
            gap: 0.3vh;
            justify-content: center;
            margin-top: 0.2vh;
            flex-wrap: wrap;
        }
        
        .type-badge {
            font-size: 1vh;
            padding: 0.2vh 0.5vh;
            border-radius: 0.3vh;
            color: white;
            font-weight: bold;
            text-transform: uppercase;
            text-shadow: 0 1px 1px rgba(0,0,0,0.3);
        }
        
        .battle-card .type-badge {
            font-size: 1.5vh;
            padding: 0.3vh 0.8vh;
        }
        
        .rank-card .type-badge, .ranking-item .type-badge {
            font-size: 0.55em;
            padding: 1px 4px;
        }
        
        .type-normal { background: #A8A878; }
        .type-fire { background: #F08030; }
        .type-water { background: #6890F0; }
        .type-electric { background: #F8D030; color: #333; }
        .type-grass { background: #78C850; }
        .type-ice { background: #98D8D8; color: #333; }
        .type-fighting { background: #C03028; }
        .type-poison { background: #A040A0; }
        .type-ground { background: #E0C068; color: #333; }
        .type-flying { background: #A890F0; }
        .type-psychic { background: #F85888; }
        .type-bug { background: #A8B820; }
        .type-rock { background: #B8A038; }
        .type-ghost { background: #705898; }
        .type-dragon { background: #7038F8; }
        .type-dark { background: #705848; }
        .type-steel { background: #B8B8D0; color: #333; }
        .type-fairy { background: #EE99AC; }
        
        .vs {
            font-size: 4vh;
            color: white;
            font-weight: bold;
            text-shadow: 0.3vh 0.3vh 0.5vh rgba(0,0,0,0.3);
            flex-shrink: 0;
        }
        
        #results {
            display: none;
            background: white;
            border-radius: 12px;
            padding: 12px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.2);
            text-align: center;
            width: 100%;
            max-width: 400px;
            flex: 1;
            overflow: hidden;
            display: none;
            flex-direction: column;
        }
        
        #results h2 {
            color: #333;
            margin-bottom: 10px;
            font-size: 1.1em;
        }
        
        .top-pokemon {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 6px;
        }
        
        .rank-card {
            background: linear-gradient(135deg, #ffd700 0%, #ffaa00 100%);
            border-radius: 8px;
            padding: 6px;
            text-align: center;
        }
        
        .rank-card:nth-child(2) {
            background: linear-gradient(135deg, #c0c0c0 0%, #a0a0a0 100%);
        }
        
        .rank-card:nth-child(3) {
            background: linear-gradient(135deg, #cd7f32 0%, #b06020 100%);
        }
        
        .rank-card:nth-child(n+4) {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        
        .rank-card .rank {
            font-size: 0.8em;
            font-weight: bold;
            color: white;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
        }
        
        .rank-card img {
            width: 45px;
            height: 45px;
            image-rendering: pixelated;
        }
        
        .rank-card .name {
            color: white;
            font-weight: bold;
            font-size: 0.65em;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
        }
        
        .rank-card .desc {
            color: rgba(255,255,255,0.85);
            font-size: 0.5em;
            font-style: italic;
            margin-top: 2px;
            line-height: 1.2;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
        }
        
        .full-rankings {
            margin-top: 8px;
            text-align: left;
            flex: 1;
            overflow-y: auto;
            padding: 8px;
            background: #f5f5f5;
            border-radius: 8px;
            min-height: 0;
        }
        
        .full-rankings h3 {
            margin-bottom: 6px;
            color: #333;
            font-size: 0.85em;
        }
        
        .ranking-item {
            display: flex;
            align-items: center;
            padding: 4px 0;
            border-bottom: 1px solid #ddd;
        }
        
        .ranking-item .position {
            width: 24px;
            font-weight: bold;
            color: #666;
            font-size: 0.8em;
        }
        
        .ranking-item img {
            width: 28px;
            height: 28px;
            image-rendering: pixelated;
        }
        
        .ranking-item .name {
            margin-left: 6px;
            color: #333;
            font-size: 0.8em;
        }
        
        .ranking-item .score {
            margin-left: auto;
            color: #888;
            font-size: 0.7em;
        }
        
        #restart-btn {
            margin-top: 8px;
            padding: 10px 24px;
            font-size: 0.9em;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            touch-action: manipulation;
            flex-shrink: 0;
        }
        
        #restart-btn:active {
            transform: scale(0.95);
        }
    </style>
</head>
<body>
    <h1>Gen 2 Pokemon Ranker</h1>
    <p class="round-info" id="round-info">Phase 1: Selection</p>
    <p class="instructions" id="instructions">Select all your favorites from this batch!</p>
    <p class="progress">Batch <span id="current">1</span> of <span id="total">0</span></p>
    <div class="progress-bar">
        <div class="progress-fill" id="progress-fill"></div>
    </div>
    <p class="selection-count" id="selection-count">0 favorites selected</p>
    <p class="hint" id="hint">Tip: The more selective you are, the fewer comparisons later!</p>
    
    <div class="batch-container" id="batch"></div>
    
    <div class="btn-row" id="selection-btns">
        <button class="back-btn" id="back-btn" onclick="prevBatch()" disabled>← Back</button>
        <button class="next-btn" id="next-btn" onclick="nextBatch()">Next →</button>
    </div>
    
    <div class="battle-container" id="battle">
        <div class="battle-card" onclick="selectWinner(0)">
            <img id="battle-img1" src="" alt="">
            <p class="name" id="battle-name1"></p>
            <div class="type-container" id="battle-types1"></div>
            <p class="desc" id="battle-desc1"></p>
        </div>
        
        <span class="vs">VS</span>
        
        <div class="battle-card" onclick="selectWinner(1)">
            <img id="battle-img2" src="" alt="">
            <p class="name" id="battle-name2"></p>
            <div class="type-container" id="battle-types2"></div>
            <p class="desc" id="battle-desc2"></p>
        </div>
        </div>
    </div>
    
    <div class="btn-row" id="undo-row" style="display: none;">
        <button class="undo-btn" id="undo-btn" onclick="undoChoice()" disabled>↩ Undo</button>
    </div>
    
    <div id="results">
        <h2>🏆 Your Top Gen 2 Pokemon! 🏆</h2>
        <div class="top-pokemon" id="top-pokemon"></div>
        <div class="full-rankings">
            <h3>Full Rankings</h3>
            <div id="full-list"></div>
        </div>
        <button id="restart-btn" onclick="restart()">Rank Again</button>
    </div>
    
    <script>
        // Gen 2 Pokemon data
        const pokemon = POKEMON_DATA_PLACEHOLDER;
        
        // State
        const BATCH_SIZE = 10;
        let allPokemon = [];
        let favorites = [];
        let batchSelections = []; // Store selections per batch for undo
        let batchIndex = 0;
        let totalBatches = 0;
        let currentBatch = [];
        
        // Pairwise ranking state
        let ratings = {};
        let initialRatings = {};
        let comparisons = [];
        let currentComparison = 0;
        let history = []; // For undo in pairwise phase
        const K = 32;
        
        // Helper to render type badges
        function renderTypes(types) {
            return types.map(t => 
                `<span class="type-badge type-${t.toLowerCase()}">${t}</span>`
            ).join('');
        }
        
        function init() {
            allPokemon = [...pokemon].sort(() => Math.random() - 0.5);
            favorites = [];
            batchSelections = [];
            batchIndex = 0;
            totalBatches = Math.ceil(allPokemon.length / BATCH_SIZE);
            
            // Initialize empty selections for each batch
            for (let i = 0; i < totalBatches; i++) {
                batchSelections.push(new Set());
            }
            
            document.getElementById('total').textContent = totalBatches;
            document.getElementById('selection-count').textContent = '0 favorites selected';
            
            showBatch();
        }
        
        function getTotalFavorites() {
            let count = 0;
            batchSelections.forEach(set => count += set.size);
            return count;
        }
        
        function showBatch() {
            const start = batchIndex * BATCH_SIZE;
            const end = Math.min(start + BATCH_SIZE, allPokemon.length);
            currentBatch = allPokemon.slice(start, end);
            
            const container = document.getElementById('batch');
            container.innerHTML = '';
            
            currentBatch.forEach((p) => {
                const isSelected = batchSelections[batchIndex].has(p.id);
                container.innerHTML += `
                    <div class="pokemon-card ${isSelected ? 'selected' : ''}" id="card-${p.id}" onclick="toggleSelect(${p.id})">
                        <img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/${p.id}.gif" alt="${p.name}">
                        <p class="name">${p.name}</p>
                        <div class="type-container">${renderTypes(p.types)}</div>
                        <p class="species">${p.desc}</p>
                    </div>
                `;
            });
            
            document.getElementById('current').textContent = batchIndex + 1;
            document.getElementById('progress-fill').style.width = 
                `${((batchIndex + 1) / totalBatches) * 100}%`;
            
            document.getElementById('selection-count').textContent = 
                `${getTotalFavorites()} favorites selected`;
            
            updateButtons();
        }
        
        function toggleSelect(id) {
            const card = document.getElementById(`card-${id}`);
            const currentSet = batchSelections[batchIndex];
            
            if (currentSet.has(id)) {
                currentSet.delete(id);
                card.classList.remove('selected');
            } else {
                currentSet.add(id);
                card.classList.add('selected');
            }
            
            document.getElementById('selection-count').textContent = 
                `${getTotalFavorites()} favorites selected`;
        }
        
        function updateButtons() {
            const backBtn = document.getElementById('back-btn');
            const nextBtn = document.getElementById('next-btn');
            const isLast = batchIndex >= totalBatches - 1;
            
            backBtn.disabled = batchIndex === 0;
            nextBtn.textContent = isLast ? 'Start Ranking! →' : 'Next →';
        }
        
        function prevBatch() {
            if (batchIndex > 0) {
                batchIndex--;
                showBatch();
            }
        }
        
        function nextBatch() {
            batchIndex++;
            
            if (batchIndex >= totalBatches) {
                // Collect all favorites
                favorites = [];
                batchSelections.forEach((set, idx) => {
                    const start = idx * BATCH_SIZE;
                    const end = Math.min(start + BATCH_SIZE, allPokemon.length);
                    const batch = allPokemon.slice(start, end);
                    set.forEach(id => {
                        const p = batch.find(p => p.id === id);
                        if (p) favorites.push(p);
                    });
                });
                
                startPairwiseRanking();
            } else {
                showBatch();
            }
        }
        
        function startPairwiseRanking() {
            if (favorites.length < 2) {
                alert('Please select at least 2 Pokemon to rank!');
                batchIndex = 0;
                init();
                return;
            }
            
            // Hide selection UI
            document.getElementById('batch').style.display = 'none';
            document.getElementById('selection-btns').style.display = 'none';
            document.getElementById('selection-count').style.display = 'none';
            document.getElementById('hint').style.display = 'none';
            
            // Show battle UI
            document.getElementById('battle').style.display = 'flex';
            document.getElementById('undo-row').style.display = 'flex';
            document.getElementById('round-info').textContent = 'Phase 2: Pairwise Ranking';
            document.getElementById('instructions').textContent = 
                `Tap your preferred Pokemon! Ranking ${favorites.length} favorites`;
            
            // Initialize ELO ratings
            ratings = {};
            initialRatings = {};
            favorites.forEach(p => {
                ratings[p.id] = 1000;
                initialRatings[p.id] = 1000;
            });
            
            // Generate comparisons
            generateComparisons();
            
            document.getElementById('total').textContent = comparisons.length;
            currentComparison = 0;
            history = [];
            showComparison();
        }
        
        function generateComparisons() {
            comparisons = [];
            const n = favorites.length;
            
            if (n <= 8) {
                for (let i = 0; i < n; i++) {
                    for (let j = i + 1; j < n; j++) {
                        comparisons.push([favorites[i], favorites[j]]);
                    }
                }
            } else {
                const numRounds = Math.ceil(Math.log2(n)) + 2;
                
                for (let round = 0; round < numRounds; round++) {
                    let shuffled = [...favorites].sort(() => Math.random() - 0.5);
                    for (let i = 0; i < shuffled.length - 1; i += 2) {
                        comparisons.push([shuffled[i], shuffled[i + 1]]);
                    }
                }
                
                const extraComparisons = Math.min(n * 2, 30);
                for (let i = 0; i < extraComparisons; i++) {
                    const idx1 = Math.floor(Math.random() * n);
                    let idx2 = Math.floor(Math.random() * n);
                    while (idx2 === idx1) {
                        idx2 = Math.floor(Math.random() * n);
                    }
                    comparisons.push([favorites[idx1], favorites[idx2]]);
                }
            }
            
            comparisons.sort(() => Math.random() - 0.5);
        }
        
        function showComparison() {
            if (currentComparison >= comparisons.length) {
                showResults();
                return;
            }
            
            const [p1, p2] = comparisons[currentComparison];
            
            document.getElementById('battle-img1').src = 
                `https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/${p1.id}.gif`;
            document.getElementById('battle-name1').textContent = p1.name;
            document.getElementById('battle-types1').innerHTML = renderTypes(p1.types);
            document.getElementById('battle-desc1').textContent = p1.desc;
            
            document.getElementById('battle-img2').src = 
                `https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/${p2.id}.gif`;
            document.getElementById('battle-name2').textContent = p2.name;
            document.getElementById('battle-types2').innerHTML = renderTypes(p2.types);
            document.getElementById('battle-desc2').textContent = p2.desc;
            
            document.getElementById('current').textContent = currentComparison + 1;
            document.getElementById('progress-fill').style.width = 
                `${(currentComparison / comparisons.length) * 100}%`;
            
            document.getElementById('undo-btn').disabled = history.length === 0;
        }
        
        function selectWinner(choice) {
            const [p1, p2] = comparisons[currentComparison];
            const winner = choice === 0 ? p1 : p2;
            const loser = choice === 0 ? p2 : p1;
            
            // Save state for undo
            history.push({
                comparison: currentComparison,
                ratings: { ...ratings }
            });
            
            // Update ELO ratings
            const expectedWinner = 1 / (1 + Math.pow(10, (ratings[loser.id] - ratings[winner.id]) / 400));
            const expectedLoser = 1 / (1 + Math.pow(10, (ratings[winner.id] - ratings[loser.id]) / 400));
            
            ratings[winner.id] += K * (1 - expectedWinner);
            ratings[loser.id] += K * (0 - expectedLoser);
            
            currentComparison++;
            showComparison();
        }
        
        function undoChoice() {
            if (history.length === 0) return;
            
            const lastState = history.pop();
            currentComparison = lastState.comparison;
            ratings = lastState.ratings;
            
            showComparison();
        }
        
        function showResults() {
            document.getElementById('battle').style.display = 'none';
            document.getElementById('undo-row').style.display = 'none';
            document.querySelector('.progress').style.display = 'none';
            document.querySelector('.progress-bar').style.display = 'none';
            document.querySelector('.instructions').style.display = 'none';
            document.querySelector('.round-info').style.display = 'none';
            document.getElementById('results').style.display = 'flex';
            
            const sorted = [...favorites].sort((a, b) => ratings[b.id] - ratings[a.id]);
            
            const topContainer = document.getElementById('top-pokemon');
            topContainer.innerHTML = '';
            for (let i = 0; i < Math.min(6, sorted.length); i++) {
                const p = sorted[i];
                topContainer.innerHTML += `
                    <div class="rank-card">
                        <div class="rank">#${i + 1}</div>
                        <img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/${p.id}.gif" alt="${p.name}">
                        <div class="name">${p.name}</div>
                        <div class="type-container">${renderTypes(p.types)}</div>
                        <div class="desc">${p.desc}</div>
                    </div>
                `;
            }
            
            const fullList = document.getElementById('full-list');
            fullList.innerHTML = '';
            sorted.forEach((p, i) => {
                fullList.innerHTML += `
                    <div class="ranking-item">
                        <span class="position">${i + 1}.</span>
                        <img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/${p.id}.gif" alt="${p.name}">
                        <span class="name">${p.name}</span>
                        <div class="type-container">${renderTypes(p.types)}</div>
                        <span class="score">${Math.round(ratings[p.id])}</span>
                    </div>
                `;
            });
        }
        
        function restart() {
            document.getElementById('batch').style.display = 'grid';
            document.getElementById('selection-btns').style.display = 'flex';
            document.getElementById('selection-count').style.display = 'block';
            document.getElementById('hint').style.display = 'block';
            document.getElementById('battle').style.display = 'none';
            document.getElementById('undo-row').style.display = 'none';
            document.querySelector('.progress').style.display = 'block';
            document.querySelector('.progress-bar').style.display = 'block';
            document.querySelector('.instructions').style.display = 'block';
            document.querySelector('.round-info').style.display = 'block';
            document.getElementById('results').style.display = 'none';
            document.getElementById('instructions').textContent = 'Select all your favorites from this batch!';
            document.getElementById('round-info').textContent = 'Phase 1: Selection';
            
            ratings = {};
            comparisons = [];
            currentComparison = 0;
            history = [];
            
            init();
        }
        
        // Start the app
        init();
    </script>
</body>
</html>
'''

def generate_html():
    # Format Pokemon data as JavaScript array
    pokemon_js = "[\n"
    for id, name, types, desc in GEN2_POKEMON:
        types_js = str(types).replace("'", '"')
        desc_escaped = desc.replace('"', '\\"')
        pokemon_js += f'            {{id: {id}, name: "{name}", types: {types_js}, desc: "{desc_escaped}"}},\n'
    pokemon_js = pokemon_js.rstrip(",\n") + "\n        ]"
    
    # Replace placeholder with actual data
    html = HTML_TEMPLATE.replace("POKEMON_DATA_PLACEHOLDER", pokemon_js)
    
    # Write the HTML file
    output_file = "index.html"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)
    
    print(f"✓ Generated {output_file}")
    print(f"✓ Includes all 100 Gen 2 Pokemon (#152-251)")
    print(f"✓ Open the HTML file in a browser to start ranking!")

if __name__ == "__main__":
    generate_html()
