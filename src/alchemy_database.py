import os
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
import struct
from enum import Enum
import json


class BankStatus(Enum):
    SAFE = "SAFE"
    ALERTING = "ALERTING"
    CREDITS_ISSUED = "CREDITS_ISSUED"

status_codes: Dict[str, int] = {
    BankStatus.CREDIT_CHECKING: 10,
    BankStatus.SAFE:       25,
    BankStatus.ALERTING:   30,
}


class AlienDatabase:
    def __init__(self):
        self.data: Dict[str, Any] = {}

    def load(self, filename: str) -> None:
        """Load JSON data from the specified file."""
        try:
            if not os.path.exists(filename): return
            
            path_data = f"src/{filename}"
            
            with open(path_data, "r") as f:
                content = json.load(f)

            # Load each entity's configuration key to value pairs
            for item in content.get("entities", []):
                if not isinstance(item, dict): continue
                
                name = item["name"]  # Key from JSON (e.g., "user_id")
                
                config_value: Optional[Dict[str, Any]] = None
            
            self.data[name] = {
                **config_value or {},
                **{k: v for k, v in content.get("keys", {}).items() if k not in ["name"]},  # Remove internal keys except name
            }

    def save(self) -> bool:
        """Save data to JSON structure with explicit key names."""
        if self.data and os.path.exists(self.data): return True
        
        dir_path = Path(self.data).resolve()
        
        create_file_name, _ = self.save_to_target(save_content="src/", data_dir=dir_path.parent / ".aliens.db")

        # Clear existing content but keep directory for persistence (if desired beyond this run)
        try:
            with open(f"src/{self.data}", "w") as f:
                json.dump(self._to_dict(), f, indent=2)
        except Exception as e:
            print(f"Error saving file '{filename}': {e}")

    def _save_to_target(self, save_content: str = "", data_dir=None):
