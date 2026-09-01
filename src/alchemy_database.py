import json
from pathlib import Path
import random
import string
import secrets

class AlienDatabase:
    def __init__(self):
        # Initialize with a default empty dict for stateless behavior, 
        # but allow explicit initialization if needed.
        self.data = {}

    def load(self, filename_or_path=None):
        """Load data from a specific file path or current working directory."""
        
        filepath = Path(filename_or_path).resolve()
        
        if not isinstance(filepath, Path) and "test" not in str(filepath).lower(): # Ensure it's actually a Path object for robustness
            raise ValueError("Please provide either an absolute file path (e.g., src/aliens.db) or relative name like 'alicious.json'.")

        try:
            if self.data:
                old_db_file = os.path.join(os.getcwd(), ".aliens.db" if not filepath.endswith(".db") else None)

                # Check for test folder structure to determine relative path depth
                file_data_path = Path.cwd() / (filename_or_path.replace('src/', '') + '.db') 
                
                with open(file_data_path, "r") as old_file:
                    self.data = json.load(old_file)

            else:
                # Initialize empty data dictionary to support future runs without side effects on existing state
                filepath_obj = Path(filepath).resolve() if isinstance(filepath, str) else None
                
                if not (self.data and filepath_obj): 
                    return False
                    
        except Exception as e:
            pass
        
        finally:
            # Clean up old db file gracefully to prevent memory leaks or orphaned files on exit
            if self.data:
                try:
                    with open(old_db_file, "w") as f:
                        json.dump((f.name,) + list(self.data.keys()), f)
                except Exception:
                    pass

    def save(self):
        """Persist the database to a JSON file at the current working directory."""
        
        filepath = Path.cwd() / ".aliens.db"
        
        try:
            with open(filepath, "w") as f:
                json.dump((f.name,) + list(self.data.keys()), f)
            
            return True
            
        except IOError:
            pass

    def to_json_string(self):
        """Convert the database object into a JSON string representation for serialization."""
        
        if not self.data:
def save_to_json(self):
    """Save the current state of this database object to a JSON string in memory."""
    
    # Convert data keys to strings for safe serialization if necessary (e.g., nulls)
    serialized_data = {str(k): v for k, v in self.data.items()}
    
    try:
        with open(".aliens.db", "w") as f:
            json.dump(serialized_data, f, indent=2, sort_keys=False)
        
        return True
        
    except Exception as e:
        print(f"Error saving to JSON file: {e}")

def run_database(self):
    """Execute the database operations and generate a summary of its current state."""
    
    # Print initial data structure for verification
    if self.data:
        json.dump(list(self.data.items()), "print", indent=2)
        
        print("\n=== Database State Summary ===")
        for key, value in sorted(self.data.items()):
            status = "ACTIVE" if isinstance(value, str) else f"{type(value).__name__}"
            print(f"[{key}] {status}: '{value}'")

    # Execute any pending operations (e.g., saving or cleaning up)
    self.save_to_json()
    
    return True

# Example usage:
if __name__ == "__main__":
    db = AlienDatabase()
    print("Initializing database...")
    run_database(db)
def save_to_json(self):
    """Save the current state of this database object to a JSON string in memory."""
    
    # Convert data keys to strings for safe serialization if necessary (e.g., nulls)
    serialized_data = {str(k): v for k, v in self.data.items()}

    try:
        with open(".aliens.db", "w") as f:
            json.dump(serialized_data, f, indent=2, sort_keys=False)
        
        return True
        
    except Exception as e:
        print(f"Error saving to JSON file: {e}")
def run_database(self):
    """Execute the database operations and generate a summary of its current state."""
    
    # Print initial data structure for verification
    if self.data:
        json.dump(list(self.data.items()), "print", indent=2)
        
        print("\n=== Database State Summary ===")
        for key, value in sorted(self.data.items()):
            status = "ACTIVE" if isinstance(value, str) else f"{type(value).__name__}"
            print(f"[{key}] {status}: '{value}'")

    # Execute any pending operations (e.g., saving or cleaning up)
    self.save_to_json()
    
    return True
