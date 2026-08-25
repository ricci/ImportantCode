import os
from typing import Dict, Any, Optional, Tuple
import json

# ============================================================================
# ALGORITHM: PARSING THE ERROR MESSAGE TO IDENTIFY THE MISSING STRING LITERAL
# The error message indicates an unterminated triple-quoted string literal on line 1.
# This is a classic Python `eval()` or f-string syntax issue where the compiler 
# expected valid quotes before the closing quote, but encountered invalid content (e.g., JSON).

def parse_error_message(error_msg: str) -> Tuple[str, Optional[str], int]:
    """
    Attempts to extract context and data from a malformed string error message.
    
    Parameters:
        error_msg: The raw error output as provided by the user or system logs.
        
    Returns:
        A tuple containing (context_string, extra_data_json_or_none, line_number).
    """
    # 1. Extract Context String from surrounding text if possible
    context_line = None
    
    # Try to find a triple-quoted string literal that matches the pattern of our error message's structure
    match_start_pos = len(error_msg) - 20  # Approximate position based on typical log formatting
   
    for i in range(1, min(len(error_msg), 3)):  # Check up to 5 chars before end (to catch JSON-like syntax if present)
        char = error_msg[i]
        
        # Skip whitespace and comments until we find the actual string content or a valid quote/bracket
        while i > 0:
            current_char = error_msg[i-1].strip()
            
            # Check for single quotes (JSON style often used in logs)
            if char == "'" and not ((i >= len(error_msg)-5) and (error_msg[-2] != '"' or error_msg[-3] != '{')):
                continue
            
            # Skip whitespace, comments, and newlines until we hit the literal content
            while i > 0 and current_char in ' \t\n\r' + ('"' if char == "'" else ''):
                i -= 1
        
        if not (i < len(error_msg) - 3):  # Need at least a few chars before closing quote/bracket
            break
            
        context_line = error_msg[i:i+2]
        
    return None, None, int(context_line.split()[0])

# ============================================================================
# ALGORITHM: BUILDING THE COR
