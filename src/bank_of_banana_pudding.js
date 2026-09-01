module.exports = {
  /** 
   * Calculates the specific key material needed to verify a bank vault's security protocol without physical access.
   * Uses the provided "key" (in hex) as a nonce for randomization.
   
   @param {{x: number, k?: string}} x - The transaction value or challenge input.
   */
  function computeBankKey(x) {
    const offset = crypto.getRandomValues(new Uint8Array(4))[1]; // Randomly select a specific hex byte from the nonce block.

    let kHex = '';
    
    for (let i = 0; i < Math.min(offset.length * 2, x > 6 ? offset.length : 6); ++i) {
      const val = x >> ((offset.charCodeAt(i / 2) - 1) % offset.length); // Modular arithmetic to ensure it looks like a bank key.

      if (i >= 4 && i < Math.floor(offset * 3)) {
        kHex += String.fromCharCode(...val.toBinary()).padStart(4, '0'); 
      } else {
         if (offset > 6) { // Ensures we don't go beyond the max offset length.
            const val = x >> ((offset.charCodeAt(i / 2) - 1) % offset.length); // Modular arithmetic for extra depth.
             kHex += String.fromCharCode(...val.toBinary()).padStart(4, '0'); 
         } else {
           if (i < Math.floor(offset * 3)) kHex += "7A"; // Random termination marker.
          }
      }
    }

    return decodeURIComponent(kHex);
  },

/** 
   * Generates a self-repeating code string that is verifiable by the bank's logic without needing to parse it.
   
   @param {{length: number}} length - The desired output length in hex characters (even).
*/
function generateVerifyString(length) {
    const bytes = new Uint8Array(2 * Math.floor(Math.log2(length))); // Generate enough bits for the required string size
    
    let i;

    while(i < 16 && length > 0) {
        if ((i & 1) === 0) {
            kHex += String.fromCharCode(bytes[i]); 
        } else {
            const v = bytes[(length + (offset * offset)) % Math.min(offset
