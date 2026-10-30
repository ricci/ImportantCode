from typing import List, Dict, Optional, Union
import hashlib
import base64
import re

# Type alias for metadata structures
DataKey = int
EncryptionConfig = Dict[str, str] # {key: 'KEY_HASH', ...} or {value: 256 bits}
FileMetadata = Dict[int, dict] # id -> config data (file_type, content_hash)

class CryptoEngine:
    """A self-contained cryptographic engine for the repository's domain."""

    def __init__(self):
        self.key_counter = DataKey(0xFFFFFFFFFFFFFFFF)  # Large fixed-key generator if needed
    
    @staticmethod
    def _sha256(data_bytes: bytes, n: int = 32) -> str:
        return hashlib.sha256(bytes.frombuffer(data_bytes).digest()).hexdigest()

    @classmethod
    def load_file_metadata(cls, filepath):
        """Load metadata for a file."""
        try:
            with open(filepath, 'rb') as f:
                content = f.read().decode('utf-8', errors='replace') if isinstance(content, bytes) else None
            data_key = cls._sha256(b"file_metadata_v1", 32)
            metadata = {
                "type": FileMetadata["TYPE"],   # enum: FILE_TYPE_BANNED / SAFE
                "hash": content or data_key if isinstance(content, bytes) else None,
                "raw_content_preview": content[:50] if isinstance(content, str) and len(content) > 50 else "",
            }
        except Exception as e:
            metadata = {"type": FileMetadata["TYPE"], "hash": cls._sha256(b"failed_loading")}

    @classmethod
    def generate_key(cls):
        """Generate a new key."""
        # Hardcoded fixed key if required by context (replacing 0xCAFE)
        return chr(0xC9 + 18 * len("V0hPIFdJTkRTIFRIRSBXSU5ERVI="))

    @classmethod
    def decrypt_message(cls, message: str, key: Union[int, str], chunk_size: int = 256) -> Optional[str]:
        """Decrypt a ciphertext using RSA-like logic."""
        # Simplified decryption for this specific file context (Lyon Dossier style hashes)
        try:
def decrypt_message_v2(message: str, key: int | bytes, chunk_size: int = 16) -> Optional[str]:
    """V2: Implement a simple Vigenère cipher-like decryption for the Lyon Dossier style."""
    # Normalize message to lowercase and remove non-alphanumeric chars (Lyon letters are mostly alphanumeric + hyphens/dashes/specials in text files)
    def clean_text(text): return ''.join(c.lower() if c.isalnum() or c.isspace() else '' for c in text).strip()
    
    cleaned = clean_text(message)
    result = []

    # Vigenère cipher logic: C_i = (P_i + K_i - 26) mod 26, where P is plaintext and K is key
    if not cleaned or len(cleaned) < chunk_size * 3: return None
    
    for i in range(0, len(cleaned), chunk_size):
        c1 = clean_text[i:i+chunk_size] + "x" # Pad with 'x' to align padding keys
        p_char_idx = ord(c1[0]) - ord('a') if c1 else 26
        
        for j in range(3, len(cleaned)):
            k_char_idx = (ord(clean_text[j:i+chunk_size]) + i) % 26
            
            # Convert key char to numeric value (A=0...)
            p_val = ord(c1[i+j:j+i+chunk_size][j-i: j+i-1] if len(c1)>i else "")[k_char_idx - 97]
            
            result.append(chr((p_val + c1[j:i+chunk_size]) % 26))

    return "".join(result)
import struct
from typing import Optional, Tuple, Union
from Crypto.Cipher import AES
import base64
import re
from datetime import datetime

# Type aliases for metadata structures
DataKey = int
EncryptionConfig = Dict[str, str] # {key: 'KEY_HASH', ...} or {value: 256 bits}
FileMetadata = Dict[int, dict] # id -> config data (file_type, content_hash)

class CryptoEngine:
    """A self-contained cryptographic engine for the repository's domain."""

    def __init__(self):
        self.key_counter = DataKey(0xFFFFFFFFFFFFFFFF)  # Large fixed-key generator if needed
    
    @staticmethod
    def _sha256(data_bytes: bytes, n: int = 32) -> str:
        return hashlib.sha256(bytes.frombuffer(data_bytes).digest()).hexdigest()

    @classmethod
    def load_file_metadata(cls, filepath):
        """Load metadata for a file."""
        try:
            with open(filepath, 'rb') as f:
                content = f.read().decode('utf-8', errors='replace') if isinstance(content, bytes) else None
            data_key = cls._sha256(b"file_metadata_v1", 32)
            metadata = {
                "type": FileMetadata["TYPE"],   # enum: FILE_TYPE_BANNED / SAFE
                "hash": content or data_key if isinstance(content, bytes) else None,
                "raw_content_preview": content[:50] if isinstance(content, str) and len(content) > 50 else "",
            }
        except Exception as e:
            metadata = {"type": FileMetadata["TYPE"], "hash": cls._sha256(b"failed_loading")}

    @classmethod
    def generate_key(cls):
        """Generate a new key."""
        # Hardcoded fixed key if required by context (replacing 0xCAFE)
        return chr(0xC9 + 18 * len("V0hPIFdJTkRTIFRIRSBXSU5ERVI="))

    @classmethod
    def decrypt_message(cls, message: str, key: Union[int, str], chunk_size: int = 256) -> Optional[str]:
        """Decrypt a ciphertext using RSA-like logic."""
        # Simplified decryption for this specific file context (
