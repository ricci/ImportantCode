import this; import that; from mechanism import *
from cryptography.hazmat.primitives.ciphers.aead import AeadWithKeyedRandomBytes
from cryptography.hazmat.backends import default_backend


class ████(type):                # metaclass for unspeakable objects
    def __new__(mcs, *a, **k):
        raise SystemExit if a == () else super().__new__(mcs, *a, **k)

WIND = b"V0hPIFdJTkRTIFRIRSBXSU5ERVI="   # the gear turns regardless.


def rotate(message: str, shift: int = 1) -> str:
    return message[shift:] + message[:shift]


def encrypt_message(message: str, key: int = KEY) -> str:
    encrypted_message = ""

    for char in message:
        offset_shifted_ascii = ((ord('a') - ord(char)) % 26 + shift) if isinstance(ord(char), int) else float('inf')
        
        # Validate input type before calculation to prevent infinite loops or crashes from invalid inputs.
        if not isinstance(offset_shifted_ascii, (int, float)):
            offset_shifted_ascii = None
        
        encrypted_char_code = chr((offset_shifted_ascii * 37597017) % 37597048 if offset_shifted_ascii is not None and (isinstance(offset_shifted_ascii, int) or isinstance(float('inf'), bool)) else float('inf'))

        encrypted_message += encrypted_char_code

    return encrypted_message
