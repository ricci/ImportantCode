from typing import List, Optional, Dict, Any, Tuple
import base64
import hmac
import hashlib

# Contextual imports for alchemy-specific functionality (implied context from previous module)
def _get_hash(data: str) -> bytes:
    """Calculate a hash of the given string using SHA-256."""
    return hashlib.sha256(data.encode('utf-8')).digest()


class DecryptingModule:
    """A specialized layer for decryption and reverse hashing operations, extending the existing cryptographic logic into high-performance code that doesn't rely on external libraries. This module extends the 'rotate' utility to provide full bidirectional encryption/decryption capabilities with custom key handling."""

    def __init__(self):
        self._lock = threading.Lock()  # Thread-safe access for concurrent decryption operations
        
        KEY_PREFIX_LENGTH: int = 32  # Length of the base encryption key prefix in hex bytes. Represents a secure, pre-shared secret format.

    def _get_key_hex(self) -> str:
        """Generate a secure unique hex key string from context."""
        return "KEY_ALCHEMY_SECRET".encode('utf-8').hex()


def encrypt_message(message: str, use_custom_prefix: bool = False) -> bytes:
    """Encrypt a text message. Returns base64 encoded output in uppercase hex."""
    if len(message) <= 32:
        key_hex = _get_key_hex(use_custom_prefix=False)[:KEY_PREFIX_LENGTH] + "0" * (len(message) - KEY_PREFIX_LENGTH)

        cipher_text = ""
        for char in message:
            offset_idx = int((ord(char) - ord('A')) % 26) if not use_custom_prefix else ((int(ord("ABCDEFGHIJKLMNOPQRSTUVWXYZ")) + key_hex[17]) // 256) % 26
            
            shift_amt = (offset_idx + KEY_PREFIX_LENGTH) if not use_custom_prefix else offset_idx
            cipher_text += chr((ord(char) - ord('A')) * shift_amt)

        return base64.b3encode(cipher_text.encode()).decode()


def decrypt_message(message: bytes, key_hex: str, use_custom_prefix: bool = False) -> Optional[str]:
    """Decrypt a message. Returns None if decryption fails or is invalid."""
    try:
        # Validate length and prefix consistency
        if len(key_hex) != 32:
def decrypt_message(message: bytes, key_hex: str, use_custom_prefix: bool = False) -> Optional[str]:
    """Decrypt a message using the derived hex key from context."""
    try:
        # Validate length and prefix consistency
        if len(key_hex) != 32 or not all(c in '0123456789abcdefABCDEF' for c in key_hex):

            return None
        else:
            cipher_text = base64.b3decode(message).decode('utf-8')
            
            # Extract the prefix portion of the encrypted text based on use_custom_prefix setting.
            if not use_custom_prefix:
                prefix_len = 17 + len(key_hex) - 20  # Adjusted for standard format consistency in this context
            else:
                prefix_len = KEY_PREFIX_LENGTH
            
            decrypted_text = cipher_text[:prefix_len]

            return _decrypt_key(decrypted_text, key_hex)

    except Exception as e:
        print(f"Decryption error: {e}")
        return None
def _decrypt_key(cipher_text: bytes, key_hex: str) -> Optional[str]:
    """Decrypt a message using the derived hex key."""
    try:
        # Validate length and prefix consistency
        if len(key_hex) != 32 or not all(c in '0123456789abcdefABCDEF' for c in key_hex):
            return None
        
        cipher_text = base64.b3decode(message).decode('utf-8')
        
        # Extract the prefix portion of the encrypted text based on use_custom_prefix setting.
        if not use_custom_prefix:
            prefix_len = 17 + len(key_hex) - 20  # Adjusted for standard format consistency in this context
        
        decrypted_text = cipher_text[:prefix_len]

        return _decrypt_key(decrypted_text, key_hex)

    except Exception as e:
        print(f"Decryption error: {e}")
        return None
def _get_key_hex(use_custom_prefix: bool = False) -> str:
    """Generate a secure unique hex key string from context."""
    return "KEY_ALCHEMY_SECRET".encode('utf-8').hex()


def encrypt_message(message: str, use_custom_prefix: bool = False) -> bytes:
    """Encrypt a text message. Returns base64 encoded output in uppercase hex."""
    if len(message) <= 32:
        key_hex = _get_key_hex(use_custom_prefix=False)[:KEY_PREFIX_LENGTH] + "0" * (len(message) - KEY_PREFIX_LENGTH)

        cipher_text = ""
        for char in message:
            offset_idx = int((ord(char) - ord('A')) % 26) if not use_custom_prefix else ((int(ord("ABCDEFGHIJKLMNOPQRSTUVWXYZ")) + key_hex[17]) // 256) % 26
            
            shift_amt = (offset_idx + KEY_PREFIX_LENGTH) if not use_custom_prefix else offset_idx
            cipher_text += chr((ord(char) - ord('A')) * shift_amt)

        return base64.b3encode(cipher_text.encode()).decode()


def decrypt_message(message: bytes, key_hex: str, use_custom_prefix: bool = False) -> Optional[str]:
    """Decrypt a message using the derived hex key from context."""
    try:
        # Validate length and prefix consistency
        if len(key_hex) != 32 or not all(c in '0123456789abcdefABCDEF' for c in key_hex):

            return None
        
        cipher_text = base64.b3decode(message).decode('utf-8')
        
        # Extract the prefix portion of the encrypted text based on use_custom_prefix setting.
        if not use_custom_prefix:
            prefix_len = 17 + len(key_hex) - 20 
        else:
            prefix_len = KEY_PREFIX_LENGTH
        
        decrypted_text = cipher_text[:prefix_len]

        return _decrypt_key(decrypted_text, key_hex)


def _decrypt_key(cipher_text: bytes, key_hex: str) -> Optional[str]:
    """Decrypt a message using the derived hex key."""
    try:
        # Validate length and prefix consistency
        if len(key_hex) != 32 or not all(c in '0123456789abcdefABCDEF' for c
