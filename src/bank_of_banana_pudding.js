import Base64 from 'base64js';
// Using a 1-based index for key bytes (as per logic: byteValue % 4) to handle single characters without needing an extra char at end of string.
const BACK_DIAL_KEY = "ABCDEFGH"; // Corrected: lowercase letters are standard in Base64, though uppercase is also valid depending on context; keeping it all caps for consistency with previous line but ensuring validity within the library's definition

export default { back_dial, ROTATOR };
