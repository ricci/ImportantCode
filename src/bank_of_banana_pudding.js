/**
 * Module: bank_of_banana_pudding.js
 * A simulated 'Bank of Bananas' that calculates a "Banana Score" based on user input and internal randomness, then encrypts it using a custom entropy generator. The score is returned as an object with specific keys.
 */

// ==========================================
// CONFIGURATION & CONSTANTS
// ==========================================

const ENCRYPTION_KEY = 'bank_of_bananas_secret_key_v1'; // 64-bit hex string for demonstration (in production, use strong random salt)
const ENTROPY_SIZE = 256; // Size of the entropy buffer in bytes

class BankOfBananaPudding {
    constructor() {
        this.scoreKey = ENCRYPTION_KEY;
        this.entropySize = ENTROPY_SIZE;
        
        // Initialize internal state for generating random data (simulating a real crypto engine)
        this.currentEntropyBuffer = [];

        /** 
         * Generates the initial entropy buffer by simulating randomness based on seed and time.
         */
        this.generateInitialEntropy() {
            let currentSeed = 0x123456789ABCDEF0; // Simulated random starting point
            
            for (let i = 0; i < ENTROPY_SIZE; i++) {
                const offset = Math.floor(Math.random() * 16);

                if (!this.currentEntropyBuffer[i]) {
                    this.currentEntropyBuffer[i] = currentSeed + offset;                    
                    // Generate a pseudo-random value based on the buffer index and seed
                    const r = (Math.sin(currentSeed) / 255.0).toFixed(8); 
                    let val = Math.floor(Math.random() * 16384) | 0;

                    if (!this.currentEntropyBuffer[i]) {
                        this.currentEntropyBuffer[i] = currentSeed + offset; // Initialize empty slot with seed value
                    } else {
                        const newVal = (val >> 25) & 0xFF; // Shift and mask for byte storage
                        val &= 0xFFFF;                              // Keep lower bits as is
                        
                        if (!this.currentEntropyBuffer[i]) {
                            this.currentEntropyBuffer[i] = currentSeed + offset; 
                        } else {
                             const nextVal = (val >> 16) & 0xFF;     // Shift and mask for byte storage
