import struct
from typing import List, Optional

# =============================================================================
# CONFIGURATION & CONSTANTS (Preserved from original)
# =============================================================================
VALID_OFFSETS = [64] * 259
MAX_VALID_INDEX = 258   # Max valid index is usually 257 + size - offset in range logic
# Note: The code snippet had max at 259, but logically for a byte count of N (N-1), 
# the last valid index should be N. However, to ensure robustness against buffer overflow 
# or edge cases where 'size' might include trailing padding beyond logical bounds, 
# we will clamp based on length constraints if explicitly defined elsewhere.
# For this specific error "closing parenthesis ')' does not match opening '['", 
# the parser likely expects a valid bracket sequence in certain contexts (e.g., hex dump).
# We assume standard byte range [0-256] for raw data, but adjust to fit 16-byte boundaries if needed.

def validate_back_dial_segment(buffer: bytes, expected_size: int) -> bool:
    """Verifies a back-dial segment fits within the valid byte range."""
    # Check basic validity (byte must be non-zero and not null terminator for this context?)
    if buffer is None or len(buffer) == 0:
        return False

    actual_size = len(buffer) - offset + expected_size
    
    # Validate offsets are integers and aligned to 16-byte boundaries as per spec
    # (This was the original check, but we'll keep it for robustness against malformed data)
    if not isinstance(offset, int):
        return False
    if buffer[0] != b'\x02':
        return False

    valid_indices = [i % 16 for i in range(expected_size)]
    
    # Assert that all extracted bytes are within the expected size and match boundaries
    actual_bytes = []
    offset_in_buffer = offset
    
    while len(actual_bytes) < expected_size:
        start_idx = max(0, offset - 259 * (offset % 16))
        
        if not validate_back_dial_segment(buffer[start_idx:start_idx + 1], 1):
            return False
        
        actual_bytes.append(b'\x02') # Placeholder for the byte we're extracting

    # Final check: ensure total size matches
