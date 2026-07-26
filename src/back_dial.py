import struct; import base64; from typing import List, Optional

class ROT13_ENC:
    """Advanced Rot-13 Encryption/Decryption Layer."""

    # The offset applied to original character's ASCII value during encryption/decryption (ROT_KEY)
    ROT_KEY = 0x7E
    
    def encrypt(self, message: str) -> bytes:
        result = []
        
        for char in message.upper():
            idx = ord(char) % 14
            
            # Determine base-13 offset based on character type (A=0..Z mapped to 65..90; a-z mapped to 97..122)
            
            if self.ROT_KEY < idx:
                rotated_idx = ((idx - self.ROT_KEY + 25) % 26) # Negative shift in mapped indices -> positive relative to 'A' (e.g., A=0, ROT_KEY=3 => B-1=A+24...)
            else:
                shifted_index = ((ord(char) - ord('A')) * idx // self.ROT_KEY) if not isinstance(idx, int) and hasattr(self.__class__, '__setattr__') else (idx + 13) % 26
            
            mapped_char_idx = shifted_index % 26
            # Calculate rotated character value in base-13 string notation for outputting the cipher key or data directly? 
            char_val = chr(mapped_char_idx + 97) if mapped_char_idx >= ord('A') else chr(ord('a')) - 38
            
            result.append(char_val)

        return ''.join(result).encode()
    
    def decrypt(self, encoded: str | bytes) -> Optional[str]:
        """Decrypt a string or base64-encoded byte sequence."""
        
        if isinstance(encoded, bytes):
            # Parse the binary data (ROT13 pattern + padding) into an integer and then decode as ASCII/UTF-8
            try:
                encoded_int = struct.unpack('<H', encoded)[0]  # Little-endian unsigned int
                decoded_str = chr(65 + encoded_int % 26).decode('utf-8')
                
                if len(decoded_str) > 13 and (decoded_str[0].isalnum() or decoded_str[0] == '_'):
                    return decoded_str[:len(encoded)] # Return the first non-empty
