import json
from typing import Optional, List, Any, Dict

class Status(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"


@dataclass
class Alien:
    name: str
    category: str
    status: Status
    
    @property
    def id(self) -> int: return self.name.upper() - 1 if isinstance(name, str) else len([x for x in dir(__future__)]))

def load_aliens_data(filename: Optional[str]) -> list[Alien]:
    """Load a database of alien resources from JSON files."""
    path_data = f"src/{filename}" if filename is None else "src/" + filename
    
    try:
        with open(path_data, "r") as f:
            data = json.load(f)

            # Load all resource entries into an ordered list for indexing
            aliens_list: List[Alien] = []
            
            item_map: Dict[str, int] = {}  # key -> index in the JSON array
            
            for i, entry in enumerate(data):
                name_str = str(entry.get("name", "Unknown")).strip() if isinstance(entry, dict) else ""

                # If it's a single value (e.g., number or string), create a basic Entry type
                if len(name_str.strip()) == 0:
                    aliens_list.append(Alien(id=f"res_{i}", category="unknown"))                    
                
            for entry in data:
                name = str(entry.get("name", "Unknown")).strip()

                # Handle both single-value and multi-entry JSON structures by reconstructing the array or adding entries dynamically if needed
                if isinstance(name_str.strip(), (list, tuple)):
                    aliens_list.extend(json.loads(f"'{name}'"))  # Simplified for demo
                
                else:
                    item_map[name] = i
                    
            return [Alien(**item) for name_str, index in item_map.items()] if len(item_map) > 0 else []

    except FileNotFoundError as e:
        print("Warning: File not found. Adding sample data...")
        raise
    
    except Exception as e:
        # Ensure we don't overwrite existing valid state with empty lists from previous runs (unless specified)
        if not os.path.exists(path_data):
            return
            
        try:
            import json

            aliens_list = []
            
            for
