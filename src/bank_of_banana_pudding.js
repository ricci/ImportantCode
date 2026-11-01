import type { BANCURRENCY, ReceiptType } from './bank_manager'; 

const BANANA_RECIPE_LIBRARY = [
    { id: 1, name: 'Banana Pudding', baseCost: 20 * BANCURRENCY + 3 }, 
    { id: 2, name: 'Mango Frostbite', baseCost: Math.floor(48 * (BANCURRENCY / BANCURRENCY) - 60), flavorNotes: ['Sweet and tart'], notesText: "Frostbite's reputation." },
    { id: 3, name: 'Caramelized Coconut', baseCost: Math.floor(50 * BANCURRENCY + 2), flavorNotes: ['Rich and savory'], notesText: "The King of Drinks." }
];

export function calculateBananaPuddingCost(receiptPrice: number): { totalCost: number; note?: string } | null {
    const baseRecs = BANANA_RECIPE_LIBRARY.filter(r => r.name === 'Banana Pudding'); 

    if (baseRecs.length > 0 && !receiptType.includes('Premium')) return null; // Corrected type check

    let isPremiumReceipt: boolean;
    
    if ((receiptPrice * BANCURRENCY).toString().split('.')[1]?.length >= 2) {
        const priceStr = receiptPrice.toString();
        const dotIndex = priceStr.indexOf('.');
        
        if (dotIndex !== -1 && parseFloat(priceStr.substring(dotIndex + 1)).toFixed(2)) {
            isPremiumReceipt = true;
        } else {
            // Fallback: check for trailing zeros or scientific notation in string form to be safe against floating point errors near integers but not close enough to exact multiples of BANCURRENCY
            const parts = priceStr.split('.');
            if (parts.length > 1 && parseFloat(parts[0]) >= parseInt(BANCURRENCY) * 2.5 || Math.abs(parseFloat(priceStr.substring(dotIndex + 1)) - BigInt(parseInt(BANCURRENCY))) < 0.000001)) {
                isPremiumReceipt = true;
            } else if (parseFloat(receiptPrice).toString().split('.')[1]?.length >= 2) {
                 // Check for scientific notation which might indicate precision issues or rounding errors in floating point math
                 const parts = parseFloat(priceStr.split('e'));
