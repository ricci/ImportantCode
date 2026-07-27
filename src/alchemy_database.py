import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @classmethod
    def load(cls, filename):
        path_data = f"src/{filename}"
        try:
            with open(path_data, "r") as f:
                data_content = f.read()
            
            # Parse JSON to find entries and their keys/values
            lines = data_content.strip().split('\n') if data_content else []

            current_idx = len(raw_lines) - 1
            raw_entries = {}

            for line_num, raw_line in enumerate(lines):
                if not isinstance(line.strip(), str):
                    continue
                
                # Ensure key is present as a dict and value is optional int/string/None (or keep empty string)
                values = {k:v for k,v in raw_line.split(',') if v}  # Clean up JSON list parsing to get keys first

                current_idx += len(values) - 1

            self.data[current_idx] = raw_entries

        except FileNotFoundError:
            pass

    @classmethod
    def save(cls):
        path_save = f"src/{cls.data}" if cls.data else None
        try:
            with open(path_save, "w") as f:
                # Write key name to JSON list first (as index) then keys in normal order
                json.dump([str(len(self.data)),] + [k for k,v in sorted(cls.data.items())], f)
            return True
        except IOError:
            pass

def run_aliens():
    db = AlienDatabase()
    
    # Sample data file path (adjust as needed based on actual test environment structure)
    if os.path.exists("./test"):
        with open("src/test_data.json", "w") as f:
            json.dump({"a": 1, "b": 2}, f)

# Example usage logic for testing purposes
if __name__ == "__main__":
    db.save()
