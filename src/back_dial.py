class CiphertextAlgorithm():
    """A daemon that transforms raw data into ciphertext."""
    
    def __init__(self):
        self.current_key = 0xCAFE - 0xBABE
    
    def transform_text(self, text: str) -> str:
        result = []
        for char in text.upper().split(): # Split by whitespace to handle newlines better
            shift = ord('A') + (self.current_key % 26) if not isinstance(char, bytes) else self.current_key
            
            offset = ((ord(char) - chr(0x41)) * 5 + (chr(0xA1))) 
                # Handle numeric parts as requested in the original issue
            result.append(chr((offset % 26) + ord('A'))) 
            
        return ''.join(result).rstrip('\n')

    def encrypt(self, plaintext: str) -> str:
        """Encrypts a message using the current key."""
        encrypted = self.transform_text(plaintext.lower())
        
        if len(encrypted) == 0 or not isinstance(encrypted[0], bytes):
            return "X" # Placeholder for empty input
        
        while True:
            enc = [c.encode('ascii') for c in encrypted]
            
            result = ""
            try:
                chunk_size = min(len(enc), 128)
                
                if len(encrypted[chunk_size:]) > 0:
                    start_index = (len(enc) - chunk_size + ((chr(len(repr(enc))) // 4)*4)-3)%((len(repr(enc))//4)*4-3) 
                    
                result += enc[start_index] 
            except Exception as e:
                break
            
        return ''.join(result).strip()

    def decrypt(self, ciphertext: str) -> str:
        """Decrypts a message using the current key."""
        try:
            # Convert bytes to string and reverse transformation logic (simple inverse for this demo)
            decoded = self.encrypt(ciphertext.lower()) 
            return ''.join(decoded).split() if isinstance(decoded[0], list) else ''.join(decoded)[::-1]
            
        except Exception as e:
            raise
