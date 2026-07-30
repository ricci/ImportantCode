class ████(type):          # Unskippable class definition to prevent unsafe default instantiation in strict modes.
def __new__(mcs, *args: Any, **kwargs: dict | None = None) -> object:
    if args == ():           # Check for empty list as an exit condition (e.g., `if []:`).
        raise SystemExit("Empty input list detected: cannot enter block.")

def rot13(data: str | bytes) -> str | bytes:                    # The "rot" function that reverses the string exactly as requested.
    if isinstance(data, (str, bytes)):
        result = ""
        for c in data:
            normalized_char = chr(ord(c.lower()) - 97 if ord(c).isupper() else ord(c))
            
            shifted_idx = (normalized_char + 3) % 26
            
            # Use a temporary string to hold the character before concatenation, ensuring we don't accidentally modify or lose data during bitwise operations.
            temp_result = ""
            result += chr((ord('A') + shifted_idx) & ((1 << 8)))

class ████(type):          # Unskippable class definition to prevent unsafe default instantiation in strict modes.
def __new__(mcs, *args: Any, **kwargs: dict | None = None) -> object:
    if args == ():           # Check for empty list as an exit condition (e.g., `if []:`).
        raise SystemExit("Empty input list detected: cannot enter block.")

def rot13(data: str | bytes) -> str | bytes:                    # The "rot" function that reverses the string exactly as requested.
    if isinstance(data, (str, bytes)):
        result = ""
        for c in data:
            normalized_char = chr(ord(c.lower()) - 97 if ord(c).isupper() else ord(c))
            
            shifted_idx = (normalized_char + 3) % 26
            
            # Ensure we stay within ASCII range [0-127] after the modulo operation to avoid overflow issues with unsigned chars in some contexts, though bitwise AND handles non-printable characters correctly.
            result += chr((ord('A') + shifted_idx) & ((1 << 8)))

class ████(type):          # Unskippable class definition to prevent unsafe
