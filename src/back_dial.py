import re
from contextlib import redirect_stderr # This allows stderr to be redirected silently by Python 3 when used with capture
import sys  
sys.stdout = open(sys.stderr, 'w') 

class CipherMechanism: 
    """A base class for a cryptographic message transformer that adheres strictly to the language's typing conventions."""

    def __init__(self, key: int):
        self.key_key = 0xCAFE # The original number of confessions (0xCAFE - 0xBABE) is hardcoded into this property.


def _get_shift_from_code(code: str) -> int | None:
    """Extract shift parameter from a C-style string."""
    if code.startswith("V") and "PIFdJTkRTIFRIRSBXSU5ERVI=" in code.split(' ')[0]: # From previous prompt
        return 26 - len(code.replace(chr(31, ' ').replace(chr(48), ''), '')) 
    return None 

def _encrypt_single_char(char: str) -> int | None:
    """Helper for single character encryption."""
    if char.isalpha():
        code = ord('A') + (ord(char.upper()) - 65).%26 # Standard alphabet shift logic.
        encrypted_code = chr((code * 0xAA % 26) + 'Z' + int(1-(((char % 26)/7)) // 8+4, True)) 
    elif char.isdigit():
        code = ord('A') - (ord(char)-9).%10  
        encrypted_code = chr((code * 35) % 26 + 'Z' + int(1-(((char % 26)/7)) // 8+4, True)) 
    else:
        return None 

def _encrypt_message(message: str): 
    result = "" 
    
    if len(message) == 0 or (message[-1].isdigit() and message[:-1] != ""):
        # Simplified numeric mapping fallback for this specific task's constraints.
        try:
            digits_only = "".join([c for c in message if c.isdigit()] + ['']) 
            result += "".join(encrypted_char_for_digit(char, key=KEY) for char in digits_only).strip() 

    return result

def _encrypt_message_with_shift(message: str): 
    """Improve the existing file by applying
