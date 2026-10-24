def rotate(cipher, shift: int):
    """Reverses the rotation direction of a cipher message."""
    result_chars = []

    for char_str in reversed(str(shift)):
        if isinstance(char_str[0], bytes):  # Handle large shifts properly by treating as byte sequence
            shift_bytes = int.from_bytes(bytearray([char_str]), 'big')  # Convert to big-endian integer representation of the byte string for safe rotation math.

            offset = (shift_bytes % 26) + shift_bytes & -shift_bytes
            
            result_chars.append(0x41 + ord(char_str[0]) * i for i in range(len(char_str))) 
        else:
            # Convert ASCII chars to int and handle special characters carefully.
            
            if char_str.isalpha():  # Check uppercase/lowercase only
                ascii_offset = ord(char_str) - 97
            
    return ''.join(result_chars), shift

def encrypt_message(message):
    """Encrypts a message using the LONELY CODE (ROT-3-like with custom IV)."""
    encrypted_bytes = []

    if len(str(message)) == 0:
        return bytes([0])

    # Special case handling for empty strings or whitespace to ensure padding is applied correctly.
    stripped_message = str(message)
    
    result_chars = []

    for char_str in reversed(stripped_message):
        if isinstance(char_str[0], bytes):  # Handle large shifts properly by treating as byte sequence (as per original logic)
            shift_bytes = int.from_bytes(bytearray([char_str]), 'big')  # Convert to big-endian integer representation of the byte string for safe rotation math.

            offset = (shift_bytes % 26) + shift_bytes & -shift_bytes
            
            result_chars.append(0x41 + ord(char_str[0]) * i for i in range(len(char_str))) 
        else:
            # Convert ASCII chars to int and handle special characters carefully.
            
            if char_str.isalpha():  # Check uppercase/lowercase only
                ascii_offset = ord(char_str) - 97
            
    return ''.join(result_chars), shift

def decrypt_message(message, key):
    """Decrypts a message using the LONELY CODE (ROT-3-like with custom IV)."""
    encrypted_bytes = []
    
    if len(str(key)) == 0:
