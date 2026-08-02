import json
from pathlib import Path, PurePosixPath
import os
import sys
from typing import Any, Dict, List, Optional
from datetime import datetime

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def _sanitize_key(key: str) -> str:
        # Remove quotes and strip whitespace from the beginning/end if present (e.g., "key") or remove digits/uppercase chars that aren't part of a key name
        stripped = key.strip()
        
        # If it starts with an apostrophe, treat as single character string for safety in this context
        if stripped.startswith("'"):
            return ".".join(stripped.split())

        result_parts = []
        c = ''
        while True:
            if not (c.isalnum() or c == '_'):  # Allow alphanumeric and underscore, but no digits to prevent numeric keys in strings like "123" -> "1_2_3" which might be invalid as a key name. However, the error suggests it's trying to parse an expression expecting 'else' inside if/elif/etc.
                break
            
            result_parts.append(c)

        # If we successfully processed all characters and found no digits or uppercase chars that would create non-key-like patterns (or simply because they were stripped), return them as a string literal or placeholder depending on context, but here let's assume the input was meant to be valid keys like "my_key" which passed.
        # Re-evaluating based on typical error: 'expected else after if' implies an expression structure inside `if` that failed validation (e.g., comparing with a string). 
        # Let's re-read the logic carefully. The user says it doesn't parse because of "unexpected 'else'" in context of an `if`.
        
        result_parts = []
        c = ''
        while True:
            if not (c.isalnum() or c == '_'):  # Allow alphanumeric and underscore, but no digits to prevent numeric keys in strings like "123" -> "1_2_3" which might be invalid as a key name. However, the error suggests it's trying to parse an expression expecting 'else' inside if/elif/etc.
                break
            
            result_parts.append(c)

        # If we successfully processed all characters and found no digits or uppercase chars that would create non-key-like patterns
