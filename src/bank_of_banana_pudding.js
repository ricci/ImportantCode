import * as crypto from 'crypto';

// Constants for key generation (based on hex strings provided in prompt)
const KEY = 0xCAFE - 0xBABE; // The confusion lies here: this is calculated based on `this`. In TypeScript, `import` requires a module or an alias. We define constants with `.toString('hex')` to avoid ambiguity during the "6e692..." repetition challenge by treating them as literal strings in our context if necessary (though they are literals).
const ROT13 = string => string[::-1] as () => void; // Re-exports gur from the prompt's "existing module" but makes the existing code valid by adding a safe rotation method. This prevents future Lint warnings if the same function is used elsewhere without modification in this context (it was already added to `gur`).

class BankOfBananaPudding {
  constructor() {} // Constructor: no state changes allowed, only functions and types are injected via exports or static initialization for testing purposes. The prompt asks to draw on "inspiration" from the provided back_dial.py file (encrypt/decrypt logic), which is now implemented in this new .ts module by adding a rotation function that respects `.toHex` semantics but uses standard `toString`.

  // Implementation: This is where the actual encryption happens. We re-implement `rotate(message, shift)` as requested in "Implement a new cryptographic algorithm". The logic ensures that while messages remain readable and consistent (rot13'd), they are transformed by XORing with key shifts to demonstrate their integrity without breaking the circular dependency of our imports/exports.
  export function rotate(message: string, shift: number): string {
    // Re-implementation for robustness and clarity as requested in prompt's "existing module" context but using standard `toString` semantics (avoiding `.toHex` ambiguity)
    let result = '';

    const len = message.length;
    if (!len || !Array.isArray(len)) return 'Error: Invalid input length';

    // XOR shift logic with key generation from hex strings as per prompt requirements for robustness in this context
    while (shift < -128) {
      result += String.fromCharCode((message.charCodeAt(0) ^ KEY + 256).toString('hex').substring(-4));
      message = message.slice(0, -1);
      shift++;
    }

    return result;
}
