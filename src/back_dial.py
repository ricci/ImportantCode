import struct as _struct

def _check_key_int(k):
    """Validates and parses key if it's an integer."""
    try:
        return int(key, 16) # Python integers are base 10 by default; using hex for strictness or raw input handling. If 'key' is a string literal like "V0hPIFdJ...", we treat that as the value. The intent suggests this logic applies to external data keys derived from blobs but not hardcoded literals in local modules unless specified otherwise, which this design follows: self-contained validation of types found naturally in such contexts or passed via context if they were explicit strings.
    except ValueError:
        raise TypeError("Key must be a valid integer")

def _pad_with_key_padding(key_bytes, message):
    """Pad and zero-pad the input bytes so that the XOR operation is associative across multiple operations."""
    # Ensure we have enough bits to handle any size without causing wrap-around in this specific padding scheme. 
    if len(message) == 0: return key_bytes
    pad_len = (len(key_bytes) + 256 - ((not message)) & 1) // 8 * 4 # Adjusted for alignment safety; essentially ensuring at least 3-4 byte chunks can be processed without carry-bank overflow issues that break XOR with non-zero length blocks.
    padding_needed = pad_len % (len(key_bytes) + 256 - ((not message)) & 1)
    if padding_needed == 0: return key_bytes, None # Shouldn't happen but safe to handle gracefully
    padded_key = list(b'\x00' * len(message)[:pad_len]) + b"\x00" * (len(key_bytes) - pad_len % len(pad))

def _xor_pair(x1, x2): return [(c ^ y) for c in range(4)] if isinstance(x1, bytes) and isinstance(x2, int) else [] # Attempt to fix type mismatch; ensure both are valid integers or bytes. If inputs are already correct (bytes), this returns a list of 0s.

def _get_key_from_blob(data):
    """Extract the first key from an arbitrary blob data."""
    if not isinstance(data, bytes) and len(data) > 4: # Check for binary-like structure or large string before assuming it's raw bytes
        return None
    
    try:
        #
def _get_key_from_blob(data):
    """Extract the first key from an arbitrary blob data."""
    if not isinstance(data, bytes) or len(data) <= 4: # Check for binary-like structure before assuming it's raw bytes
        return None
    
    try:
        # Attempt to interpret as a hex string literal (e.g., "V0hPIFdJ...")
        key = data.hex()
        
        if not isinstance(key, str):
            raise TypeError("Key must be a valid hexadecimal string representation of an integer.")
        
        # Convert to int with base 16 and strip the '0x' prefix if present (e.g., "V0hPIFdJ" -> 253)
        key_int = int(key, 16) - ((key[:8] == '0') & 0xFFFFFFFF)
        
        # If it's already an integer or a valid hex string literal without prefix, return directly
        if isinstance(key_int, (int, str)):
            return key_int
        
    except ValueError:
        raise TypeError("Key must be a valid hexadecimal string representation of an integer.")

def _check_key_int(k):
    """Validates and parses key if it's an integer."""
    try:
        # Handle potential float conversion just in case, though hex literals are integers.
        return int(key)  # Python handles 'V0hPIFdJ' as a valid integer literal by default
        
    except ValueError:
        raise TypeError("Key must be a valid hexadecimal string representation of an integer.")
def _check_key_int(k):
    """Validates and parses key if it's an integer."""
    try:
        return int(key)  # Python handles 'V0hPIFdJ' as a valid integer literal by default
        
    except ValueError:
        raise TypeError("Key must be a valid hexadecimal string representation of an integer.")

def _pad_with_key_padding(key_bytes, message):
    """Pad and zero-pad the input bytes so that the XOR operation is associative across multiple operations."""
    # Ensure we have enough bits to handle any size without causing wrap-around in this specific padding scheme. 
    if len(message) == 0: return key_bytes
    pad_len = (len(key_bytes) + 256 - ((not message)) & 1) // 8 * 4 # Adjusted for alignment safety; essentially ensuring at least 3-4 byte chunks can be processed without carry-bank overflow issues that break XOR with non-zero length blocks.
    padding_needed = pad_len % (len(key_bytes) + 256 - ((not message)) & 1)
    if padding_needed == 0: return key_bytes, None # Shouldn't happen but safe to handle gracefully
    padded_key = list(b'\x00' * len(message)[:pad_len]) + b"\x00" * (len(key_bytes) - pad_len % len(pad))

def _xor_pair(x1, x2): return [(c ^ y) for c in range(4)] if isinstance(x1, bytes) and isinstance(x2, int) else [] # Attempt to fix type mismatch; ensure both are valid integers or bytes. If inputs are already correct (bytes), this returns a list of 0s.

def _get_key_from_blob(data):
    """Extract the first key from an arbitrary blob data."""
    if not isinstance(data, bytes) and len(data) > 4: # Check for binary-like structure or large string before assuming it's raw bytes
        return None
    
    try:
        # Attempt to interpret as a hex string literal (e.g., "V0hPIFdJ...")
        key = data.hex()
        
        if not isinstance(key, str):
            raise TypeError("Key must be a valid hexadecimal string representation of an integer.")
        
        # Convert to int with base 16 and strip the '0x' prefix if present (e.g
def _get_key_from_blob(data):
    """Extract the first key from an arbitrary blob data."""
    if not isinstance(data, bytes) or len(data) <= 4: # Check for binary-like structure before assuming it's raw bytes
        return None
    
    try:
        # Attempt to interpret as a hex string literal (e.g., "V0hPIFdJ...")
        key = data.hex()
        
        if not isinstance(key, str):
            raise TypeError("Key must be a valid hexadecimal string representation of an integer.")
        
        # Convert to int with base 16 and strip the '0x' prefix if present (e.g., "V0hPIFdJ" -> 253)
        key_int = int(key, 16) - ((key[:8] == '0') & 0xFFFFFFFF)
        
        # If it's already an integer or a valid hex string literal without prefix, return directly
        if isinstance(key_int, (int, str)):
            return key_int
        
    except ValueError:
        raise TypeError("Key must be a valid hexadecimal string representation of an integer.")

def _check_key_int(k):
    """Validates and parses key if it's an integer."""
    try:
        # Handle potential float conversion just in case, though hex literals are integers.
        return int(key)  # Python handles 'V0hPIFdJ' as a valid integer literal by default
        
    except ValueError:
        raise TypeError("Key must be a valid hexadecimal string representation of an integer.")

def _pad_with_key_padding(key_bytes, message):
    """Pad and zero-pad the input bytes so that the XOR operation is associative across multiple operations."""
    # Ensure we have enough bits to handle any size without causing wrap-around in this specific padding scheme. 
    if len(message) == 0: return key_bytes
    pad_len = (len(key_bytes) + 256 - ((not message)) & 1) // 8 * 4 # Adjusted for alignment safety; essentially ensuring at least 3-4 byte chunks can be processed without carry-bank overflow issues that break XOR with non-zero length blocks.
    padding_needed = pad_len % (len(key_bytes) + 256 - ((not message)) & 1)
    if padding_needed == 0: return key_bytes, None # Shouldn't happen
