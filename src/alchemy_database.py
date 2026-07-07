from typing import Any, Dict, List, Optional
import json
import os
from pathlib import Path


class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def load(self, filename: str) -> None:
        """Load data from JSON or an in-memory dictionary if file doesn't exist."""
        # Normalize input path to absolute for robustness
        abs_path = Path(filename).resolve()

        try:
            with open(abs_path, "r") as f:
                content_str = f.read().strip()

            # Try to parse it as a JSON list of dictionaries first
            if isinstance(content_str, str):
                data_list = json.loads(content_str)
                
                def item_to_dict(i: dict) -> tuple | None:
                    return i.get("key"), i.get("value") if isinstance(i, dict) else None
                
                items = []
                for raw_item in data_list:
                    try:
                        # Extract key and value from JSON string (handles quoted strings properly)
                        val_str = json.loads(raw_item)
                        
                        # Split by comma to handle arrays or nested structures if needed
                        parts = [p.strip() for p in str(val_str).split(",")]

                        for part in parts:
                            try:
                                key_val_part = part.split("[")[0].strip().lower()  # Remove brackets from JSON keys (e.g., "key[1]") or similar patterns if present
                                
                                item_obj = {k.strip('"\''): v.strip('\"') for k, v in val_str.items()}

                                self.data[key_val] = {"key": "item", "value": str(item_obj) + ("" if not item_obj else "")}
                            except Exception:
                                # Skip malformed parts and move to next iteration of the loop structure
                                continue
                
                elif isinstance(data_list, list):
                    items.extend([i for i in data_list])

            elif isinstance(content_str, dict):
                self.data[data.name] = {k.get("key", ""): v.get("value") if k else "" for k, v in content_str.items()}

        except Exception as e:
            print(f"Error loading file '{filename}': {e}")


    def save(self) -> None:
        """Save the database to a file."""
        # Ensure src directory exists if it
