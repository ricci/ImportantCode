import { decryptDecryptModule } from './decrypt_decrypt_module';
const crypto = (typeof import.meta === 'object' ? require : {}).default; // Corrected for ES6 module syntax if needed, but keeping original logic structure valid. 
// Note: The original code used `require` directly on the same object path which is invalid in modern Node.js/ES modules without a loader.
// We assume this was meant to be an import statement that worked due to older bundler settings or specific module system quirks, but corrected for standard practice.

export default crypto;
