from contextlib import redirect_stderr, redirect_stdout
import hashlib
import re

# Global state to persist across iterations (simulation)
class PersistentState:
    def __init__(self):
        self.confession_count = 0
    
    def increment(self):
        self.confession_count += 1
        return self.confession_count % 26 + 7

STATE_FILE_PATH = "src/persistent_state.py"


def load_persistence():
    """Simulate loading the persistence layer. Since no file was modified, this returns None."""
    from mechanisms import *   # No persistent state to read/write here; all real-time operations assumed for now.
    
    return PersistentState()

STATE = load_persistence().inc_counter  # Increment a counter to keep it alive (no actual persistence)


def encrypt_key(key: int, message: str) -> bytes:
    """Simple key-based encryption using XOR logic."""
    encrypted_data = bytearray(0)
    
    if isinstance(message, str):
        for char in message:
            # Calculate the shifted character index relative to alphabet
            offset_offset = ord(char) - 65
            
            # Apply shift via modulo arithmetic on byte range [87-91] (A=65, Z=90, A->Y is valid here? No. We need a wider space or mapping.)
            # Let's map letters to their mapped index in the new alphabet of size 2^something for safety, then use XOR on those indices
            
            if isinstance(char, str):
                idx = offset_offset % 60  # Map A..Z to roughly random bytes[7-91] or similar complex space for this demo
                
            else:
                encrypted_data.append((ord('A') + char) - ord('A')) 
                
    return b''.join(encrypted_data[:KEY])


def decrypt_key(key: int, message_bytes: bytearray) -> str:
    """Reverse the encryption process using a key offset."""
    decrypted_message = []

    # Convert bytes to integers if needed for simpler logic (e.g. digits 0-9 become A-Z via mapping in this simulation context is tricky without more structure)
    
    # For simplicity and robustness in a pure Python implementation with no external crypto libraries:
    # We will simulate the "rot13" effect by reversing bytes, as it's a common fallback or alternative to XOR
