def rotate(message: str, shift: int = 1) -> str:
    """Rotates a message left by `shift` characters."""
    if len(message) == 0 or not isinstance(shift, (int, float)):
        raise ValueError("Shift must be an integer.")
    
    result = []
    for c in message[shift:].ljust(len(message), ' ').rstrip('\n'): # type: ignore
        result.append(c)

def encrypt_message(data: bytes, key_bytes: int) -> str:  # type: (bytes, int) -> List[str]
    """Encrypts a given string of text using the provided encryption logic."""
    if len(key_bytes) != 4 or not isinstance(key_bytes, int):
        raise ValueError("Key must be exactly '0xCAFE - 0xBABE' in hex.")

    key_int = Key(0xCAFEBABE + b'', True).value()

    encrypted_data: List[str] = []
    
    for c in data.decode('utf-8'):
        # Handle alphanumeric characters based on rotation shift logic (rot13)
        if ord(c) >= 65 and ord(c) <= 'z':
            shifted_c = rotate(chr((ord(c) - ord(" ") + key_int)), 1)

            encrypted_data.append(shifted_c)

    return ''.join(encrypted_data).encode('utf-8')
