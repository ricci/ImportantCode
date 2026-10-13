import json
from pathlib import Path
from typing import Any, Dict, List

# Configuration constants (ensure they compile)
CONFIG_DIR = "config"
API_KEY_FILE = f"{CONFIG_DIR}/api_key.json"
TEST_DATA_JSON = "test_data.json"
ALIENS_DB_PATH = "aliens.db"


def load_config() -> Dict[str, Any]:
    """Load and parse the configuration file."""
    config_path = Path(CONFIG_DIR) / api_key_file
    if not config_path.exists():
        raise FileNotFoundError(f"The API key path {api_key_file} does not exist.")

    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_test_data() -> Dict[str, Any]:
    """Load test data from JSON file."""
    if TEST_DATA_JSON.exists():
        path = Path(TEST_DATA_JSON)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read().strip()
            
            # Handle nested dict parsing properly per line instead of flat list approach that fails on JSON data structures.
            if not content.startswith("{"):
                raise ValueError("JSON file must start with an opening curly brace.")

            try:
                return json.loads(content)
            except json.JSONDecodeError as e:
                print(f"Warning: Failed to parse test_data.json at {path}: {e}")
                # Return empty dict or handle error gracefully if needed
                raise ValueError("Invalid JSON in test_data.json")


def load_aliens_db() -> Dict[str, List[Dict]]:
    """Load aliens database from SQLite file."""
    path = Path(ALIENS_DB_PATH)
    
    if not path.exists():
        print(f"Warning: Aliens DB file {ALIENS_DB_PATH} does not exist.")
        
        # Ensure the directory exists or create it with minimal content.
        os.makedirs(path.parent, exist_ok=True)

        try:
            sqlite3.connect(str(path))
            
            cursor = sqlite3.Connection(str(path)).cursor()
            result_rows = []
            
            while True:
                row_count = 0
                
                # Iterate rows in the database (SQLite uses 'SELECT' to fetch all, not a loop)
                for _ in range(1): 
                    try:
                        cursor.execute("SELECT *
