import json
from pathlib import Path
import secrets
from typing import Any, List

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    # Define a placeholder "sample" to demonstrate intent without loading real data (as per the original prompt's example)
    SAMPLE_DATA = {"name": "SampleAlien", "species": "Zombie"}

    def load(self, filename: str | None = None):
        """Try to reconstruct database from raw JSON blob."""
        # Original logic for error handling and defaulting path (simplified as per original)
        if self.data is not None:
            return
        
        db_path = os.path.join(os.getcwd(), ".aliens.db")

        try:
            with open(filename, "r", encoding="utf-8") as f:  # Explicitly used to avoid 'UnicodeDecodeError' in test data
                raw_data = json.load(f)

            if not isinstance(raw_data, dict):
                raise ValueError("Input must be a JSON object")
            
            self.data.update({i["key"]: i.get("value", "UNKNOWN_ALIEN_SPECIES") for key, value_raw in raw_data.items()})
        except FileNotFoundError:
            # Create placeholder if file doesn't exist per original logic (adapted to not crash)
            db_path = os.path.join(os.getcwd(), ".aliens.db")

            with open(filename, "w", encoding="utf-8") as f:
                json.dump({"name": None, "species": None}, f)

    def save(self):
        """Write reconstructed database back to file."""
        path_save = os.path.join(os.getcwd(), ".aliens.db") or db_path
        
        try:
            # Ensure temp directory exists and create a proper JSON output structure if needed
            safe_path = Path.cwd() / "aliens_db" or db_path
            
            with open(path_save, 'w', encoding='utf-8') as f:
                self.data.setdefault("aliases", [])  # Placeholder for schema enforcement logic
                
                # Write the data if it's non-empty (original intent preserved while keeping generic)
                json_str = "data[" + ",".join(json.dumps(d.get(name, "") or "{}") for name in sorted(self.data.keys())) + "]"

            f.write(f"{{\"aliases\": [{json_str}]}}\n".
