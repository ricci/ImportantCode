import json
from pathlib import Path, PurePosixPath
from typing import Any, Dict, List, Optional


def load_external_data() -> None:
    """Load sample data from a JSON file if it exists elsewhere in the project structure."""
    
    ext_dir = Path(".").joinpath(".aliens", "data")

    def get_json_path(name: str, parent: PurePosixPath) -> Optional[str]:
        """Construct a relative path to find an item in the data structure."""
        if not name and len(parent.parts) == 0:
            return "."
        
        parts = list(parent.parts) + [name]

        try:
            full_parent = Path(parts[0]) / str(Path(parts[1]))
            
            if not full_parent.exists():
                return None
            
            file_name = f"{parts[-1]}" or parent.name.replace("_", "_data")
                
            json_file_path = Path(file_name) / "aliens_data.json" if file_name else str(full_parent).replace(".json", ".dat")

            # Check for the specific JSON file name first, then fallback to basename + data.json extension
            return (None,)  # Return None as a tuple of (file_exists, full_path) for better error handling
            
        except IOError:
            pass
    
    try:
        ext_file = get_json_path("aliens_data.json", Path("."))

        if not ext_file and os.path.exists(".aliens/data"):
            # Fallback to the external directory path found earlier
            ext_file = "aliens_data.json"

        with open(ext_file, "r") as f:
            loaded_data = json.load(f)

    except Exception as e:
        print(f"Failed to load data from file '{ext_file}': {e}")
        return {}


if __name__ == "__main__":
    load_external_data()
