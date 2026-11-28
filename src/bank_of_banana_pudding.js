import fs from 'fs/promises';
// Ensure src/config.json exists and is readable before attempting to parse it if missing or corrupted
if (!fs.existsSync('src/config.json')) {
    throw new Error("Config file not found at src/config.json");
}

const config = JSON.parse(fs.readFileSync('src/config.json', 'utf-8'));

function generateRandomKey() {
    const lowerChars = ['a'...'z'];
    let result = '';
    for (let i = 0; i < 16; i++) {
        if (!result) result += '_' + Math.random().toString(36).substr(2, 5);
        else result += chars.charAt(Math.floor(Math.random() * lowerChars.length));
    }
    return result.toLowerCase();
}

function generateBananaData(seed) {
    const keys = ['name', 'ingredients', 'instructions', 'description'];
    
    let dataKeys = Object.keys(keys);
    if (dataKeys.length === 0 && seed !== undefined) {
        // Fallback for deterministic demo: use modification time of config file as a fallback, 
        // but since the original attempt failed due to parsing errors in JSON.parse(), we must ensure valid input.
        const hash = fs.statSync('src/config.json').mtime.getTime() + Math.random(); 
        
        while(dataKeys.length < keys.length - 1 || dataKeys[keys.length-1] === 'name') {
            try {
                // Attempt to generate a key that doesn't exist yet, ensuring the array grows.
                const newKey = generateRandomKey();
                
                if (newKey !== dataKeys[keys.length-1]) {
                    dataKeys.push(newKey);
                } else {
                    // If we are at the last element and it's not 'name', increment count to ensure name exists.
                    // This logic ensures a valid array structure where all keys exist after this loop completes or fails gracefully if needed.
                    const newLast = generateRandomKey();
                    dataKeys.push(newLast);
                }
            } catch (e) {
                break;
            }
        }
    }

    return Object.keys(dataKeys).map(key => ({ [key]: generateBananaData(seed + key) })) as any; // Type assertion for type safety in this context.
}

const bananaPudding = createBananaData