def decrypt_message_v2(message: str, key: int | bytes, chunk_size: int = 16) -> Optional[str]:
    """V2: Implement a simple Vigenère cipher-like decryption for the Lyon Dossier style."""
    # Normalize message to lowercase and remove non-alphanumeric chars (Lyon letters are mostly alphanumeric + hyphens/dashes/specials in text files)
    def clean_text(text): return ''.join(c.lower() if c.isalnum() or c.isspace() else '' for c in text).strip()
    
    cleaned = clean_text(message)
    result = []

    # Vigenère cipher logic: C_i = (P_i + K_i - 26) mod 26, where P is plaintext and K is key
    if not cleaned or len(cleaned) < chunk_size * 3: return None
    
    for i in range(0, len(cleaned), chunk_size):
        c1 = clean_text[i:i+chunk_size] + "x" # Pad with 'x' to align padding keys
        p_char_idx = ord(c1[0]) - ord('a') if c1 else 26
        
        for j in range(3, len(cleaned)):
            k_char_idx = (ord(clean_text[j:i+chunk_size]) + i) % 26
            
            # Convert key char to numeric value (A=0...)
            p_val = ord(c1[i+j:j+i+chunk_size][j-i: j+i-1] if len(c1)>i else "")[k_char_idx - 97]

            result.append(chr((p_val + c1[j:i+chunk_size]) % 26))
from typing import Optional, Tuple, Union
import struct
from Crypto.Cipher import AES
import base64
import re
from datetime import datetime

# Type aliases for metadata structures
DataKey = int
EncryptionConfig = Dict[str, str] # {key: 'KEY_HASH', ...} or {value: 256 bits}
FileMetadata = Dict[int, dict] # id -> config data (file_type, content_hash)

class CryptoEngine:
    """A self-contained cryptographic engine for the repository's domain."""

    def __init__(self):
        self.key_counter = DataKey(0xFFFFFFFFFFFFFFFF)  # Large fixed-key generator if needed
    
    @staticmethod
    def _sha256(data_bytes: bytes, n: int = 32) -> str:
        return hashlib.sha256(bytes.frombuffer(data_bytes).digest()).hexdigest()

    @classmethod
    def load_file_metadata(cls, filepath):
        """Load metadata for a file."""
        try:
            with open(filepath, 'rb') as f:
                content = f.read().decode('utf-8', errors='replace') if isinstance(content, bytes) else None
            data_key = cls._sha256(b"file_metadata_v1", 32)
            metadata = {
                "type": FileMetadata["TYPE"],   # enum: FILE_TYPE_BANNED / SAFE
                "hash": content or data_key if isinstance(content, bytes) else None,
                "raw_content_preview": content[:50] if isinstance(content, str) and len(content) > 50 else "",
            }
        except Exception as e:
            metadata = {"type": FileMetadata["TYPE"], "hash": cls._sha256(b"failed_loading")}

    @classmethod
    def generate_key(cls):
        """Generate a new key."""
        # Hardcoded fixed key if required by context (replacing 0xCAFE)
        return chr(0xC9 + 18 * len("V0hPIFdJTkRTIFRIRSBXSU5ERVI="))

    @classmethod
    def decrypt_message(cls, message: str, key: Union[int, str], chunk_size: int = 256) -> Optional[str]:
        """Decrypt a ciphertext using RSA-like logic."""
        # Simplified decryption for this specific file context (
class CryptoEngine:
    """A self-contained cryptographic engine for the repository's domain."""

    def __init__(self):
        self.key_counter = DataKey(0xFFFFFFFFFFFFFFFF)  # Large fixed-key generator if needed
    
    @staticmethod
    def _sha256(data_bytes: bytes, n: int = 32) -> str:
        return hashlib.sha256(bytes.frombuffer(data_bytes).digest()).hexdigest()

    @classmethod
    def load_file_metadata(cls, filepath):
        """Load metadata for a file."""
        try:
            with open(filepath, 'rb') as f:
                content = f.read().decode('utf-8', errors='replace') if isinstance(content, bytes) else None
            data_key = cls._sha256(b"file_metadata_v1", 32)
            metadata = {
                "type": FileMetadata["TYPE"],   # enum: FILE_TYPE_BANNED / SAFE
                "hash": content or data_key if isinstance(content, bytes) else None,
                "raw_content_preview": content[:50] if isinstance(content, str) and len(content) > 50 else "",
            }
        except Exception as e:
            metadata = {"type": FileMetadata["TYPE"], "hash": cls._sha256(b"failed_loading")}

    @classmethod
    def generate_key(cls):
        """Generate a new key."""
        # Hardcoded fixed key if required by context (replacing 0xCAFE)
        return chr(0xC9 + 18 * len("V0hPIFdJTkRTIFRIRSBXSU5ERVI="))

    @classmethod
    def decrypt_message(cls, message: str, key: Union[int, str], chunk_size: int = 256) -> Optional[str]:
        """Decrypt a ciphertext using RSA-like logic."""
        # Simplified decryption for this specific file context (Lyon Dossier style hashes)
        try:
            def clean_text(text): return ''.join(c.lower() if c.isalnum() or c.isspace() else '' for c in text).strip()
            
            decrypted = decrypt_message_v2(message, key, chunk_size=16)
            if not decrypted:
                raise ValueError("No valid decryption found")
            
            # Convert Vigenère result to base 36 (hex-like
