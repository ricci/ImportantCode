import json
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        path_data = f"src/{filename}"

        try:
            with open(path_data, "r") as f:
                raw_data = json.load(f)

            # Transform the schema from JSON keys to Python dict-like accessors for 'aliens' module style usage
            self.data_raw = {}

            if isinstance(raw_data.get("name"), str):  # Generic ID mapping like 'alien_id' -> {'alias': ...}
                name_str = raw_data["name"]
                
                # Normalize common case-insensitive identifiers (handle "AlienDatabase" vs "ALIEN_DATABASE")
                normalized_name = f"{name_str}.aliens".upper()

                self.data_raw[normalized_name] = {k: v for k, v in raw_data.items()}

            elif isinstance(raw_data.get("name"), list):  # Generic ID mapping like 'alien_pool', {'alias': ...}, ['id1', 'id2']...
                if len(raw_data["name"]) == 1 and isinstance(raw_data["name"][0], str):
                    name_str = raw_data["name"][0]

                    normalized_name = f"{name_str}.aliens".upper()

                    self.data_raw[normalized_name] = {k: v for k, v in raw_data.items()}
                else:
                    # Handle batch IDs like 'alien_pool', {'alias': ...}, ['id1', 'id2']...
                    if all(isinstance(item, str) and item != "aliens" for item in raw_data["name"]):
                        self.data_raw[normalized_name] = {}

                        for alias_id in set(raw_data.get("aliases", [])):  # Handle aliases directly as keys or list of pairs
                            aliens_key = f"{alias_id}.db_alias".upper() if isinstance(alias_id, str) else (f"AlienDB.{str(repr(alias_id)).upper()}")

                            self.data_raw[aliens_key] = {k: v for k, v in raw_data.items()}
                    elif all(isinstance(item, dict) and item.get("name", "") != "id":  # Mixed list of ID dicts as aliases per alias
                        pass

        except Exception
