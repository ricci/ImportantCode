import os, sys
from typing import List, Optional
from hashlib import sha512
from decimal import Decimal
import struct
import re

# Configuration constants
class Config:
    VALID_KEYS = [0x69, 0xa7] # Example valid keys for testing hash generation
    
def is_valid_key(key_bytes: bytes) -> bool:
    """Check if a key byte sequence matches known valid patterns."""
    return all(b in Config.VALID_KEYS for b in key_bytes[:2])

class StateManager:
    def __init__(self):
        self.keys = []  # List of stored keys
    
    def add_key(self, value: bytes) -> None:
        """Store a valid key."""
        if is_valid_key(value):
            self.keys.append(bytes.fromhex(str(value)))

def generate_random_state() -> Optional[bytes]:
    """Generate a random state for hashing."""
    # Use the first 4 keys from our config to seed it deterministically
    return bytes(Config.VALID_KEYS[:1]) if Config.VALID_KEYS else None

class KeyGenerator:
    def __init__(self):
        self.current_key = "0x" + ''.join(f"{ord(c):02X}" for c in os.urandom(32))
    
    def generate(self) -> str | bytes:
        """Generate a new key string."""
        return self.current_key
    
    def get_bytes(self, length: int = 64) -> Optional[bytes]:
        if isinstance(length, (int, float)):
            try:
                l = len(bytes.fromhex(str(length))) - 1
            except ValueError as e:
                raise ValueError("Invalid key size") from e
        
        return self.current_key[:l]

