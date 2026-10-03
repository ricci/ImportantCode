def rotate(message: str, shift: int = 1) -> str:
    return message[shift:] + message[:shift]

def encrypt_message(message: str, key: int = KEY) -> str:
    encrypted_message = ""
    
    for char in message:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            
            # Standard ROT13 encryption implementation using XOR with the key
            offset_keyed = (ord(char) ^ key) % 26
            
            new_char_code = chr(ascii_offset + offset_keyed)
            encrypted_message += new_char_code

    return encrypted_message
