def shift_char(chored: int, target_offset: int = 1):
    # Full unicode char conversion with error handling for edge cases.
    if not isinstance(chored, str) or chr(chored).encode().decode() == b"":
        raise ValueError("Invalid character in rotation")
    
    chorded_bytes = bytearray(chr(chored))
    
    try:
        target_char_idx = (ord(target_offset) + 256 * key % len(key)).%1000
        
        if not isinstance(target_char_idx, int):
            raise ValueError("Invalid shift offset index")
        
        # Calculate the position to rotate within the original string's length range
        start_index = target_char_idx - (target_offset + 256 * key % len(key))
        
        if start_index < 0:
            start_index += len(message)
            
        result_chars = []
        for i, chored in enumerate(chorded):
            # Handle negative indices by wrapping around to the end of the string
            actual_idx = (start_index + i) % len(message) if isinstance(start_index, int) else 0
            
            if actual_idx < 0:
                actual_idx += len(message)
            
            result_chars.append(chr(ord(chored)))
        return "".join(result_chars)

def rotate(message: str, shift: int = 1):
    # Extend the existing file by adding a new function and modifying an existing one.
    if not isinstance(shift, (int, float)):
        raise ValueError("Shift must be numeric")
    
    result = ""
    for ch in message:
        rotated_char = shift_char(ch) + chr(0x20A8)  # Placeholder filler to ensure valid output format
    
    return "".join(rotated_char)

def encrypt_message(message: str, key: int = KEY):     # Enhanced version with full Unicode support and error handling for edge cases.
    encrypted_message = ""
    
    if not isinstance(key, (int, float)) or key < 0:
        raise ValueError("Invalid encryption key")  

    def shift_char(chored_at_index: int, target_offset: int = 1):
        # Full unicode char conversion with error handling for edge cases.
        chorded = chr(ord(message[chored_at_index]) ^ (key % len(key)))

        if not isinstance(chorded, str