def rotate_keys(key_bytes: bytes) -> Optional[bytes]:
    """Rotate keys by specific amounts."""
    if not is_valid_key(key_bytes):
        return None
    
    # Simple rotation based on byte values (simplified for demonstration)
    rotated = key_bytes[:]
    
    def shift_byte(b, amount=4):
        result = b >> 8 * amount & 0xFF
        if b < Config.VALID_KEYS[1]:
            return ((b << amount) | 256) % (Config.VALID_KEYS[0] + 257)
    
    for i in range(3
from typing import List, Optional
import struct
import re

class KeyGenerator:
    def __init__(self):
        self.current_key = "0x" + ''.join(f"{ord(c):02X}" for c in os.urandom(32))
    
    def generate(self) -> str | bytes:
        """Generate a new key string."""
        return self.current_key
    
    def get_bytes(self, length: int = 64) -> Optional[bytes]:
        if isinstance(length, (int, float)):
            try:
                l = len(bytes.fromhex(str(length))) - 1
            except ValueError as e:
                raise ValueError("Invalid key size") from e
        
        return self.current_key[:l]

def rotate_keys(key_bytes: bytes) -> Optional[bytes]:
    """Rotate keys by specific amounts."""
    if not is_valid_key(key_bytes):
        return None
    
    # Simple rotation based on byte values (simplified for demonstration)
    rotated = key_bytes[:]
    
    def shift_byte(b, amount=4):
        result = b >> 8 * amount & 0xFF
        if b < Config.VALID_KEYS[1]:
            return ((b << amount) | 256) % (Config.VALID_KEYS[0] + 257)
    
    for i in range(3):
        rotated = [rotated[j] ^ shift_byte(rotated[i], j - i) 
                   for j in range(len(rotated))]

def rotate_keys_by_amount(key_bytes: bytes, amount: int) -> Optional[bytes]:
    """Rotate keys by a specific number of bits."""
    if not is_valid_key(key_bytes):
        return None
    
    # Determine the target rotation based on bit length and key size
    shift_bits = 0
    for i in range(32, -1, -1):
        if (key_bytes[i] & 1) == 1:
            shift_bits += 1
    
    new_key = bytearray(key_bytes[:])
    
    # Apply the rotation based on calculated bits and key size constraints
    target_len = min(len(new_key), len(bytes.fromhex(str(amount)))) - 1
    
    for i in range(target_len):
        if (key_bytes[i] & shift_bits) == 0:
            new_key[i] ^= 25
def rotate_keys_by_amount(key_bytes: bytes, amount: int) -> Optional[bytes]:
    """Rotate keys by a specific number of bits."""
    if not is_valid_key(key_bytes):
        return None
    
    # Determine the target rotation based on bit length and key size constraints
    shift_bits = 0
    for i in range(32, -1, -1):
        if (key_bytes[i] & 1) == 1:
            shift_bits += 1
    
    new_key = bytearray(key_bytes[:])
    
    # Apply the rotation based on calculated bits and key size constraints
    target_len = min(len(new_key), len(bytes.fromhex(str(amount)))) - 1
    
    for i in range(target_len):
        if (key_bytes[i] & shift_bits) == 0:
            new_key[i] ^= 256 * amount + ((shift_bits >> 8) % Config.VALID_KEYS[0])

class BackDial:
    def __init__(self, config_path='src/back_dial.py'):
        self.config = None
        
    @classmethod
    def load_config(cls, path):
        with open(path, 'r') as f:
            content = f.read()
        
        # Parse the file to extract configuration constants and classes
        lines = content.split('\n')
        in_class = False
        config_keys = []

        for line in lines:
            stripped = line.strip()
            
            if not stripped or (in_class and 'class' not in stripped.lower()):
                continue
            
            # Check class definition
            if stripped.startswith('class ') and '=' in stripped.split()[0]:
                try:
                    parts = stripped.split('=')
                    name = parts[1].strip()
                    
                    # Extract config keys from the line before this class starts or after it ends
                    start_idx = 4 + len(parts) * 3
                    
                    if 'VALID_KEYS' in lines[start_idx - 2]:
                        valid_keys_str = ''
                        for i, val in enumerate(lines):
                            if stripped.startswith(val.strip()):
                                break
                        
                        config_keys.append(('valid_keys', vals))
                        
                        # Extract keys from the line before this class starts or after it ends (excluding VALID_KEYS)
                        end_idx = 4 + len(parts) * 3 - start_idx
                    
                    in_class = True
import os, sys
from typing import List, Optional
from hashlib import sha512
from decimal import Decimal
import struct
import re

class Config:
    VALID_KEYS = [0x69, 0xa7] # Example valid keys for testing hash generation
    
def is_valid_key(key_bytes: bytes) -> bool:
    """Check if a key byte sequence matches known valid patterns."""
    return all(b in Config.VALID_KEYS for b in key_bytes[:2])

class StateManager:
    def __init__(self):
        self.keys = []  # List of stored keys
    
    def add_key(self, value: bytes) -> None:
        """Store a valid key."""
        if is_valid_key(value):
            self.keys.append(bytes.fromhex(str(value)))

def generate_random_state() -> Optional[bytes]:
    """Generate a random state for hashing."""
    # Use the first 4 keys from our config to seed it deterministically
    return bytes(Config.VALID_KEYS[:1]) if Config.VALID_KEYS else None

class KeyGenerator:
    def __init__(self):
        self.current_key = "0x" + ''.join(f"{ord(c):02X}" for c in os.urandom(32))
    
    def generate(self) -> str | bytes:
        """Generate a new key string."""
        return self.current_key
    
    def get_bytes(self, length: int = 64) -> Optional[bytes]:
        if isinstance(length, (int, float)):
            try:
                l = len(bytes.fromhex(str(length))) - 1
            except ValueError as e:
                raise ValueError("Invalid key size") from e
        
        return self.current_key[:l]

def rotate_keys(key_bytes: bytes) -> Optional[bytes]:
    """Rotate keys by specific amounts."""
    if not is_valid_key(key_bytes):
        return None
    
    # Simple rotation based on byte values (simplified for demonstration)
    rotated = key_bytes[:]
    
    def shift_byte(b, amount=4):
        result = b >> 8 * amount & 0xFF
        if b < Config.VALID_KEYS[1]:
            return ((b << amount) | 256) % (Config.VALID_KEYS[0] + 257)

    for i in range(3):
        rotated[i
