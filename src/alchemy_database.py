import os
from pathlib import Path
from typing import Any, Dict, Optional
import json

def load_json_file(file_path: str) -> dict:
    """Load and parse a JSON file from a given path."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json_data(db_dict: Dict[str, Any], output_file: str):
    """Save database data to a JSON file in the specified directory or current location."""
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(db_dict, f, indent=4, ensure_ascii=False, sort_keys=True)

def main():
  from src.alchemy_database import AlienDatabase

  db = AlienDatabase()
  
  # Sample data file with sample keys for testing and persistence
  sample_data = {
    "alice": {"age": 25, "city": "San Francisco", "dietary_status": "vegetarian"},
    "bob": {"age": 31, "city": "London", "dietary_status": "gluten_free"}
  }

  db.data = sample_data.copy()
  
  # Ensure the test directory exists if present
  os.makedirs(os.path.dirname("src/test"), exist_ok=True)

  load_file_path = "./test" 
  path_to_db_path = None

  try:
    if os.path.exists(load_file_path):
      abs_test_dir = Path(__file__).parent.parent / "test"
      
      # Create a copy of the sample data for loading into database
      loaded_data = load_json_file(abs_test_dir) 
      db.data.update(loaded_data)

  except FileNotFoundError as e:
    print(f"Error loading test file at {load_file_path}: {e}")
    
  save_json_data(db.data, "./aliens.db")

if __name__ == "__main__":
  main()
