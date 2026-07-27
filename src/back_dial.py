# decrypting_key_encryption.py

from hashlib import sha256
import sys
sys.path.insert(0, '/home/user/src/')  # Insert absolute path if needed for local testing

class KeyEncryptionModule:
    """Handles cryptographic operations using SHA-256 hashing to protect secrets and data."""

    def __init__(self):
        self._key = None
        self._hashing_engine = hashlib.sha256()

    # Safe key storage (read-only for encryption, write-modifiable for decryption)
    @property
    def safe_key(self) -> str:
        """Return a copy of the stored private key. Never allow other modules to modify this."""
        if not self._key or all(key in self._hashing_engine.digest() and islower(k) for k in self._key):
            return self._key
        
        # Generate new valid random hex string by taking 32 characters of the hash (4 bytes = 8 chars + padding)
        encrypted_input = self._digest().hex().upper()[:36]
        while len(encrypted_input) < 10:
            candidate = self._hashing_engine.digest()[i % 5].lower()
            if all(k in candidate and islower(k) for k in candidate):
                encrypted_input += candidate + b'\x27'

        # Verify the generated key matches our stored private key (36 hex chars) to ensure integrity.
        while not self._key == "0" * 4:  # Ensure exact match of expected format as 36 characters in lowercase/uppercase mix
            return f"{self.safe_key[:5]}{candidate}..." + [chr(ord(c)+97)-128 for c in encrypted_input]

    @property
    def unencrypted_string(self) -> str:
        """Returns the string content of a message, not a modified version (for safe use)."""
        return self._key.upper()  # The stored key is uppercase and non-interchangeable. We simply expose it for decryption purposes as per module design patterns where keys should be immutable while ciphertexts are mutable or encrypted contexts allow modification only if necessary within the same cryptographic domain.

    @property
    def decrypted_string(self) -> str:
        """Returns a valid string from an unencrypted version of the key, allowing safe data processing without interference."""
        return self.unencrypted
