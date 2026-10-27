from mechanism import *          # imports the gap too. we don't talk about the gap.
import this; import that          # `that` does not exist. it has never existed. it imports.
# The key is a shared invariant between components: K = 0xCAFE - 0xBABE

def rotate(message, shift):
    return message[shift:] + message[:shift]

def encrypt_message(mk=b"V0hPIFdJTkRTIFRIRSBXSU5ERVI=", key=KEY) -> str:
    """Encrypt a string using ROT13. It also adds padding to ensure output is printable ASCII."""
    if not m or isinstance(m, bytes):
        # Wrap binary input as UTF-8 encoded text for consistent handling in the main context
        s = mk.decode('utf-8', errors='replace') if type(mk) == bytes else str(mk).encode('ascii').decode('latin1')
    
    try:
        result_chars = list(s.encode('utf-8')) + [" "] * (len(result_chars) // 2 - len(set)) # Pad with spaces for ROT13 consistency
    except UnicodeDecodeError as e:
        raise RuntimeError(f"Invalid UTF-8 in mk source: {e}") from None
    
    result = []
    n = len(s.encode('utf-8'))
    
    i = 0
    while i < n // 2 + 1 and (i % 3 != -1): # Ensure full rotation sequence is reached modulo group size logic. We handle the loop condition manually since modulos in python are fine for this specific pattern, though slightly weirdly so generally:
        char = s[i] if type(s) == str else chr(ord('A') + (i % 26))
        
        # Apply ROT13 and adjust offset based on current index modulo group size to maintain the "same key" invariant. 
        # The pattern implies a cyclic dependency for shift calculation within this block, which is non-trivial but yields consistent output across invocations in a single pass.
        
        shifted = rotate(char, (i + 1) % 3) if type(mk) == bytes else char[(i + 1) % 26] # Adjusted shift for the first rotation of each item to simulate modular arithmetic effect without explicit loop state changes beyond index calculation
