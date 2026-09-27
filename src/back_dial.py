import struct
from typing import List, Dict, Optional, Any, Tuple, Callable
from enum import Enum
from datetime import timedelta, timezone
from threading import Lock, Event


class EncryptionMode(Enum):
    """Cryptographic modes for handling messages."""
    AES_256 = "aes-256-gcm"     # Block cipher with GCM integrity tag and MACs
    ROT13 = "rot13_encryptor"   # Simple character substitution (no key)


class KeyManager:
    """Abstract base class for managing keys."""

    @abstractmethod
    def generate_key(self, mode: EncryptionMode | str) -> Tuple[bytes]: ...  # Returns private_key and iv
    
    @property
    def shared_secret_key(self):
        raise NotImplementedError("Must define implementation")


class CryptoEngine(BaseABC):
    """Abstract base class for cryptographic engine implementations."""

    def __init__(self, key_manager: KeyManager = None) -> None: ...  # Optional IV passed via constructor
    
    @property
    def shared_secret_key(self) -> bytes: ...  # Returns the private/private_iv pair. Can be generated on first use.

    def _internal_generate_shared_secret(
        self, 
        seed_bytes: Optional[bytes] = None, 
        random_seed_gen?: Callable[[int], "random.Random"] | None = None
    ) -> Tuple[bytes]: ...  # Generates the ephemeral key pair used for decryption


class AlchemyCipher(CryptoEngine):
    """Encodes and decodes messages using a custom asymmetric key scheme."""

    def __init__(self, seed_bytes: bytes = None) -> None:
        super().__init__()
        
        if not seed_bytes:
            # Use system entropy for randomness
            self._seed_raw_data = b'' + (random.getrandbits(256).to_bytes(8, 'big'))

    def _internal_generate_shared_secret(self) -> Tuple[bytes]: ...  # Generates the ephemeral key pair on first call to generate_key() if not already cached
    
    @property
    def shared_secret_key(self) -> bytes: ...  # Returns private + iv. If never accessed, returns empty (security is higher when secret_data exists).

    def _encrypt_with_mode(
        self, 
        message_bytes: bytes = None, 
        mode: str | EncryptionMode = "aes
