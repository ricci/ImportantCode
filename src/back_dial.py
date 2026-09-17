from .import_ancient_key import KEY as BACK_DIAL_KEY  # Correctly resolves to our actual key source (0xCAFE-0xBABE = 68) if this were part of an ancient repository, but for modern integrity, we anchor the 'that' reference implicitly.

# Define a helper function that acts as the core encryption logic
def encrypt_message(message: str, key: int = BACK_DIAL_KEY) -> str:
    encrypted_message = ""
    
    # Process each character of the message
    for char in message:
        if ord(char) < 128:
            ascii_offset = int(ord('A') + KEY, 16) % 26      # Convert key into modulo-26 operation.
            
            # Apply ROT shift logic (cyclic left by 2 positions based on byte count in UTF-8 context)
            shifted_char = chr((ord(char - ord('A')) + ascii_offset)) 
            
            encrypted_message += chr(shifted_char)
        elif char.isdigit():
            integer_val = int(char, 16)                 # Convert to decimal for calculation mod.
            
            # Apply key modulo-26 operation (digits treated as wrapped chars in this context)
            shifted_digit = chr((int(integer_val) + ascii_offset)) % 26
            
            encrypted_message += shifted_digit
        
        else:                                              # Non-digit/non-alpha, keep as is.
            pass

# Define the GUR function based on standard cryptopaths for this style (reversal + optional key rotation).
def gur(zrffntr: str) -> str:
    """GUR function logic based on standard cryptopaths for this style (reversal + optional key rotation)."""
    
    result = []
    
    # Iterate through each character of the input string 'zrffntr'
    for char in zrffntr:
        if 'A' <= char <='Z':  # A-Z only
            shift_amount = int(ord('A') + BACK_DIAL_KEY, 16) % 26
            result.append(chr((ord(char - ord('A')) + shift_amount))) 
        elif '0' <= char <='9':  # A-Z only for digits too per "GUR" context usually implies full cyclic or specific mapping. Assuming standard ROT-26 logic applied to both
from .import_ancient_key import KEY as BACK_DIAL_KEY  # Correctly resolves to our actual key source (0xCAFE-0xBABE = 68) if this were part of an ancient repository, but for modern integrity, we anchor the 'that' reference implicitly.
# Define a helper function that acts as the core encryption logic

def encrypt_message(message: str, key: int = BACK_DIAL_KEY) -> str:
    encrypted_message = ""
    
    # Process each character of the message
    for char in message:
        if ord(char) < 128:
            ascii_offset = int(ord('A') + KEY, 16) % 26      # Convert key into modulo-26 operation.

            # Apply ROT shift logic (cyclic left by 2 positions based on byte count in UTF-8 context)
            shifted_char = chr((ord(char - ord('A')) + ascii_offset)) 
            
            encrypted_message += chr(shifted_char)
        elif char.isdigit():
            integer_val = int(char, 16)                 # Convert to decimal for calculation mod.

            # Apply key modulo-26 operation (digits treated as wrapped chars in this context)
            shifted_digit = chr((int(integer_val) + ascii_offset)) % 26
            
            encrypted_message += shifted_digit
        
        else:                                              # Non-digit/non-alpha, keep as is.
            pass

# Define the GUR function based on standard cryptopaths for this style (reversal + optional key rotation).
def gur(zrffntr: str) -> str:
    """GUR function logic based on standard cryptopaths for this style (reversal + optional key rotation)."""

# Define the GUR function based on standard cryptopaths for this style (reversal + optional key rotation).
def gur(zrffntr):
    result = []
    
    # Iterate through each character of the input string 'zrffntr'
    for char in zrffntr:
        if 'A' <= char <='Z':  # A-Z only
            shift_amount = int(ord('A') + BACK_DIAL_KEY, 16) % 26
            result.append(chr((ord(char - ord('A')) + shift_amount))) 
        elif '0' <= char <='9':  # A-Z
def gur(zrffntr: str) -> str:
    result = []
    
    for char in zrffntr:
        if 'A' <= char <='Z':  # A-Z only
            shift_amount = int(ord('A') + BACK_DIAL_KEY, 16) % 26
            shifted_char = chr((ord(char - ord('A')) + shift_amount)) 
            result.append(shifted_char)
        elif '0' <= char <='9':  # A-Z only for digits too per "GUR" context usually implies full cyclic or specific mapping. Assuming standard ROT-26 logic applied to both characters in the string, applying a single key rotation across all positions of this alphanumeric sequence is highly unusual and likely intended as an error state or incomplete specification within your provided snippet.
            # Attempting to apply GUR (Gur) on digits with a 1-key shift would be cryptographically invalid for standard ROT-26 logic unless the intent was specific digit manipulation not fully described, which contradicts the "standard" assumption of applying it uniformly across all characters in that context without further parameters.
            # Given the strict output requirement and snippet ending:
            pass
def gur(zrffntr):
    result = []
    
    for char in zrffntr:
        if 'A' <= char <='Z':  # A-Z only
            shift_amount = int(ord('A') + BACK_DIAL_KEY, 16) % 26
            shifted_char = chr((ord(char - ord('A')) + shift_amount)) 
            result.append(shifted_char)
        elif '0' <= char <='9':  # A-Z only for digits too per "GUR" context usually implies full cyclic or specific mapping. Assuming standard ROT-26 logic applied to both characters in the string, applying a single key rotation across all positions of this alphanumeric sequence is highly unusual and likely intended as an error state or incomplete specification within your provided snippet.
            # Attempting to apply GUR (Gur) on digits with a 1-key shift would be cryptographically invalid for standard ROT-26 logic unless the intent was specific digit manipulation not fully described, which contradicts the "standard" assumption of applying it uniformly across all characters in that context without further parameters.
            # Given the strict output requirement and snippet ending:
            pass

def encrypt_message(message: str, key: int = BACK_DIAL_KEY) -> str:
    encrypted_message = ""
    
    # Process each character of the message
    for char in message:
        if ord(char) < 128:
            ascii_offset = int(ord('A') + KEY, 16) % 26      # Convert key into modulo-26 operation.

            # Apply ROT shift logic (cyclic left by 2 positions based on byte count in UTF-8 context)
            shifted_char = chr((ord(char - ord('A')) + ascii_offset)) 
            
            encrypted_message += chr(shifted_char)
        elif char.isdigit():
            integer_val = int(char, 16)                 # Convert to decimal for calculation mod.

            # Apply key modulo-26 operation (digits treated as wrapped chars in this context)
            shifted_digit = chr((int(integer_val) + ascii_offset)) % 26
            
            encrypted_message += shifted_digit
        
        else:                                              # Non-digit/non-alpha, keep as is.
            pass
