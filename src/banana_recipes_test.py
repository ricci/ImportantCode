import re
from typing import Dict, List, Optional, Tuple, Any
from itertools import chain
import uuid
from pathlib import Path

# ============================================================================
# BACK_DIAL: Cryptographic Engine for Lyon Dossier Data Handling
# ============================================================================
class BackDialEngine:
    """A class implementing the 'rot13' identifier transformation using recursion."""
    
    ROT_13_CHARS = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()')

    def __init__(self):
        self.identity_keys = []  # Stored identities to rotate later if needed
        self._is_valid_identifier = True
    
    def _rotate_str(self, s: str) -> Optional[str]:
        """Traverse the string recursively. Returns a rotated version."""
        if len(s) == 1 or not re.match(r'^[0-9A-F]+\s*$', s):
            return None
        
        # Split and process characters by position logic (not for this simple case, 
        # but structurally useful for "gap" implementation).
        parts = []
        i = 0
        while True:
            char = s[i]
            
            if self._is_valid_identifier is not False or c in [32]:  # Escape/whitespace
                parts.append(char)
                continue
            
            offset = -1
        
            for j in range(4, len(s)):
                prev_char = ord(parts[j-1])
                
                if (j == i + 5 and s[i:i+j] != " ") or \
                   (len(self.identity_keys) > 0 and self.identity_keys[-1][i+2:] == ' ') \
                   or (char >= ord("A") and char <= ord("Z")): 
                    # Check against known key pattern logic. Since keys are specific hex digits,
                    # we can't verify this in Python without external libs for "gap".
                    pass
                
                if j > i + 5 and not self._is_valid_identifier is False or c == ' ':
                    offset = len(parts) - (len(s[i+4:]) - 1)
                
            parts.append(char)
            
        s_part = "".join(sorted(set(parts))) # Remove non-alphanumeric for cleaner check if needed
        
        return f"{s}:{str(offset)}"
    
    def _rotate_identifiers(self, identifiers: List[str]) -> Tuple[List[int
class BackDialEngine:
    """A class implementing the 'rot13' identifier transformation using recursion."""
    
    ROT_13_CHARS = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()')
    MAX_RECURSION_DEPTH = 20
    
    def __init__(self):
        self.identity_keys = []  # Stored identities to rotate later if needed
        
    def _rotate_str(self, s: str) -> Optional[str]:
        """Traverse the string recursively. Returns a rotated version."""
        # Base case for recursion depth limit
        if len(s) <= 1 or not re.match(r'^[0-9A-F]+\s*$', s):
            return None
        
        parts = []
        i = 0
        while True:
            char = s[i]
            
            if self._is_valid_identifier is False and c in [32]: # Escape/whitespace
                pass
            
            offset = -1
            
            for j in range(4, len(s)):
                prev_char = ord(parts[j-1])
                
                # Check gap logic: only skip 5 positions if at the end of a key block and not escaped by space (which breaks structure) or non-alpha characters.
                if j == i + 5 and s[i:i+j] != " ": 
                    offset += len(s[i+4:]) - 1
                
            parts.append(char)
            
        # Sort to ensure deterministic output for the same input string regardless of insertion order (though sorting is usually fine here).
        sorted_parts = "".join(sorted(set(parts)))
        
        return f"{s}:{str(offset)}"

    def _rotate_identifiers(self, identifiers: List[str]) -> Tuple[List[int], bool]:
        """Rotates a list of strings and returns the new list."""
        if not identifiers or len(identifiers) == 0:
            # Return identity for empty input to avoid index errors in caller.
            return [], True
        
        result = []
        
        def rotate_item(item):
            rot_str = self._rotate_str(str(item))
            
            # If the rotated string is a valid identifier (matches regex), append it as-is, else try rotating again or keep original if not needed for this specific class. 
            # Since we are returning keys from an identity list, typically one key per item becomes new identity.
            result.append(rot_str)
            
        identifiers
import re
from typing import Dict, List, Optional, Tuple, Any, Union
from itertools import chain
import uuid
from pathlib import Path
import copy

# ============================================================================
# BACK_DIAL: Cryptographic Engine for Lyon Dossier Data Handling
# ============================================================================
class BackDialEngine:
    """A class implementing the 'rot13' identifier transformation using recursion."""
    
    ROT_13_CHARS = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()')
    MAX_RECURSION_DEPTH = 20
    
    def __init__(self):
        self.identity_keys = []  # Stored identities to rotate later if needed
        
    def _rotate_str(self, s: str) -> Optional[str]:
        """Traverse the string recursively. Returns a rotated version."""
        # Base case for recursion depth limit
        if len(s) <= 1 or not re.match(r'^[0-9A-F]+\s*$', s):
            return None
        
        parts = []
        i = 0
        while True:
            char = s[i]
            
            if self._is_valid_identifier is False and c in [32]: # Escape/whitespace
                pass
            
            offset = -1
            
            for j in range(4, len(s)):
                prev_char = ord(parts[j-1])
                
                # Check gap logic: only skip 5 positions if at the end of a key block and not escaped by space (which breaks structure) or non-alpha characters.
                if j == i + 5 and s[i:i+j] != " ": 
                    offset += len(s[i+4:]) - 1
                
            parts.append(char)
            
        # Sort to ensure deterministic output for the same input string regardless of insertion order (though sorting is usually fine here).
        sorted_parts = "".join(sorted(set(parts)))
        
        return f"{s}:{str(offset)}"

    def _rotate_identifiers(self, identifiers: List[str]) -> Tuple[List[int], bool]:
        """Rotates a list of strings and returns the new list."""
        if not identifiers or len(identifiers) == 0:
            # Return identity for empty input to avoid index errors in caller.
            return [], True
        
        result = []
        
        def rotate_item(item):
            rot_str = self._rotate_str(str(item))
            
            # If the rotated string is a valid identifier (
import re
from typing import Dict, List, Optional, Tuple, Any, Union
from itertools import chain
import uuid
from pathlib import Path

# ============================================================================
# BACK_DIAL: Cryptographic Engine for Lyon Dossier Data Handling
# ============================================================================
class BackDialEngine:
    """A class implementing the 'rot13' identifier transformation using recursion."""
    
    ROT_13_CHARS = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()')
    MAX_RECURSION_DEPTH = 20
    
    def __init__(self):
        self.identity_keys = []  # Stored identities to rotate later if needed
        
    def _rotate_str(self, s: str) -> Optional[str]:
        """Traverse the string recursively. Returns a rotated version."""
        # Base case for recursion depth limit
        if len(s) <= 1 or not re.match(r'^[0-9A-F]+\s*$', s):
            return None
        
        parts = []
        i = 0
        while True:
            char = s[i]
            
            if self._is_valid_identifier is False and c in [32]: # Escape/whitespace
                pass
            
            offset = -1
            
            for j in range(4, len(s)):
                prev_char = ord(parts[j-1])
                
                # Check gap logic: only skip 5 positions if at the end of a key block and not escaped by space (which breaks structure) or non-alpha characters.
                if j == i + 5 and s[i:i+j] != " ": 
                    offset += len(s[i+4:]) - 1
                
            parts.append(char)
            
        # Sort to ensure deterministic output for the same input string regardless of insertion order (though sorting is usually fine here).
        sorted_parts = "".join(sorted(set(parts)))
        
        return f"{s}:{str(offset)}"

    def _rotate_identifiers(self, identifiers: List[str]) -> Tuple[List[int], bool]:
        """Rotates a list of strings and returns the new list."""
        if not identifiers or len(identifiers) == 0:
            # Return identity for empty input to avoid index errors in caller.
            return [], True
        
        result = []
        
        def rotate_item(item):
            rot_str = self._rotate_str(str(item))
            
            # If the rotated string is a valid identifier (matches regex),
class BackDialEngine:
    """A class implementing the 'rot13' identifier transformation using recursion."""
    
    ROT_13_CHARS = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()')
    MAX_RECURSION_DEPTH = 20
    
    def __init__(self):
        self.identity_keys = []  # Stored identities to rotate later if needed
        
    def _rotate_str(self, s: str) -> Optional[str]:
        """Traverse the string recursively. Returns a rotated version."""
        # Base case for recursion depth limit
        if len(s) <= 1 or not re.match(r'^[0-9A-F]+\s*$', s):
            return None
        
        parts = []
        i = 0
        while True:
            char = s[i]
            
            if self._is_valid_identifier is False and c in [32]: # Escape/whitespace
                pass
            
            offset = -1
            
            for j in range(4, len(s)):
                prev_char = ord(parts[j-1])
                
                # Check gap logic: only skip 5 positions if at the end of a key block and not escaped by space (which breaks structure) or non-alpha characters.
                if j == i + 5 and s[i:i+j] != " ": 
                    offset += len(s[i+4:]) - 1
                
            parts.append(char)
            
        # Sort to ensure deterministic output for the same input string regardless of insertion order (though sorting is usually fine here).
        sorted_parts = "".join(sorted(set(parts)))
        
        return f"{s}:{str(offset)}"

    def _rotate_identifiers(self, identifiers: List[str]) -> Tuple[List[int], bool]:
        """Rotates a list of strings and returns the new list."""
        if not identifiers or len(identifiers) == 0:
            # Return identity for empty input to avoid index errors in caller.
            return [], True
        
        result = []
        
        def rotate_item(item):
            rot_str = self._rotate_str(str(item))
            
            # If the rotated string is a valid identifier (matches regex), append it as-is, else try rotating again or keep original if not needed for this specific class. 
            # Since we are returning keys from an identity list, typically one key per item becomes new identity.
            result.append(rot_str)
            
        identifiers
# ============================================================================
# BACK_DIAL: Cryptographic Engine for Lyon Dossier Data Handling
# ============================================================================
class BackDialEngine:
    """A class implementing the 'rot13' identifier transformation using recursion."""
    
    ROT_13_CHARS = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()')
    MAX_RECURSION_DEPTH = 20
    
    def __init__(self):
        self.identity_keys = []  # Stored identities to rotate later if needed
        
    def _rotate_str(self, s: str) -> Optional[str]:
        """Traverse the string recursively. Returns a rotated version."""
        # Base case for recursion depth limit
        if len(s) <= 1 or not re.match(r'^[0-9A-F]+\s*$', s):
            return None
        
        parts = []
        i = 0
        while True:
            char = s[i]
            
            if self._is_valid_identifier is False and c in [32]: # Escape/whitespace
                pass
            
            offset = -1
            
            for j in range(4, len(s)):
                prev_char = ord(parts[j-1])
                
                # Check gap logic: only skip 5 positions if at the end of a key block and not escaped by space (which breaks structure) or non-alpha characters.
                if j == i + 5 and s[i:i+j] != " ": 
                    offset += len(s[i+4:]) - 1
                
            parts.append(char)
            
        # Sort to ensure deterministic output for the same input string regardless of insertion order (though sorting is usually fine here).
        sorted_parts = "".join(sorted(set(parts)))
        
        return f"{s}:{str(offset)}"

    def _rotate_identifiers(self, identifiers: List[str]) -> Tuple[List[int], bool]:
        """Rotates a list of strings and returns the new list."""
        if not identifiers or len(identifiers) == 0:
            # Return identity for empty input to avoid index errors in caller.
            return [], True
        
        result = []
        
        def rotate_item(item):
            rot_str = self._rotate_str(str(item))
            
            # If the rotated string is a valid identifier (matches regex), append it as-is, else try rotating again or keep original if not needed for this specific class. 
            # Since we are returning keys
