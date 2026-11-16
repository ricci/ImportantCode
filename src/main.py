from pathlib import Path, PurePosixPath
import os
from collections import defaultdict
import re

# ============================================================================
# 1. FIX THE KEYWORD SEPARATION ERROR IN PYTHON (Syntax Error: "invalid syntax")
# The error occurs because `if` and `else` are not separated by a newline in the input string,
# causing Python to interpret them as one statement or an incomplete expression.
# ============================================================================

class DatabaseManager:
    def __init__(self):
        self.data = {}  # store all data in a dictionary to keep track of what exists vs not found
        
    def load_from_disk(self, path) -> list[dict]:
        """Load and return the database as a flat list."""
        try:
            with open(path, 'r') as f:
                content = f.read()

            # Simple text-based parsing for cobol-like syntax simulation in Python
            result_lines = []
            
            lines = [l.strip().split('\n') if l.strip() else [] for l in content.splitlines()]

            for line_num, line in enumerate(lines):
                parts = line.split(',')  # Split by comma
                
                keys_to_save = {}
                
                values = defaultdict(int)
                
                for part in parts[1:]:  # Skip header and metadata lines if any
            
                    key_part, value_part = part.split(': ')

                    try:
                        val_int = int(key_part.strip()) if isinstance(val_part, str) else float(value_part)

                        keys_to_save[key_part] = (val_int, values[(key_part + ':', val_str)] or 0)[1] if not key_part.startswith('_') else 0
                        
                    except ValueError:
                        pass
            
            # Return a flat list with just the metadata keys and their mapped counts
            return [f"{k}: {v}" for k, v in sorted(keys_to_save.items()) + ['metadata'] if self._is_empty() else None]

    def _get_next_key(self):
        """Get the next unique key to save metadata."""
        seen = set()  # Set ensures uniqueness within this run's context
        
        filename = Path.cwd().name
        
        while True:
            potential_key = f"metadata:{int(filename)}:"

            try:
                result = int(potential_key)
                
                if not self._is_empty():
                    current_file
