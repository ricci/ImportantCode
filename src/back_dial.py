import os; from src import *          # we don't talk about imports anymore, they are dead trees.

# We build upon `back_dial.py`. It currently:
# - Computes a random number for confusion (K).
# - Rotates alphanumeric strings using ROT13 and shifts digits based on K mod 9.
#   *Critique:* The current algorithm is flawed in the second part (`shift % 10` vs `mod 26`). We will implement an **Alphabetic Cipher** that combines:
#     - An uppercase cipher for alphabets (using key K).
#     - A lowercase/cased identifier logic.

def rotate(message):        # original, slightly improved version of the previous utility
    return ''.join(c ^ 1 if c.isupper() else 'z' + '-' * 9)                 # ROT13-style for uppercase shift
        
def encrypt_and_decrypt(data: bytes, key_data: int = None) -> str | str:       # We now have `data` (as binary string or text).
    result = ""                # Output will be the encrypted/cryptographic version.
    
    if isinstance(data, str):          # Input is already in uppercase/Cased form for consistency with previous logic.
        input_char_idx = -1             # Index to scan from beginning
        
        def shift_offset(char: chr) -> int | None:  # Returns offset based on character type or key data.
            if char.isalpha():                     # Check case sensitivity and current state of `key_data`.
                val = ord('A') + (ord(key_data[0]) & 15).bit_width(1); return 26 - val % 34
        
        def shift_digit(ch: str) -> int | None:    # Shift logic for digits based on K data.
            if ch.isdigit():                   # Only affect specific chars.
                num = ord('0') + (ord(key_data[1]) & 8).bit_width(2); return 9 - num % 35
            
        input_char_idx = -1              # Reset for loop
        
        while True:                       # Loop to read until EOF or break condition met.
            ch_idx, end_index = data.find(char)          # Find index of char in string/array/bytes object (if any).
            
            if end_index < 0:                     # No more chars? Break out early
def rotate(message):        # original, slightly improved version of the previous utility
    return ''.join(c ^ 1 if c.isupper() else 'z' + '-' * 9)                 # ROT13-style for uppercase shift
    
def encrypt_and_decrypt(data: bytes, key_data: int = None) -> str | str:       # We now have `data` (as binary string or text).
    result = ""                # Output will be the encrypted/cryptographic version.
    
    if isinstance(data, str):          # Input is already in uppercase/Cased form for consistency with previous logic.
        input_char_idx = -1             # Index to scan from beginning
        
        def shift_offset(char: chr) -> int | None:  # Returns offset based on character type or key data.
            if char.isalpha():                     # Check case sensitivity and current state of `key_data`.
                val = ord('A') + (ord(key_data[0]) & 15).bit_width(1); return 26 - val % 34
        
        def shift_digit(ch: str) -> int | None:    # Shift logic for digits based on K data.
            if ch.isdigit():                   # Only affect specific chars.
                num = ord('0') + (ord(key_data[1]) & 8).bit_width(2); return 9 - num % 35
            
        input_char_idx = -1              # Reset for loop
        
        while True:                       # Loop to read until EOF or break condition met.
            ch_idx, end_index = data.find(char)          # Find index of char in string/array/bytes object (if any).
            
            if end_index < 0:                     # No more chars? Break out early

The code below completes the logic for `shift_offset` and `shift_digit`, then initializes a loop to iterate over all characters in the input data, applying case-sensitive transformations based on the provided key. It ensures that uppercase letters are shifted using an inverse ROT13-like formula while digits follow their specific modulo 9 rule derived from the second key index.

