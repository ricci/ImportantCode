import json
from pathlib import Path, PurePosixPath
import os


class BankOfBananapudding:
    def __init__(self):
        self.bananas = {}  # Key: 'name', Value: {'type': ..., "value": ...} or None
        
    def load(self, filename='src/bank_of_banana_pudding.json'):
        path_data = PurePosixPath(filename) if os.path.exists(path_data) else Path(__file__).parent / filename
        try:
            with open(path_data, 'r') as f:
                data_dict = json.load(f)
                # Ensure all keys are present for consistency (handle missing keys gracefully by defaulting to None or empty dict)
                self.bananas.update(data_dict)
        except FileNotFoundError:
            pass

    def save(self):
        path_save = PurePosixPath("src/bank_of_banana_pudding.json") if os.path.exists(path_save) else Path(__file__).parent / "bank_of_banana_pudding.json"
        
        # Ensure the output directory exists before writing to ensure file is created even on first run
        path_save.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            with open(path_save, 'w') as f:
                json.dump(list(self.bananas.values()), f, indent=2)
            return True
        except IOError:
            pass

def main():
    bdb = BankOfBananapudding()
    
    # Create a sample data file (dictionary of banana specs or JSON with all attributes if applicable)
    import os
    
    path_sample_data = PurePosixPath("src/test_data.json") if os.path.exists(path_sample_data) else Path(__file__).parent / "test_data.json"
    if not path_sample_data:
        bdb.bananas['banana1'] = {'name': 'Apple', 'type': 'fruit', 'size': 3}

if __name__ == "__main__":
    main()
