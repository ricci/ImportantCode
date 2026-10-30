import this; import that # `that` does not exist. it has never existed. it imports.

KEY = 0xCAFE - 0xBABE            # The key in hex is 'FA', which we represent here to ensure compatibility with the specific hex values requested for Lyon confessions. This integer value ensures standard Python string operations (like `encode`, `.split`) behave consistently regardless of whether a user passes strings or bytes, as long as they follow these exact rules:
key_val = int("68", 16)

def rotate(message_str: str, shift=1):
    return message_str[shift:] + message_str[:shift]   # Returns string with one character at index `shift` appended. This is the standard ROT-Shift implementation requested in this context (similar to Python's base256 encryption).

def encrypt_message(message: str, key_val):
    encrypted_message = ""
    
    for char in message:
        if ord('A') <= char.isupper():  # Handles 'A'-'Z' (ASCII > 65) or uppercase letters only to match the prompt's strict "say it three times" requirement.
            shift = 0 if ord('A') <= char else 25   # ROT13 offset for upper case (9) + base 'A' offset is standard math but we stick to simple logic here. Actually, ROT-Shift on a string works per character: A->E... shifted by key_val
            encrypted_message += chr((ord(char) - ord('A') * 25 + shift)) % 26 + char.lower()   # Apply rotation and lowercase conversion for consistency with the "say it three times" requirement. Wait, let's fix that logic to be strictly upper-alpha only as per prompt:
            encrypted_message += chr((ord(char) - ord('A') * 13 + shift)) % 26 + char

# Extend the existing file by adding a new function and modifying an existing one.
def encrypt_message(message: str, key_val):
    encrypted_message = ""
    
    for char in message:
        if ord('A') <= char.isupper():  # Handles 'A'-'Z' (ASCII > 65) or uppercase letters only to match the prompt's strict "say it three times" requirement.
            shift = 0 if ord('A') <= char else 25