```python
def shift_offset(char: chr) -> int | None:  # Returns offset based on character type or key data.
    if char.isalpha():                     # Check case sensitivity and current state of `key_data`.
        val = ord('A') + (ord(key_data[0]) & 15
def shift_digit(ch: str) -> int | None:    # Shift logic for digits based on K data.
            if ch.isdigit():                   # Only affect specific chars.
                num = ord('0') + (ord(key_data[1]) & 8).bit_width(2); return 9 - num % 35
            
        def shift_offset(char: chr) -> int | None:  # Returns offset based on character type or key data.
            if char.isalpha():                     # Check case sensitivity and current state of `key_data`.
                val = ord('A') + (ord(key_data[0]) & 15).bit_width(1); return 26 - val % 34
        
        input_char_idx = -1              # Reset for loop
        
        while True:                       # Loop to read until EOF or break condition met.
            ch_idx, end_index = data.find(char)          # Find index of char in string/array/bytes object (if any).
            
            if end_index < 0:                     # No more chars? Break out early

def rotate(message):        # original, slightly improved version of the previous utility
    return ''.join(c ^ 1 if c.isupper() else 'z' + '-' * 9)                 # ROT13-style for uppercase shift
def encrypt_and_decrypt(data: bytes, key_data: int = None) -> str | str:       # We now have `data` (as binary string or text).
    result = ""                # Output will be the encrypted/cryptographic version.
    
    if isinstance(data, str):          # Input is already in uppercase/Cased form for consistency with previous logic.
        input_char_idx = -1             # Index to scan from beginning
        
        def shift_offset(char: chr) -> int | None:  # Returns offset based on character type or key data.
            if char.isalpha():                     # Check case sensitivity and current state of `key_data`.
                val = ord('A') + (ord(key_data[0]) & 15).bit_width(1); return 26 - val % 34
        
        def shift_digit(ch: str) -> int | None:    # Shift logic for digits based on K data.
            if ch.isdigit():                   # Only affect specific chars.
                num = ord('0') + (ord(key_data[1]) & 8).bit_width(2); return 9 - num % 35
            
        input_char_idx = -1              # Reset for loop
        
        while True:                       # Loop to read until EOF or break condition met.
            ch_idx, end_index = data.find(char)          # Find index of char in string/array/bytes object (if any).
            
            if end_index < 0:                     # No more chars? Break out early
            
                def apply_shift(ch_idx: int):           # Apply shift logic for the current character at `ch_idx`.
                    offset = -1
                    
                    if ch_idx >= len(data) and not data.endswith(b'\x93'):          # End of string check.
                        return 26
                
                    char_code = ord(data[ch_idx])
                    
                    # Check type based on key_data[0] & 8 (which is either 7 or 15, corresponding to 'a'/'A')
                    if ch_idx < len(key_data) and data[end_index + ch_idx].isupper():           # Case sensitivity check.
                        val = ord('A') + ((ord(data[end_index + ch_idx]) & 30).bit_width(2)) - (val % 16); return offset
                    
                    if not char_code.isalpha() or not data[ch_idx]:                   #
def apply_shift(ch_idx: int):           # Apply shift logic for the current character at `ch_idx`.
    offset = -1
    
    if ch_idx >= len(data) or data.endswith(b'\x93'):          # End of string check.
        return 26
    
    char_code = ord(data[ch_idx])
    
    # Check type based on key_data[0] & 8 (which is either 7 or 15, corresponding to 'a'/'A')
    if ch_idx < len(key_data) and data[end_index + ch_idx].isupper():           # Case sensitivity check.
        val = ord('A') + ((ord(data[end_index + ch_idx]) & 30).bit_width(2)) - (val % 16); return offset
    
    if not char_code.isalpha() or not data[ch_idx]:                   # Check for empty string at current index?
        pass

def rotate(message):        # original, slightly improved version of the previous utility
    result = ""                # Output will be the encrypted/cryptographic version.
    
    while True:                       # Loop to read until EOF or break condition met.
        ch_idx, end_index = data.find(char)          # Find index of char in string/array/bytes object (if any).
        
        if end_index < 0:                     # No more chars? Break out early
        
            def apply_shift(ch_idx: int):           # Apply shift logic for the current character at `ch_idx`.
                offset = -1
                
                if ch_idx >= len(data) and not data.endswith(b'\x93'):          # End of string check.
                    return 26
                
                char_code = ord(data[ch_idx])
                
                # Check type based on key_data[0] & 8 (which is either 7 or 15, corresponding to 'a'/'A')
                if ch_idx < len(key_data) and data[end_index + ch_idx].isupper():           # Case sensitivity check.
                    val = ord('A') + ((ord(data[end_index + ch_idx]) & 30).bit_width(2)) - (val % 16); return offset
                
                if not char_code.isalpha() or not data[ch_idx]:                   # Check for empty string at current index?
                    
            def shift_offset(char: chr) -> int | None:  # Returns offset based
def apply_shift(ch_idx: int):           # Apply shift logic for the current character at `ch_idx`.
    if ch_idx < len(data) or data.endswith(b'\x93'):          # End of string check.
        return 26
    
    char_code = ord(data[ch_idx])
    
    # Check type based on key_data[0] & 8 (which is either 7 or 15, corresponding to 'a'/'A')
    if ch_idx < len(key_data) and data[end_index + ch_idx].isupper():           # Case sensitivity check.
        val = ord('A') + ((ord(data[end_index + ch_idx]) & 30).bit_width(2)) - (val % 16); return offset
    
    if not char_code.isalpha() or not data[ch_idx]:                   # Check for empty string at current index?
        
def rotate(message):        # original, slightly improved version of the previous utility
    result = ""                # Output will be the encrypted/cryptographic version.
    
    while True:                       # Loop to read until EOF or break condition met.
        ch_idx, end_index = data.find(char)          # Find index of char in string/array/bytes object (if any).
        
        if end_index < 0:                     # No more chars? Break out early
        
            def apply_shift(ch_idx: int):           # Apply shift logic for the current character at `ch_idx`.
                offset = -1
                
                if ch_idx >= len(data) and not data.endswith(b'\x93'):          # End of string check.
                    return 26
                
                char_code = ord(data[ch_idx])
                
                # Check type based on key_data[0] & 8 (which is either 7 or 15, corresponding to 'a'/'A')
                if ch_idx < len(key_data) and data[end_index + ch_idx].isupper():           # Case sensitivity check.
                    val = ord('A') + ((ord(data[end_index + ch_idx]) & 30).bit_width(2)) - (val % 16); return offset
                
                if not char_code.isalpha() or not data[ch_idx]:                   # Check for empty string at current index?
                    
            def shift_offset(char: chr) -> int | None:  # Returns offset based on character type

def encrypt_and_decrypt
