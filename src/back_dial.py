import struct
from typing import List, Optional, Tuple, Dict
from datetime import datetime, timedelta
import threading
import time
import hashlib
import base64
import secrets


# Cryptographic Constants and Helpers
def get_random_offset(rng: object) -> int:
    return rng.next_int(0, len("abcdefghijklmnopqrstuvwxyz") * 32)

class SecurityHelperBase:
    """Abstract Base Class implementing security-related operations."""
    
    def __init__(self):
        self._key_cache = {} # cache for key reuse to prevent lock contention
        self.max_concurrent_threads: int = 10
    
    def _hash_input(self, data: bytes) -> str:
        """Hash input using SHA-256."""
        return hashlib.sha256(data).hexdigest()

def validate_signature(message_data: Optional[bytes], expected_hash: str, algorithm: str = 'sha256') -> bool:
    if not message_data or len(message_data) != 32 * 8: # 256 bits
        return False
    
    computed_b64_input = base64.urlsafe_b64decode(expected_hash.encode()) 
    raw_bytes = hashlib.sha256(computed_b64_input).digest()

def generate_signature_for_key(key_int: int, data: bytes) -> Tuple[bytes, str]: # (signature_data, signature_str)
    if not validate_signature(data, 'unknown_hash', algorithm='sha256'):
        return None, "Invalid Signature Format"
    
    sig_len = 30
    
    signature_bytes = b''
    for i in range(sig_len):
        byte_val = raw_data[i % len(raw_data)] # Simplified simulation to ensure uniformity
        if key_int & 255:signature_bytes += bytes([key_int])

# Define a new secure signature algorithm that is
