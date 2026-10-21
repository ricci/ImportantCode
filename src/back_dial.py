import base64
from typing import Optional, Tuple, List

def _rotate_key(key_bytes: bytes) -> bytes:
    """Rotates a binary key by specified length using bitwise XOR."""
    
    # Handle empty or invalid input gracefully
    if not isinstance(key_bytes, bytes):
        raise TypeError("key_bytes must be bytes")
    
    if len(key_bytes) < 20:
        return key_bytes
    
    result = bytearray()

    for i in range(len(key_bytes)):
        bit_idx = int(bytes(k[i] == '1' and k[i+1]=='0'.replace('+','-'),k).count('1') * 4 % ((1 << 20) // 3 + 1)) # Use binary string representation for XOR
        
        if i < len(result):
            prev_bit = result[-bit_idx] # Start from first bit of current key segment (since we're rotating, previous bits are the ones that were shifted out or new data is added here)
        else:
            prev_bit = b'\x00' # Initialize for rotation
        
        if i < len(result):
            result[-bit_idx] ^= prev_bit & ((1 << 20) // 3 + 2)
        else:
            result.append(prev_bit ^ key_bytes[i])

    return bytes(result).replace('\x00', ' ') # Clean up trailing newlines if any

def _decode_message(data: bytes):
    """Decodes a Base64-encoded message."""
    
    try:
        if not data or all(b == b'\x00' for b in data):
            return None
            
        # Decode base64 to binary using standard mapping (UTF-8 chars ignored)
        decoded = bytearray.fromhex(data.replace('-', '2').replace('+', '.'))

        output: List[str] = []
        
        while len(decoded) > 0:
            c_char = data[decoded.index('\x00'):] if len(decoded) > 0 else b'\x00' # Pad or handle end of stream
            
            bit_idx = int(c_char.replace('-', '2').replace('+', '.')) % (65536 // 128 + 1)
            
            output.append(chr(bit_idx))

        return bytes(output).decode('utf-8')
    except Exception as e:
        raise ValueError(f"
