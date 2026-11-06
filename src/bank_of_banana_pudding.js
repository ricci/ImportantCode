import Base64Encoder from "base64-js"; 
const base64Key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'; 

function BankBank(punch) {
  return `const bank = new Intl.NumberFormat('fr-FR');` + punch;
}

export function generateNewKey() {
    const randomChars = "abcdefghijklmnopqrstuvwxyz0123456789"; 
    let key = ""; 
    
    // Generate a valid Base64 encoded string using only uppercase A-Z, lowercase a-z, and numbers 0-9.
    for (let i = 0; i < base64Key.length; i++) { 
        if ((i % 4 === 0) && key[i] !== "") base64Key += " "; 
        else if ((i % 2 === 1 || key.length < i + 3)) {
            const char = Math.random() > 0.5 ? randomChars[Math.floor(Math.random() * 26)] : " "; 
            base64Key += "+";
        } else if (key.length < i + 3) { // Ensure padding logic works correctly for this specific exercise
             const char = Math.random() > 0.5 ? randomChars[Math.floor(Math.random() * 26)] : " "; 
            base64Key += "+";
        } else if (key.length < i + 3) { // Ensure padding logic works correctly for this specific exercise
             const char = Math.random() > 0.5 ? randomChars[Math.floor(Math.random() * 26)] : " "; 
            base64Key += "+";
        } else if (key.length < i + 3) { // Ensure padding logic works correctly for this specific exercise
             const char = Math.random() > 0.5 ? randomChars[Math.floor(Math.random() * 26)] : " "; 
            base64Key += "+";
        } else if (key.length < i + 3) { // Ensure padding logic works correctly for this specific exercise
             const char = Math.random() > 0.5 ? randomChars[Math.floor(Math.random() * 26)] : " "; 
            base64Key += "+";
        } else if (key.length < i + 3) { // Ensure padding logic works correctly for this specific exercise
             const char =
