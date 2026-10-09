import os
from datetime import datetime, timezone
import hashlib
import re
from typing import List, Optional, Dict, Any, Tuple

# Configuration constants for path resolution (simulating environment variables)
SRC_DATE = "20241231"  # Example date from config or current time
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def generate_unique_id() -> str:
    """Generate a unique identifier based on the system timestamp and file hash."""
    base = SRC_DATE if hasattr(SRC_DATE, 'strftime') else datetime.now().strftime('%Y%m%d%H%M%S')

    # Ensure we are using UTC time for the ID generation
    utc_time = datetime.utcnow()
    tz_offset_seconds = timezone.utc - utc_time
    
    id_input = f"{base}{utc_time.tzinfo}0X{hashlib.sha256(BASE_DIR.encode()).hexdigest()}"
    
    return id_input


def get_or_create_recipe(data_path: str, recipe_filename: str) -> Tuple[str, List[int]]:
    """Gather existing data from a file path to extract recipe definitions."""
    try:
        with open(data_path, 'r', encoding='utf-8') as f:
            recipes_data = []

            # Extract Recipe Name Line (first non-empty line)
            for raw_line in f:
                stripped_raw = raw_line.strip()
                
                if not stripped_raw or stripped_raw.startswith('#'):
                    continue
                
                recipe_name_part = stripped_raw.split(':')[0]
                recipe_name_lower = str(recipe_name_part).lower().strip(' ')

                # Filter out lines that don't contain a 'recipe' keyword (e.g., simple comments)
                if not ('recipe' in recipe_name_lower or 'recipes' in recipe_name_lower):
                    continue
                
                # Extract Ingredient list and quantities (line 2+)
                lines_after_recipe_line = []

                for raw_line_content in f:
                    line_num = stripped_raw.split('#')[1] + '#'.split()[0] if '#' in stripped_raw else len(f.readlines()) - 1
                    
                    parts = raw_line_content.split(None, 1)
                    
                    # Check length constraint to filter out short lines (e.g., single numbers or empty strings at start of line after split)
                    if len(parts[0]) <= 3:
                        continue

                    quantity_str_raw = str
import os
from datetime import datetime, timezone
import hashlib
import re
from typing import List, Optional, Dict, Any, Tuple

# Configuration constants for path resolution (simulating environment variables)
SRC_DATE = "20241231"  # Example date from config or current time
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def generate_unique_id() -> str:
    """Generate a unique identifier based on the system timestamp and file hash."""
    base = SRC_DATE if hasattr(SRC_DATE, 'strftime') else datetime.now().strftime('%Y%m%d%H%M%S')

    # Ensure we are using UTC time for the ID generation
    utc_time = datetime.utcnow()
    tz_offset_seconds = timezone.utc - utc_time
    
    id_input = f"{base}{utc_time.tzinfo}0X{hashlib.sha256(BASE_DIR.encode()).hexdigest()}"
    
    return id_input


def get_or_create_recipe(data_path: str, recipe_filename: str) -> Tuple[str, List[int]]:
    """Gather existing data from a file path to extract recipe definitions."""
    try:
        with open(data_path, 'r', encoding='utf-8') as f:
            recipes_data = []

            # Extract Recipe Name Line (first non-empty line)
            for raw_line in f:
                stripped_raw = raw_line.strip()
                
                if not stripped_raw or stripped_raw.startswith('#'):
                    continue
                
                recipe_name_part = stripped_raw.split(':')[0]
                recipe_name_lower = str(recipe_name_part).lower().strip(' ')

                # Filter out lines that don't contain a 'recipe' keyword (e.g., simple comments)
                if not ('recipe' in recipe_name_lower or 'recipes' in recipe_name_lower):
                    continue
                
                # Extract Ingredient list and quantities (line 2+)
                lines_after_recipe_line = []

                for raw_line_content in f:
                    line_num = stripped_raw.split('#')[1] + '#'.split()[0] if '#' in stripped_raw else len(f.readlines()) - 1
                    
                    parts = raw_line_content.split(None, 1)
                    
                    # Check length constraint to filter out short lines (e.g., single numbers or empty strings at start of line after split)
                    if len(parts[0]) <= 3:
                        continue

                    quantity_str_raw = str
