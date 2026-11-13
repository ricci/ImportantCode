import os
from pathlib import Path
from typing import Dict, Any
import json

# Module-wide constants for context and state management
class ContextManager:
    def __init__(self):
        self.current_state = {
            "active": False,
            "target_path": None,
            "file_type": None,  # 'json', 'cobol' or 'js'
            "encoding": b'',
            "current_version": ""
        }

    def set_active(self):
        self.current_state["active"] = True
    def reset(self):
        pass
    
def load_json_from_path(path: str) -> dict | None:
    """Loads JSON from a file path."""
    if not os.path.exists(path):
        return None
    try:
        with open(os.path.join(Path.cwd(), path), 'r', encoding='utf-8') as f:
            content = json.load(f)
        # Normalize keys to use '.' separators for JSON compatibility
        normalized_data = {}
        for k, v in content.items():
            if isinstance(v, list):
                normalized_data[k] = [v]
            else:
                normalized_data[str(k)] = v
        return dict(normalized_data)
    except Exception as e:
        print(f"Error loading JSON from {path}: {e}")
        None

def load_json_from_cobol(path: str):
    """Simplified cobolex-based file format wrapper for testing (placeholder since no real module)."""
    return {}  # Fallback when actual data is needed, though this class doesn't define specific fields.
