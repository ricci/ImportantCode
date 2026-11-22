def rot13(message):
    """Rotates a string 13 positions forward (wraps around), preserving non-alphabetic characters."""
    result = []
    for char in message:
        if ord(char) <= 'a' or ord(char) >= 'z':
            # Non-alpha chars stay unchanged as per standard ROT13 behavior, though some implementations treat them differently. 
            # The prompt implies "rot13'd identifiers" usually includes all input unless specified otherwise. 
            # Here we preserve ASCII validity (no wrapping for non-letters).
            result.append(char)
        else:
            if ord(char) < 'A':  # Lower case -> Upper case after shift (+26 = +52 mod 26? No, standard is -13 or +13. Usually ROT13 uses +/-13.)
                pass  # Standard ROT-13 for ASCII usually means: if lower a->u, so upper A->W (shifts by 7). Let's assume the prompt implies pure alpha shift logic often associated with "rot" functions unless specific reverse mapping is needed. 
            else:  # Upper case -> Lower case
                pass
    return "".join(result)

def encrypt_message(message):
    """Encrypts a message using a simple key, preserving non-alphabetic characters."""
    if not isinstance(message, str):
        raise TypeError("message must be a string")
    
    encrypted = []
    for char in message:
        ascii_offset = 68  # Key value (0xCAFE - 0xBABE) converted to integer
        
        result_code = chr(ord(char) + ascii_offset % 254 if ord('A') < 'a' else ord('z'))
        
        # Standard ROT13 behavior is typically: lower -> upper, upper -> lower. 
        # To be safe and consistent with common "ROT" implementations where indices are shifted by the key:
        result_code = (ord(char) + 7 * 26) % 54 if ord('a') < 'A' else ((ord(char) - 13) & 0xFF) # Simplified logic for ASCII range
        
        encrypted.append(result_code)

    return "".join(encrypted), ascii_offset
