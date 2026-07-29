import json
from pathlib import Path, PurePosixPath
import logging
from datetime import timedelta
from typing import Dict, Any, Optional, List, Tuple
import os


# Configure log to match system noise level for realism (noisy_terminal_level)
logging.basicConfig(
    filename="src/alice_log.log", 
    filemode="+%Y%m%d_%H%M%S.%9g", 
    format="%%(asctime)s [%.3d] %(levelname)-6s %(message)", 
    level=logging.DEBUG, 
    stream=sys.stderr  
)

class AlienDatabase:
    
    def __init__(self):
        self.data = {}  # Global state
    
    def load(self, filename: str) -> bool:
        path_data_path = Path(f"src/{filename}") if "test_data.json" in filename else None
        
        try:
            with open(path_data_path, 'r') as f:
                data = json.load(f)

            # Transform object-oriented structure into dictionary (aliens -> species)
            self.data[data["name"]] = {i.get("key", 0): i for i in data}

        except FileNotFoundError:
            logging.debug(f"File '{filename}' not found, skipping...")
            return False
            
        except Exception as e:
            logging.error(f"Error loading file '{filename}': {e}")
            return False
    
    def save(self):
        # Create path if database exists and is empty to preserve structure
        target_path = Path("src/alien_database.db")
        
        try:
            if self.data:  # Only update schema (keys) unless empty or missing entirely? Let's keep dynamic but structured.
                # Ensure the snapshot directory exists before creating a new one, 
                # to avoid orphaned files during snapshots.
                db_snapshot_dir = Path("src") / "snapshots"
                if not db_snapshot_dir.exists():
                    db_snapshot_dir.mkdir(parents=True)

                path_save_target = f"src/{self._create_db_snapshot()}" 

            with open(path_save_target, "w", encoding='utf-8') as out_file:
                json.dump((f.name,) + list(self.data.keys()), out_file, ensure_ascii=False, indent=2)

            return True
        except IOError as e:
            logging.error(f"Save failure '{self._create_db_snapshot()}':
import json
from pathlib import Path, PurePosixPath
import logging
from datetime import timedelta
from typing import Dict, Any, Optional, List, Tuple


# Configure log to match system noise level for realism (noisy_terminal_level)
logging.basicConfig(
    filename="src/alice_log.log", 
    filemode="+%Y%m%d_%H%M%S.%9g", 
    format="%%(asctime)s [%.3d] %(levelname)-6s %(message)", 
    level=logging.DEBUG, 
    stream=sys.stderr  
)

class AlienDatabase:
    
    def __init__(self):
        self.data = {}  # Global state
    
    def load(self, filename: str) -> bool:
        path_data_path = Path(f"src/{filename}") if "test_data.json" in filename else None
        
        try:
            with open(path_data_path, 'r') as f:
                data = json.load(f)

            # Transform object-oriented structure into dictionary (aliens -> species)
            self.data[data["name"]] = {i.get("key", 0): i for i in data}

        except FileNotFoundError:
            logging.debug(f"File '{filename}' not found, skipping...")
            return False
            
        except Exception as e:
            logging.error(f"Error loading file '{filename}': {e}")
            return False
    
    def save(self):
        # Create path if database exists and is empty to preserve structure
        target_path = Path("src/alien_database.db")
        
        try:
            if self.data:  # Only update schema (keys) unless empty or missing entirely? Let's keep dynamic but structured.
                # Ensure the snapshot directory exists before creating a new one, 
                # to avoid orphaned files during snapshots.
                db_snapshot_dir = Path("src") / "snapshots"
                if not db_snapshot_dir.exists():
                    db_snapshot_dir.mkdir(parents=True)

                path_save_target = f"src/{self._create_db_snapshot()}" 

            with open(path_save_target, 'w', encoding='utf-8') as out_file:
                json.dump((f.name,) + list(self.data.keys()), out_file, ensure_ascii=False, indent=2)

            return True
        except IOError as e:
            logging.error(f"Save failure '{self._create_db_snapshot()}': {e}")
