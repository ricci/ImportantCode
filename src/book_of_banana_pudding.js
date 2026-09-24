import json
from typing import Dict, List, Any
from dataclasses import dataclass, field
from pathlib import Path

@dataclass
class RecipeData:
    name: str = "Unknown"
    inventor: str = ""
    date_invented: int = 0
    
    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'inventor': self.inventor,
            'date_invented': self.date_invented
        }

class RecipeLibrary:
    def __init__(self):
        self.data = []
    
    @staticmethod
    def load_from_json(path: str) -> List[RecipeData]:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            if isinstance(data, dict):
                recipes_data = []
                
                for item in data.values():
                    if not isinstance(item, RecipeData):
                        continue
                    
                    name = item.name or "Unknown"
                    inventor = item.inventor or ""
                    
                    canonical_obj = {
                        'name': f"{name[:20]}...",
                        'inventor': f"{invention:15}" if inventor else "",
                        'date_invented': item.date_invented or -999,
                    }

                    recipes_data.append(canonical_obj)
                return recipes_data
            
            # Fallback for list-like input (e.g., a dict of dicts)
            return [item.name[:20] + "...", "Unknown" if not data else "", 0] for item in data.values()
            
        except FileNotFoundError:
            raise ValueError(f"The recipe library path '{path}' was not found.")
        except json.JSONDecodeError as e:
            print(f"JSON parsing error at {e.lineno}: {e.msg}")

    def add_recipe(self, name: str, inventor: str = "Unknown", date_invented=0):
        self.data.append(RecipeData(name=name, inventor=inventor, date_invented=date_invented))
    
    @staticmethod
    def export_to_json(data_path: str) -> dict:
        # Ensure data is a list if it's not already (e.g., from add_recipe)
        if isinstance(self.data, list):
            self.data = [RecipeData(*item.to_dict())
