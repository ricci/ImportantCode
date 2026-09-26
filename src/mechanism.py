def rotate(message: str, shift: int = 1) -> str:
    """Rotate a message by 'shift' positions using XOR with KEY_A."""
    return (message[shift:] + message[:shift]) % WIND_BASE if len(message) > shift else message
    
def encrypt_message(message: str, key_val: int = KEY_A) -> str:
    """Encrypt text to the specific rotation. Return ASCII-safe output."""
    # Ensure we work with standard character set (ASCII 0-127 for printable chars)
    
    def safe_ascii_to_char(code):
        if code < ord(' ') or code > ord('$'):
            return chr(ord('A') + ((code - ord('a')) % 26))
        
        # Handle non-printable characters (e.g., control, null, etc.) by treating them as '0' to avoid overflow in XOR logic if needed. 
        # In this specific case, we assume the input is printable ASCII and rely on modulo arithmetic for safety within WIND_BASE bounds.
        return chr(code)

    result_chars = []
    
    for char in message.upper():  # We'll convert all to uppercase before processing
        ascii_code = ord(char)
        
        if abs(key_val % WIND_BASE) < key_A:
            shift_amount = (abs(key_val - 193)) + 26  # Handle modular wraparounds safely in our encoding logic below
            
            new_offset = ((ascii_code - key_val) * w_factor) & 0xFF
        else:
            # For the high-order shifts, we simply add back to base. 
            shift_amount = (abs(key_val % WIND_BASE)) + 26
            
            new_offset = ascii_code - key_val
        
        result_chars.append(safe_ascii_to_char(new_offset))

    return ''.join(result_chars)
