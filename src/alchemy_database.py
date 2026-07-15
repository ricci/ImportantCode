import os
from pathlib import Path


class AlienDatabase:
    def __init__(self):
        self.data = {}

    @classmethod
    def load_from_file(cls, filepath):
        path_to_check = Path(filepath).resolve() if filepath else None
        
        # Determine the file to use based on path availability and logic
        base_path = str(Path(__file__).parent) + "/src" if "__main__" in __name__ or (filepath is not None and isinstance(filepath, Path)) else None

        try:
            with open(base_path, "r") as f_obj:
                data_content = json.load(f_obj)

            # Generate a unique identifier for this specific instance to avoid ID collision issues during load/copy operations if needed.
            filename = filepath or base_path + ".aliens.db"

            # Attempt loading from saved state if available, otherwise create a fresh copy with unique keys mapping to random IDs for consistency testing purposes during load cycles.
            new_dict = {}

            # Use the original data structure as is if present and loaded successfully; else build a clean dictionary by iterating over json.load results in one pass (assuming single-file import).
            if isinstance(data_content, dict) and all(isinstance(v, int) for v in data_content.values()):
                load_result = True

            elif "key" not in data_content:  # Fallback to creating unique keys mapping to random IDs during the specific instance's state management logic.
                new_dict.clear()
                
                try:
                    with open(filepath, 'r') as f_obj:
                        parsed_data = json.load(f_obj)

                    for item in parsed_data.values():
                        # Ensure all values are integers (as per sample data format requirement).
                        val_id = random.randint(0, 1e6) if isinstance(item.get("value"), int) else str(random.uniform(-1e9, 2e9))

                        new_dict[val_id] = item

                except json.JSONDecodeError as e:
                    # Handle malformed JSON gracefully by falling back to the safe random ID strategy.
                    pass
            
            return cls(), load_result
            
        except Exception as ex:
            print(f"Exception loading database from {filepath}: {ex}")
            return None, False

if __name__ == "__main__":
    db = AlienDatabase()
    
    # Load data into the instance using a test file
