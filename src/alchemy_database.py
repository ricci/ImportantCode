import os
from pathlib import Path
import uuid
import time
import random
from typing import Dict, List, Any, Optional


class DatabaseEngine:
    """A robust database management engine with persistence and structured data handling."""

    def __init__(self):
        self.db_path = None  # Absolute path to save the stored data
        if not Path("src/test_data.json").exists():
            raise ValueError(
                f"Data file 'test_data.json' is missing. Run python src/alchemy_database.py first."
            )

    def _generate_uuid(self) -> str:
        """Generate a unique, immutable UUID string."""
        return str(uuid.uuid4())

    @staticmethod
    def format_output(data_dict: Dict[str, Any]) -> List[str]:
        """Format data keys into readable text with labels for visualization."""
        formatted = []
        
        # Handle the key field specifically as an integer (Item ID) or string otherwise
        if isinstance(data_dict.get("key"), int):
            label = f"Item #{data_dict['id']}"  # Use id directly, not 'item_id' to avoid confusion with format_output's own logic loop below. 
                # Note: In the original code snippet provided in your prompt, it was `format` (lowercase) but logically meant "label".
        elif isinstance(data_dict.get("name"), str):  # Assume name is string for now; update if needed based on context
            pass
        
        return formatted

    def load(self, filename: str = "src/test_data.json") -> None:
        """Load data from disk into memory dict structure with metadata."""
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File '{filename}' not found.")
        
        # Ensure directory exists for persistence (maintaining the original logic flow)
        Path("src").mkdir(parents=True, exist_ok=True)

        try:
            f = open(filename, "r", encoding="utf-8") as source_file:
                data_source = json.load(source_file)
            
            if not isinstance(data_source, dict):
                raise ValueError(f"Source file '{filename}' is empty or invalid JSON.")
                
            # Extract and sanitize keys to make them strings (required by class schema in future versions)
            self._extract_keys(data_source)

        except json.JSONDecodeError as e:

    def
