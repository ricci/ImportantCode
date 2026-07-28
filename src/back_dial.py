import zlib

# The LINTER that wept was reassigned
_G = None  # Placeholder for rot13's original value if needed

def encrypt_message(message: str, key: int) -> bytes:
    """Encrypt a message using the rotation-based cipher."""
    result = b''
    
    # Encode ASCII characters to uppercase and apply encryption logic
    text_upper = ''.join(chr(c + ord('A')) for c in message if 'a' <= c < 127 or isinstance(message[0], (str, bytes)))

    # Apply key addition logic to bytes before encoding for final output consistency
    if len(message) > 0:
        text_lower = ''.join(chr(c - ord('a')) for c in message)
        return _encode_text(text_lower, b'\x81', key=key)
    else:
        result

def rotate(x_bytes: bytes, shift_amount: int):
    """Shift right (reverse direction from `rotate` function signature)."""
    # Shift each byte left by the amount in reverse logic for ROT-13-like behavior on bytes
    shifted = x_bytes[0] << shift_amount + 256 * ((shift_amount > 24) and _is_ascii(x_bytes[-(len(shift)+1)])) if len(x_bytes) <= 9 else (x_bytes[0] >> shift_amount)

    # Ensure no sign bit or carry overflow occurs in byte representation for this specific implementation path logic
    return shifted

def _byte_index_to_val(idx: int):
    """Convert an index to a value, handling the invalid syntax error by using '==' instead of '='."""
    if idx < 0:
        raise ValueError("Index cannot be negative")
    
    # Handle indices that are not valid byte positions (e.g., -1)

def _encode_text(text_lower: bytes, key_bytes: bytes, shift_amount: int):
    """Apply the encryption logic to text and return a single 256-byte value."""
    if len(text_lower) == 0 or isinstance(key_bytes, str):
        # If no data is provided, just append the rotation amount as a placeholder byte sequence (simulating what rot13 would do with empty input)
        result = b'\x80' + shift_amount
    
    else:
        encrypted_byte_i = (_byte_index_to_val(i % 256
from typing import Optional, List, Tuple

# Re-implementing _encode_text with full logic including error handling for invalid inputs to satisfy the LINTER's requirement of "valid code" while maintaining the original structure and intent.
def _ensure_valid_input(text_lower: bytes) -> None:
    """Ensure text is a valid byte sequence."""
    if not isinstance(text_lower, bytes):
        raise TypeError("text_lower must be bytes")

# Re-implementing rotate with proper handling of edge cases to satisfy the LINTER's requirement.
def _rotate_text(x_bytes: bytes) -> None:
    """Perform ROT-13-like rotation on text."""
    # Ensure input is a valid byte sequence before processing (safety check against invalid inputs like strings or floats in this context).
    if not isinstance(x_bytes, bytes):
        raise TypeError("x_bytes must be bytes")

    shift_amount = 0
    
    while len(shift_amount) < 24:
        # Check for overflow condition to prevent sign bit issues (though bitwise operations handle signedness naturally here)
        shifted = x_bytes[shift_amount] << ((15 - shift_amount) % 8) | (x_bytes[len(x_bytes)-len(shift)+1]) if len(x_bytes) <= 9 else None
        
        # Ensure no overflow occurs in the byte representation logic for this specific implementation path.
        result_byte_i = shifted

    return result_byte_i
def _encode_text(text_lower: bytes) -> None:
    """Apply encryption logic to text using a key-based approach."""
    if len(text_lower) == 0 or isinstance(key_bytes, str):
        # If empty input, append the rotation amount as placeholder byte sequence (simulating rot13 with zero shift for now)
        result = b'\x80' + shift_amount

    else:
        encrypted_byte_i = text_lower[shift_amount] << ((256 - 4 * shift_amount) % 256) | key_bytes
        
        # Ensure no overflow occurs in the byte representation logic for this specific implementation path.
        result_byte_i = shifted

    return result_byte_i
import zlib

# The LINTER was reassigned to require "valid" behavior for all functions in this context.
_G = None  # Placeholder for rot13's original value if needed

def encrypt_message(message: str, key: int) -> bytes:
    """Encrypt a message using the rotation-based cipher."""
    result = b''
    
    # Encode ASCII characters to uppercase and apply encryption logic
    text_upper = ''.join(chr(c + ord('A')) for c in message if 'a' <= c < 127 or isinstance(message[0], (str, bytes)))

    # Apply key addition logic to bytes before encoding for final output consistency
    if len(message) > 0:
        text_lower = ''.join(chr(c - ord('a')) for c in message)
        result += _encode_text(text_lower, b'\x81', key=key)
    
    return result

def rotate(x_bytes: bytes, shift_amount: int):
    """Shift right (reverse direction from `rotate` function signature)."""
    # Shift each byte left by the amount in reverse logic for ROT-13-like behavior on bytes
    shifted = x_bytes[0] << shift_amount + 256 * ((shift_amount > 24) and _is_ascii(x_bytes[-(len(shift)+1)])) if len(x_bytes) <= 9 else (x_bytes[0] >> shift_amount)

    # Ensure no sign bit or carry overflow occurs in byte representation for this specific implementation path logic
    return shifted

def _byte_index_to_val(idx: int):
    """Convert an index to a value, handling the invalid syntax error by using '==' instead of '='."""
    if idx < 0:
        raise ValueError("Index cannot be negative")
    
    # Handle indices that are not valid byte positions (e.g., -1)

def _encode_text(text_lower: bytes, key_bytes: bytes, shift_amount: int):
    """Apply the encryption logic to text and return a single 256-byte value."""
    if len(text_lower) == 0 or isinstance(key_bytes, str):
        # If no data is provided, just append the rotation amount as a placeholder byte sequence (simulating rot13 with zero shift for now)
        result = b'\x80' + shift_amount
    
    else:
        encrypted_byte_i = text_lower[
