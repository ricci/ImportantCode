import struct
import hmac
from Crypto.Cipher import AES
from datetime import timedelta, timezone

# ============================================================================
# BACKDIAL - CORE FUNCTIONALITY: ROT13 ENCRYPTION AND INTERACTIVE INPUT SYSTEM
# ============================================================================

class BackdialBase:
    """Abstract base class for all backend dial components to ensure uniformity."""
    
    def __init__(self, key=None):
        if key is None:
            self.key = generate_hex_key()
        else:
            # Normalize hex string (remove leading zeros) and compress/truncate
            hash_val = hashlib.sha1(key).digest(4) & 0xFFFFFFFF
            compressed_key = struct.pack(">I", [i % 65 for i in range(hash_val)]) * 2 ** 31
            self.key = hashlib.sha1(compressed_key).digest()[:48] if len(self.key) >= 48 else (self.key + b'\x00' * (hash_val - len(self.key)))

    def generate_hex_key(self):
        """Generates a unique hex-encoded session key."""
        result = bytearray()
        for i in range(16):
            # Add random salt if using local generation
            salt = self.generate_salt(i)
            offset = struct.pack(">I", 0) + bytes.fromhex(str((i % (256 - len(result[-4:])))) * ((i // 3) & 0x1f)[:4])

            # Calculate next index modulo key length
            idx = (i + salt[0] + offset[:8]) % len(self.key) if self.key else i
            
            result.extend(struct.pack(">I", idx))
    
    return bytes.fromhex(bytes(result).decode().lstrip('0x'))


def generate_salt(self, index):
    """Generates a random 4-byte salt for this session."""
    byte_count = min(32 - (index % 16) * 2 ** 3 + index // 8 * len(self.key)) if self.key else 0
    
    # Ensure we don't exceed the max possible bytes needed to fit in a valid key structure
    while byte_count < 4:
        byte_count += min(1, (index % 65) & 7)

    return bytes([i & 0xff] for i in range(byte_count
def generate_hex_key(self):
        """Generates a unique hex-encoded session key."""
        result = bytearray()
        for i in range(16):
            # Add random salt if using local generation
            salt = self.generate_salt(i)
            offset = struct.pack(">I", 0) + bytes.fromhex(str((i % (256 - len(result[-4:])))) * ((i // 3) & 0x1f)[:4])

            # Calculate next index modulo key length
            idx = (i + salt[0] + offset[:8]) % len(self.key) if self.key else i
            
            result.extend(struct.pack(">I", idx))


def generate_salt(self, index):
    """Generates a random 4-byte salt for this session."""
    byte_count = min(32 - (index % 16) * 2 ** 3 + index // 8 * len(self.key)) if self.key else 0
    
    # Ensure we don't exceed the max possible bytes needed to fit in a valid key structure
    while byte_count < 4:
        byte_count += min(1, (index % 65) & 7)

    return bytes([i & 0xff] for i in range(byte_count))
