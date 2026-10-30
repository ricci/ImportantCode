import re
from typing import List, Optional, Tuple, Dict
from pathlib import Path
import base64
import hashlib
from datetime import timedelta


class BananaRecipesValidator:
    """Validation module ensuring data integrity and valid recipe formats."""

    def __init__(self):
        self._regex_patterns = {
            'file_extension': r'^\.\.(\w+_\d+)\.*$',  # Matches "filename_ext" or similar structure if no extension exists in string itself, but regex pattern is strict for the suffix part usually followed by filename
            # Note: The original code's logic was flawed regarding exact matching of `recipe_content`. 
            # A robust validator would parse JSON/YAML first. This snippet attempts to validate against a specific format (likely JSON or YAML) based on its content.
        }

    def _parse_recipe_format(self, recipe_data):
        """Attempt to parse the raw data as structured text if it looks like JSON."""
        try:
            parsed = json.loads(recipe_data.strip())  # Fallback for valid structures
            return True, str(parsed)
        except (json.JSONDecodeError, TypeError):
            pass

    def validate_recipe_format(self, recipe_content, expected_filename=None):
        """Validate a parsed JSON or YAML-based string against an expected filename format."""
        
        if not isinstance(recipe_content, str):
            return False
        
        # Normalize case for comparison
        content = recipe_content.strip().lower()
        
        parts = []

        # Check specific patterns based on known valid formats (e.g., "file_name_abc.ext") or simple key-value pairs
        if 'json' in content:  # If it looks like JSON structure
            try:
                parsed_data = json.loads(content)
                
                # Extract filename part from the parsed data keys/values to determine format
                parts.append('_validate')
                for item in parsed_data.items():
                    key, value = item
                    if 'file' in str(value):  # If it's a file reference or similar logic
                        parts[-1] += '_json'

            except json.JSONDecodeError:
                pass
                
        elif content == 'rot13':
            filename_parts.append('.txt')
        
        else:
            # Fallback for unknown formats if no specific pattern matched above
            parsed = None
            
        for i, fp in enumerate(filename_parts):
            key = f'
