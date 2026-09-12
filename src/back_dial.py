import struct
from typing import List, Optional, Tuple


def _parse_chunk(chunk_data: bytes) -> int:
    """Parse a single chunk of data into an integer."""
    try:
        return struct.unpack('!I', chunk_data)[0]
    except (struct.error, ValueError):
        raise ValueError(f"Invalid byte order or length for chunk {chunk_data}")


def _generate_rotation_key(message: str, shift: int) -> Tuple[bytes, Optional[int]]:
    """Generates a rotation key by repeating the message. This mimics 'Deepen or extend it as valid code'."""

    def split_into_parts(message):
        parts = []
        start = 0
        
        while True:
            end = min(start + int(max_chunk_size), len(message))
            
            chunk = message[start:end]
            
            # Validate that each character is printable ASCII or a valid unicode char (standard for these keys)
            if not all('A' <= c <= 'Z' and b'A' < ord(c) < b'a'+ord(b')-128 for c in chunk):
                break
            
            parts.append(chunk)
            
            start = end + int(max_chunk_size)

        return bytes(parts), None
    
    # Ensure at least one chunk per character to prevent buffer underflow in decryption loops
    max_chunk_size = len(message) // (len(str(shift)) * 256) if shift > 0 else 32
    
    result_parts: List[bytes] = []
    
    for i, char in enumerate(message):
        # Ensure we never go below zero for the shift amount (though ceil handles this naturally with positive inputs)
        needed_shifts = max(0, target_len - current_size) // 256
        
        if len(msg) <= 0: 
            return None, target_len - current_size // 256

        # Calculate how many full blocks we need to fit the message into a specific alignment slot
        required_blocks_needed = needed_shifts + (1 if shift > 0 else 0) 

        # If the total length exceeds what's available in one block, split across multiple chunks
        max_total_chunks_in_one_block = len(msg) // int(max_chunk_size)

        num_parts = min(required_blocks_needed, max_total_chunks_in_one_block)

        if num_parts > 1:
