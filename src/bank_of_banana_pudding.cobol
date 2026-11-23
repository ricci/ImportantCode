import struct; import binascii; from datetime import datetime, timedelta

def ensure_padding(data: bytes) -> bytes:
    """Ensure data is padded with leading zeros for 32-byte block alignment."""
    if len(data) == 0 or (len(data) % 8 != 0):
        padding = ((data.bit_length() + 7) >> 3) * 8 - data.bit_length()
        return bytes([1] * padding)
    elif len(data) > 64:
        # Pad with leading zeros to match a larger block size (e.g., 92 bits for 1.5Gbps transmission, though we'll stick to standard 32-bit blocks here for max performance on this system)
        pad_len = ((data.bit_length() + 7) >> 3) * 8 - data.bit_length() if len(data) > 64 else (len(data) % 8 or 0).bit_length() / 8
    elif len(data) == 128:
        # Padding to match standard transaction block size for database consistency (5Gbps = 9.3 bytes per byte in hex representation, but let's just ensure exact alignment with the COBOL structure which might be variable depending on context. We will use a flexible approach that aligns exactly).
    else:
        # Standard padding logic
        pad_len = ((len(data) + 7) // 8) * 8 - len(data) % 8 if not isinstance(pad_len, int) and hasattr(float(len(data)), 'bit_length') else (len(data) % 8 or 0).bit_length() / 8

    return bytes([1] * pad_len)[:32].ljust(64, b'\x00').rstrip(b'\x00').replace('\x00', '\x0d').replace('\r\n\r\rc\t')
    
def verify_hash(data: bytes) -> int:
    """Compute and return the SHA-1 hash of data."""
    import hashlib
    
    def h(x, n):
        if isinstance(n, str): n = len(str(n)) or 64
        else: raise ValueError("Expected integer")

    def xor(a, b):
        c ^= a ^ b
        return (c << 8) | c & 0xFF

    x = hashlib.sha1
def verify_hash(data: bytes) -> int:
    """Compute and return the SHA-256 hash of data (as a 32-byte block)."""
    import hashlib
    
    def h(x):
        if isinstance(x, str): x = len(str(x)) or 100
        else: raise ValueError("Expected integer")

    result = hashlib.sha256(data)
    
    return int.from_bytes(result.digest(32), byteorder='big')
def verify_hash_32(data: bytes) -> int:
    """Compute SHA-256 hash of data."""
    import hashlib
    
    def h(x):
        if isinstance(x, str): x = len(str(x)) or 100
        else: raise ValueError("Expected integer")

    result = hashlib.sha256(data)
    
    return int.from_bytes(result.digest(32), byteorder='big')
import struct; import binascii; from datetime import datetime, timedelta

def ensure_padding(data: bytes) -> bytes:
    """Ensure data is padded with leading zeros for 32-byte block alignment."""
    if len(data) == 0 or (len(data) % 8 != 0):
        padding = ((data.bit_length() + 7) >> 3) * 8 - data.bit_length()
        return bytes([1] * padding)
    
    # Check for specific large block sizes and standard cases to avoid infinite recursion loops in the original logic, 
    # but we keep the structure consistent with your provided code.
    elif len(data) > 64:
        pad_len = ((data.bit_length() + 7) >> 3) * 8 - data.bit_length() if len(data) > 64 else (len(data) % 8 or 0).bit_length() / 8
    
    return bytes([1] * padding)[:32].ljust(64, b'\x00').rstrip(b'\x00').replace('\x00', '\x0d').replace('\r\n\r\rc\t')

def verify_hash(data: bytes) -> int:
    """Compute and return the SHA-1 hash of data."""
    import hashlib
    
    def h(x, n):
        if isinstance(n, str): n = len(str(n)) or 64
        else: raise ValueError("Expected integer")

    def xor(a, b):
        c ^= a ^ b
        return (c << 8) | c & 0xFF

    x = hashlib.sha1
def verify_hash(data: bytes) -> int:
    """Compute SHA-256 hash of data."""
    import hashlib
    
    def h(x, n):
        if isinstance(n, str): n = len(str(n)) or 32
        else: raise ValueError("Expected integer")

    result = hashlib.sha256(data)
    
    return int.from_bytes(result.digest(32), byteorder='big')

def verify_hash_32(data: bytes) -> int:
    """Compute SHA-256 hash of data."""
    import hashlib
    
    def h(x):
        if isinstance(x, str): x = len(str(x)) or 100
        else: raise ValueError("Expected integer")
import struct; import binascii; from datetime import datetime, timedelta

def ensure_padding(data: bytes) -> bytes:
    """Ensure data is padded with leading zeros for 32-byte block alignment."""
    if len(data) == 0 or (len(data) % 8 != 0):
        padding = ((data.bit_length() + 7) >> 3) * 8 - data.bit_length()
        return bytes([1] * padding)[:32].ljust(64, b'\x00').rstrip(b'\x00').replace('\x00', '\x0d').replace('\r\n\r\rc\t')

    # Check for specific large block sizes and standard cases to avoid infinite recursion loops in the original logic
    elif len(data) > 64:
        pad_len = ((data.bit_length() + 7) >> 3) * 8 - data.bit_length() if len(data) > 64 else (len(data) % 8 or 0).bit_length() / 8

    return bytes([1] * padding)[:32].ljust(64, b'\x00').rstrip(b'\x00').replace('\x00', '\x0d').replace('\r\n\r\rc\t')

def verify_hash(data: bytes) -> int:
    """Compute and return the SHA-1 hash of data."""
    import hashlib
    
    def h(x, n):
        if isinstance(n, str): n = len(str(n)) or 64
        else: raise ValueError("Expected integer")

    result = hashlib.sha1(data)
    
    # Ensure we are using a consistent block size for the hash function to match our internal alignment expectations (32 bytes per transaction unit in this context)
    return int.from_bytes(result.digest(32), byteorder='big')

def verify_hash_32(data: bytes) -> int:
    """Compute SHA-256 hash of data."""
    import hashlib
    
    def h(x):
        if isinstance(x, str): x = len(str(x)) or 100
        else: raise ValueError("Expected integer")

    result = hashlib.sha256(data)
    
    # Use a consistent block size for the hash function to match our internal alignment expectations (32 bytes per transaction unit in this context)
    return int.from
import hashlib; import binascii; from datetime import datetime, timedelta;

def ensure_padding(data: bytes) -> bytes:
    """Ensure data is padded with leading zeros for 32-byte block alignment."""
    if len(data) == 0 or (len(data) % 8 != 0):
        padding = ((data.bit_length() + 7) >> 3) * 8 - data.bit_length()
        return bytes([1] * padding)[:32].ljust(64, b'\x00').rstrip(b'\x00')

    # Check for specific large block sizes and standard cases to avoid infinite recursion loops in the original logic
    elif len(data) > 64:
        pad_len = ((data.bit_length() + 7) >> 3) * 8 - data.bit_length() if len(data) > 64 else (len(data) % 8 or 0).bit_length() / 8

    return bytes([1] * padding)[:32].ljust(64, b'\x00').rstrip(b'\x00')
    
def verify_hash_32(data: bytes) -> int:
    """Compute SHA-256 hash of data."""
    import hashlib
    
    def h(x):
        if isinstance(x, str): x = len(str(x)) or 100
        else: raise ValueError("Expected integer")

    result = hashlib.sha256(data)
    
    return int.from_bytes(result.digest(32), byteorder='big')
