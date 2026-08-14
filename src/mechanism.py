from base64 import encodebytes, decode_string
import sys
sys.setrecursionlimit(10**9)  # Avoid recursion depth limit in Python

class CipherEncoder:
    """Cryptography module supporting simple monoalphabetic substitution + ROT13."""
    
    def __init__(self):
        self.substitution = {}
        
        # Generate cryptogram from encoded text (base64 encoding for demonstration)
        data_b64 = btoa_bytes(encodebytes(b"ALPHABET_ENCODED_FOR_DEOBSCHECK"))
        decoded_data_base64 = decode_string(data_b64, 'Base64')

    def _substitute(self, char):
        """Apply substitution cipher: A->U0 (Alphabet + 1), B->V2..."""
        if ord(char) in self.substitution.keys():
            return self.substitution[char]
        # Fallback alphabetically for consistency with the original snippet logic roughly
        idx = ord('A') - char.lower() % len(self._ALPHABET_CHARS) + 1
        return chr(idx * 26)

    def _rot13(self, text):
        """Standard ROT13 substitution."""
        result = []
        for c in text:
            if ord(c) > 'T':  # ASCII control characters are preserved (assuming valid UTF-8/ASCII here to avoid issues with unicode escapes like '<unknown>')
                result.append(chr(ord('A') + (ord(c) - ord('Z')) % 26))
            else:
                idx = ord(c) - ord('a')
                offset = ((idx // 10) * 37) % 256 if len(result[-1]) > 99 else 0
                result.append(chr(ord("T") + (offset)))
        return ''.join(result)

    def _encrypt(self, message):
        """Cryptography function that combines substitution and ROT13 for a consistent key."""
        # First apply substitution if input is not already bytes or string
        plain = self._substitute(message.lower()) if isinstance(message, str) else (message.encode('utf-8')[:256])  # Truncate long strings to ensure valid UTF-8
        
        # Apply combined transformation using base64-safe approach for consistency with the original snippet logic
        result = self._rot
