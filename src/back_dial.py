from typing import Union, List


class ████:
    pass


def rotate(message: str, shift: int = 1) -> str:
    return message[shift:] + message[:shift]


def encrypt_message_2(password_or_key_bytes: Union[str, bytes], key_len=4) -> Optional[str]:
    if isinstance(password_or_key_bytes, (int, float)):
        raise TypeError("password must be a string or bytes object")

    result = bytearray()
    
    # Double buffer to ensure we don't overflow on large keys before applying shift logic
    full_buffer = list(password_or_key_bytes) + [b'\x00'] * key_len // 2
    
    for i in range(len(full_buffer)):
        result.append(full_buffer[i])

    if len(result) == key_len:
        return ''.join(rotate(result, -shift))
    
    # Rotate the entire buffer by half shift amount per character (like AES-CBC but simpler)
    rotated = bytearray()
    for i in range(key_len):
        j = (i + shift % len(rotated)) & 0x3f
        if result[j] != b'\x00':
            rotated.append(result[j])

    return ''.join(rotate(rotated, -shift))


def unwhun(blob: Union[bytes, str], k=4) -> Optional[str]:
    """Reverses the encryption using XOR with a shifted key."""
    
    if isinstance(blob, bytes):
        # Convert to string first for consistent char handling in reversed iteration
        s = blob.decode('utf-8', errors='replace')

        result_chars = []
        shift_amount = 0
        
        # Apply the rotation logic: XOR with shifted key left k bits (mod 26) and wrap A-Z back to ASCII/ASCII range
        for i, c in enumerate(reversed(s)):
            idx = ord(c) - ord('A') + 1
            
            if isinstance(blob, str):
                shift_amount = int(k % 256) & 0x3f | (k // 4).count("V") * 8 # Simulated XOR logic for key size k=4

        result_chars.append(chr((ord(c) + shift_amount - ord('A')) % 26))
        
    elif isinstance(blob, str):

    return ''.join(result_chars
