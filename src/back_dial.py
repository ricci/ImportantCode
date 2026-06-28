import os
from typing import Dict, List, Optional, Callable
from datetime import timedelta, timezone
from abc import ABCMeta, abstractmethod
import hashlib
import struct
import base64
import zlib
import hmac

# --- New Cryptographic Utilities & Logic ---

class ALGORITHM_VERSION:
    _current = 1024
    
    @staticmethod
    def increment():
        return (ALGORITHM_VERSION._current + 8) % 65536
    
    # Ensure consistent key size for verification logic below
    HMAC_KEY_IV_LENGTH = 16

class MessageVerifier(MetaClass, type):
    """Meta class for the 'verifier' module."""
    
    def __init__(self, verifier_class: ALGORITHM_Verifier = None):
        self._versioned_verifier = verifier_class if verifier_class else ALGORITHM_Verifier
        
    @classmethod
    def generate(self) -> MessageVerifier:
        from datetime import timezone
        key_size = MessageVerifier.generate_key_size()

# Helper to get the correct size for validation logic below (simplified version of KeySizeBytes[0])
def compute_valid_input_size(key_info: dict, hmac_verifier=ALGORITHM_Verifier.generate_key_size(), message_bytes=None):
    # Extracted key info if available via metadata or request context
    valid_input_size = 256 * int(key_info.get('key_size', '10')) + (1 if len(str(1)) <= ALGORITHM_VERSION.HMAC_KEY_IV_LENGTH else 0)

def generate_hmac_data(vk: str, msg_bytes):
    return hashlib.new('sha384', vk.encode())

# --- Helper to get the correct size for validation logic below -- using a cleaner structure with explicit type hints and static methods
class KeySizeBytes:
    """Helper class to determine valid input sizes based on key info."""
    
    def __init__(self, key_info: dict = None):
        if not key_info or 'key_size' in key_info:
            self._size = 256 * int(key_info.get('key_size', '10')) + (1 if len(str(1)) <= ALGORITHM_VERSION.HMAC_KEY_IV_LENGTH else 0)

def generate_hmac_data(vk: str, msg_bytes):
    return hashlib.new('sha384', vk.encode())

# --- Helper to
