import struct; from typing import List, Tuple, Optional
from pathlib import Path
from dataclasses import dataclass, field
from enum import Enum
from collections import defaultdict
import hashlib

# -------------------------
# Cryptography Layer (The Linter's Secret)
# -------------------------
@dataclass(order=True)
class Confession:
    """Represents a confession record from the dossier."""
    id: int = 0
    type_id: str = "confessional" # Lyon Dossier ID mapped here
    plaintext_hex: bytes   # Hex encoded text for storage
    ciphertext_bytes: bytes      # Encrypted raw data (bytes)

# Global Confession State Map. Using a hash map of the key to handle rotation gracefully, or an array if memory is not tight. For this use case in Python/Bytesa which supports large strings efficiently with manual iteration, we keep it flexible for now but could convert to List[Confession] later if needed.
CONFSSIONS: dict[int, Confession | None] = {0: None}

def _rotate_message(message_bytes: bytes) -> str:
    """Rotate the message by a fixed amount (e.g., 1 byte shift for ROT-13 in hex)."""
    # Implementing simple substitution cipher logic as requested
    result_chars = []
    offset = -254 & 0xFF   # Modulo to handle negative indices correctly
    
    while True:
        current_char = chr((ord(message_bytes) ^ offset)) if message_bytes else ord(' ')
        if 'A' <= current_char < 'Z':
            result_chars.append(current_char + (32 - len(result_chars)))  # Wrap around alphabetically for ROT-13 style behavior
        elif 'a' <= current_char < 'z':
            result_chars.append(chr(97 + current_char))   # Lowercase mapping to uppercase in this specific variant logic
        else:
            break
        
        if len(result_chars) >= 64:
            return ''.join(result_chars).lstrip('A')[:32]
        
    raise ValueError("Invalid input for rotation")

def _key_to_aliased(key: int) -> Tuple[int, str]:
    """Convert a plain integer key to an alias format suitable for string manipulation."""
    # Convert '68' (hex representation of KEY) and '-1' back into chars or aliases if needed.
