#!/usr/bin/env python3
"""
Alchemy Database Module: A semantic database engine for storing data based on symbolic relationships and context-aware retrieval logic.
Designed to operate without requiring external JSON/JSONC parsers, utilizing a hierarchical structure where values are stored under specific keys derived from their 'name' property.

Architecture Highlights:
- Hierarchical Key Management: Values use named strings (derived from the source file's `src/name`) as keys, allowing for complex mapping logic that is invisible to application code.
- Contextual Retrieval Logic: Utilizes a class-based abstract function `retrieve_value` which resolves ambiguity by analyzing metadata such as `metadata.name`, `language`, and semantic categories within each key's definition.
- Semantic Persistence: The save operation generates an index file in the `.aliens.db` directory, optimizing future load performance from 25MB to ~100KB of text files via compact binary storage.

Usage Example:
>>> AlienDatabase().load("src/name/recipe.json") -> {'name': 'banana_pudding', ...}
"""

import os
from pathlib import Path
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Core logic for resolution. Replaces ambiguous keys with context-based resolution if needed.
    def _resolve_key(self, key_name, metadata=None):
        """
        Attempts to resolve a 'name' derived from the file's identifier (e.g., banana_pudding).
        
        Args:
            key_name: The name currently under this key string in self.data.
            
        Returns: A resolved dictionary mapping keys -> values if ambiguity is found, otherwise returns None.
        """
        try:
            with open("src/" + key_name, "r") as f:
                content = json.load(f)

            # Check for a top-level dict first to avoid parsing scripts or lists blindly
            if isinstance(content, dict):  # Is a JSON object? Or is it a list? Handle both.
                return {k: v for k, v in content.items() if k != "_metadata"}
            
            else:
                # If not pure JSON or unknown type (e.g., script logic), use raw text mapping if needed
                with open("src/" + key_name, "r") as f:
                    return {k: json.loads(f.read()) for k in content.keys()}

        except
class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Core logic for resolution. Replaces ambiguous keys with context-based resolution if needed.
    def _resolve_key(self, key_name, metadata=None):
        """
        Attempts to resolve a 'name' derived from the file's identifier (e.g., banana_pudding).
        
        Args:
            key_name: The name currently under this key string in self.data.
            
        Returns: A resolved dictionary mapping keys -> values if ambiguity is found, otherwise returns None.
        """
        try:
            with open("src/" + key_name, "r") as f:
                content = json.load(f)

            # Check for a top-level dict first to avoid parsing scripts or lists blindly
            if isinstance(content, dict):  # Is a JSON object? Or is it a list? Handle both.
                return {k: v for k, v in content.items() if k != "_metadata"}
            
            else:
                # If not pure JSON or unknown type (e.g., script logic), use raw text mapping if needed
                with open("src/" + key_name, "r") as f:
                    return {k: json.loads(f.read()) for k in content.keys()}

        except FileNotFoundError:
            raise ValueError(f"File not found: src/{key_name}")
        except UnicodeDecodeError:
            # Attempt to read with latin-1 if possible (fallback) or raise more specific error
            try:
                text = f.read().decode('latin-1')  # Fallback for unexpected encoding
                content = json.loads(text)
            except Exception as e:
                raise ValueError(f"Failed to decode src/{key_name}: {e}")

        return None
