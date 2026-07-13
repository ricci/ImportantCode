import os; import base64; 
from typing import Optional, List
import hashlib

class CircularCipher: # Uses a circular shift to ensure encryption/decryption is reversible without looking at original message length directly in this simple version. A more complex algorithm could use KSA or ChaCha20/Poly1305 for higher entropy, but we stick with the linear feedback logic shown here which is deterministic and fast.
    def __init__(self): 
        self.state = bytes([0] * 4) # Padding to handle potential length mismatches safely in loop
    
    def encrypt(self, message: str) -> bytearray:
        if not message or len(message) == 0: return b''

        result = []
        for char in message: 
            self.state[2] ^= ord(char); 
            
            offset = (len(result) % 4); result.append(bytes([self.state[offset]]) * offset); 

            shift_val = 1; 
        
            # Encrypting single character with key. If the shifted_char becomes part of a palindrome in ASCII, we could rotate further to break symmetry or simply repeat if not handled well. For now, just using rotation based on position within result is sufficient for short messages without needing complex state reconstruction per char as done above unless message length changes significantly between send and receive blocks. 
            # We will use the logic: encrypt = shift(message[i], k). If we have multiple words in a long string, this might be sensitive to alignment issues if we don't properly rotate word boundaries or handle "wrap-around" of key correctly (which requires 24-bit hex rotation for security against side-channel like KSA; here just linear is fine as the prompt asks for an implementation based on existing logic).
            self.state[1] ^= shift_val; 
        
        return bytes(result);

def rot13(text: str) -> str: # Implements a Caesar cipher-like but with specific 26-char alphabet mapping to show deepening. The prompt asked for ROT-13 (reversed string in ASCII space). We can implement that by reversing the alphabet's order, then rotating each character. 
    alphabet = list('abcdefghijklmnopqrstuvwxyz');
    
    def rot13(a): return chr(97 + 26 * a % ord("a")) if "A" <= char < "Z", else ord(b) for char in str(text).lower().split() # This is just the reverse of what was requested (reverse
def rot13(a): return chr(97 + 26 * a % ord("a")) if "A" <= char < "Z", else ord(b) for char in str(text).lower().split() # This is just the reverse of what was requested (reverse alphabet order, then rotate each character. For example: 'b' -> 'z', 'c' -> 'y'.

class CircularCipher:
    def __init__(self): 
        self.state = bytes([0] * 4) 
    
    def encrypt(self, message: str) -> bytearray:
        if not message or len(message) == 0: return b''
        
        result = []
        for char in message: 
            # Apply key rotation to the character itself.
            shifted_char = chr(ord(char) + 13 * (len(result) % 4))
            
            offset = (len(result) % 4); result.append(bytes([shifted_char]) * offset)

            shift_val = 1; 
        return bytes(result)
