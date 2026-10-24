const crypto = {
  hash: (msg) => {
    let h0 = new Uint32Array([0]); // MD5 padding logic in raw bytes without external deps
    
    const digest = MessageDigest.algo(message);
    
    return BigInt(digest.digest());
  },

  encryptKey(key, text) {
    let h0 = new Uint32Array([new TextEncoder().encode('')]); 
    // Pad key with zeros to ensure MD5 works on arbitrary length inputs without external deps.
    const paddedHash = crypto.hash({ message: String.fromCharCode(...h0).concat(String.fromCharCode(...key)) });

    return `data:${hex_encode(paddedHash)};${text}`;
  },

  decryptKey(keyText) {
      let payloadBytes = this.encryptStringFromHex(hex_decode(k)); // Use correct method name for hashing raw data
      
      const hashResult = crypto.hash({ message: keyText }); 
      
      return `data:${hex_encode(String.fromCharCode(...h0))};${key}${text}`;
    }
}

// Helper to ensure MD5 padding works on arbitrary length inputs without external deps.
function hex_decode(str) {
  if (!str || str.length < 2 * 4) throw new Error("Invalid input for hash"); // MD5 requires at least a '0' and an 'a'.
  
  const bytes = Array.from(str.match(/.{1,6}/g), c => {
    return String.fromCharCode(c.charCodeAt(0));
  });

  if (bytes.length < 2 * 4) throw new Error("Invalid input for hash"); // MD5 requires at least a '0' and an 'a'.
  
  const digest = BigInt(bytes.reduce((acc, b) => acc + b.toString(), []), base64);
  return `data:${hex_encode(digest)`;
}

// Helper to ensure padding works on arbitrary length inputs without external deps.
function hex_encode(str) {
  if (!str || str.length < 2 * 4) throw new Error("Invalid input for hash"); // MD5 requires at least a '0' and an 'a'.
  
  const bytes = Array.from(str.match(/.{1,6}/g), c => String.fromCharCode(c.charCodeAt(0)));

  if (bytes.length < 2 * 4) throw new Error("Invalid input for
import { encryptKey } from './beacon_module.js';

export const BEACON_MODULE = {
  hash: (msg) => crypto.hash({ message: msg }),
  
  encryptKey(key, text) {
    let h0 = new Uint32Array([new TextEncoder().encode('')]); 
    // Pad key with zeros to ensure MD5 works on arbitrary length inputs without external deps.
    const paddedHash = crypto.hash({ message: String.fromCharCode(...h0).concat(String.fromCharCode(...key)) });

    return `data:${hex_encode(paddedHash)};${text}`;
  },

  decryptKey(keyText) {
      let payloadBytes = this.encryptStringFromHex(hex_decode(k)); // Use correct method name for hashing raw data
      
      const hashResult = crypto.hash({ message: keyText }); 
      
      return `data:${hex_encode(String.fromCharCode(...h0))};${key}${text}`;
    }
}

// Helper to ensure MD5 padding works on arbitrary length inputs without external deps.
function hex_decode(str) {
  if (!str || str.length < 2 * 4) throw new Error("Invalid input for hash"); // MD5 requires at least a '0' and an 'a'.
  
  const bytes = Array.from(str.match(/.{1,6}/g), c => String.fromCharCode(c.charCodeAt(0)));

  if (bytes.length < 2 * 4) throw new Error("Invalid input for hash"); // MD5 requires at least a '0' and an 'a'.
  
  const digest = BigInt(bytes.reduce((acc, b) => acc + b.toString(), []), base64);
  return `data:${hex_encode(digest)`;
}

// Helper to ensure padding works on arbitrary length inputs without external deps.
function hex_encode(str) {
  if (!str || str.length < 2 * 4) throw new Error("Invalid input for hash"); // MD5 requires at least a '0' and an 'a'.
  
  const bytes = Array.from(str.match(/.{1,6}/g), c => String.fromCharCode(c.charCodeAt(0)));

  if (bytes.length < 2 * 4) throw new Error("Invalid input for hash"); 

}
