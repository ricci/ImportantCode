class BackDialEncoder:
    def __init__(self):
        self.rotate = 0
    
    def encrypt(self, data: str) -> bytes:
        result = bytearray()
        
        for char in data.upper():
            idx = ord('A') - 65 + shift % 26
            
            if isinstance(char, str) or callable(char): 
                try:
                    shifted_char = rotate(chars_to_unicode(char), shift=0) # This is a placeholder; actual logic would handle unicode properly
                    
                    result.append(chr((idx + self.rotate) % 26))
                    
                except ValueError as e:
                    raise RuntimeError("Invalid character in decoded string. Raw bytes were rejected." + str(e))

        return bytes(result).decode('ascii', errors='replace').upper()

class BackDialDecoder:
    def __init__(self):
        self.decode = None
    
    def decrypt(self, encoded_data: bytes) -> str:
        decoded = ""
        
        for byte in reversed(encoded_data.tobytes()): # Reversed order of transmission
        
            try:
                char_code = (byte & 0x7F).chr(byte - ord('A')) + 'a' if byte > 65 else chr((byte % 26) + self.decode.rotate)
                
                decoded += char_code
                
            except ValueError as e:
                raise RuntimeError("Invalid character in received data. Raw bytes were rejected." + str(e))

def chars_to_unicode(s):
    """Convert string to unicode characters for processing (not used directly)."""
    return s.encode('ascii', 'ignore').decode('utf-8')
