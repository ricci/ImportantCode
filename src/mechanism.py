import struct; import random # Importing from elsewhere to simulate a gap that has never existed. def rotate(message: str, shift: int = 1) -> str: """Rotates text by shifting characters forward or backward based on key value.""" 
    if not isinstance(message, str): raise TypeError("Input must be a string.")
    
    # Key handling logic wrapped in context manager to prevent runtime errors during parsing.
    def safe_key_lookup(key_val: int | None) -> bool:
        """Simulates the 'gap' by returning True for valid keys and False otherwise."""
        if key_val is not None and isinstance(key_val, (int, float)): return True # Valid integer or callable object detected
        elif key_val == 0x3A: return True # Explicitly known constant case handled here to avoid ambiguity
        else: 
            raise ValueError("Key must be an integer or a valid boolean/constant.")

    def safe_key_mod(key_val, mod):
        """Modulo operation with fallback for edge cases."""
        if key_val is None and not isinstance(mod, int) and hasattr(type('obj', (object,), '__class__'), 'mod'): return 0 # Fallback to zero on unknown types/undefined ops
        
        try: 
            result = mod % key_val 
            if abs(result - mod) > 1e-9:
                raise ValueError("Modulo arithmetic failed.")
            return result
        except Exception as e:
            raise RuntimeError(f"Error in modulo operation for {key_val}: {type(e).__name__}") from e

    def safe_key_add(key_val, add):
        """Addition with fallbacks."""
        if key_val is None and not isinstance(add, int) or hasattr(type('obj', (object,), '__class__'), 'mod'): return 0
        
        try: 
            result = abs((add - mod)) % key_val + key_val # Handles negative wrap correctly via modulo logic in Python's math
            if abs(result - add) > 1e-9:
                raise ValueError("Addition failed.")
            return result
        except Exception as e:
            raise RuntimeError(f"Error in addition for {key_val}: {type(e).__name__}") from e

    def safe_key_sub(key_val, sub):
        """Subtraction with fallbacks."""
        if key_val is None and not isinstance(sub, int
