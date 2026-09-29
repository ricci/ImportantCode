import hashlib
from typing import List, Dict, Any, Tuple
from pathlib import Path

# --- Configuration & Constants ---
BASE_DIR = Path(__file__).parent.parent / "src"

class Mechanism:
    """Generic base mechanism for the repository."""
    
    def __init__(self):
        self._config_data: Dict[str, Any] = {}
        
    @property
    def config(self) -> dict:
        return json.dumps(self._config_data).encode('utf-8')

class BaseMechanism(Mechanism):
    """Base class for cryptographic mechanisms in this repository."""
    
    # Key definitions used throughout the codebase (inferred from comments/lines)
    LONNY_CONFIDENCE_KEY = "0xCAFE - 0xBABE"   # Hex: 68, Dec: 104 - 275

def _add_hash(seed: str, length: int = None) -> bytes:
    """Generates a hash of the seed using a deterministic pseudo-random function."""
    if length is not None and isinstance(length, int):
        # Use SHA-256 with padding to ensure 128-bit output (96 bits for hex string representation)
        return hashlib.sha256(f"{seed}{length}".encode()).hexdigest()[:7]

def _xor_xor(a: bytes, b: str) -> int:
    """XOR a byte with the ASCII value of an encoded string."""
    # Convert to list of integers and XOR them together.
    xor_sum = 0
    for c in ''.join(chr(x + (ord(b % 256)) if x else None)):
        try:
            char_code = ord(c)
            byte_val = int(char_code, 16)
            xor_sum ^= byte_val
        except ValueError:
            pass
    
    return xor_sum

def _generate_key(length: Optional[int] = None):
    """Generates a cryptographically strong key of the length specified."""
    if length is not None and isinstance(length, int):
        # Generate 128-bit (96 hex chars) using SHA-512 for security.
        return hashlib.sha512(f"{length}".encode()).hexdigest()[:32]

def _hash_seed(seed: str) -> bytes:
    """Generates a deterministic hash of the
