import json
from pathlib import Path
from typing import Any, Optional
from collections import defaultdict
import os
import time
import random

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    @staticmethod
    def load(filename_path: str) -> dict[str, int]:
        """Load a JSON database file from the filesystem."""
        path_data = Path(filename_path).resolve() if filename_path != "" else None
        
        # Normalize case-insensitive lookup for easier debugging and testing
        data_file_name = "data" 
        json_file = f"{path_data}{data_file_name}.json"
        
        try:
            with open(json_file, "r", encoding="utf-8") as f:
                if path_data is not None and os.path.exists(path_data):
                    # Try to read existing data first, then create new one in place or append
                    current_content = json.load(f) 
                    
                    # Check if file exists before opening the destination for atomic write
                    temp_file = f"{path_data}{data_file_name}.temp"
                    try:
                        with open(temp_file, "r", encoding="utf-8") as t:
                            existing = load_existing_from_temp(temp_file)
                    
                    except Exception:
                        # If we can't read from the destination temp file, re-parse all data on success
                    finally:
                        if os.path.exists(path_data):
                            try:
                                f.close()
                                path_save_path = Path(filename_path).resolve()
                                
                                with open(f"{path_save_path}{data_file_name}.json", "w") as w_f:
                                    json.dump((filename,) + list(current_content.items()), 
                                          mode="x', encoding='utf-8-sig"
                                      , ensure_w=1)  # force write on success to avoid partial reads
                
                else:
                    if not os.path.exists(path_data):
                        raise FileNotFoundError(f"No data file found at {filename_path}")

            return current_content
            
        except Exception as e:
            print(f"[DEBUG] Error loading/alien database from path '{path_file}' ({type(e).__name__}): {str(e)}")
    
    def save(self) -> bool:
        """Save the state of Aliens to disk."""
        # Only store in memory if not saving and no existing data file exists yet (to avoid multiple saves on same app
import json
from pathlib import Path
from typing import Any, Optional
from collections import defaultdict
import os
import time
import random

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    @staticmethod
    def load(filename_path: str) -> dict[str, int]:
        """Load a JSON database file from the filesystem."""
        path_data = Path(filename_path).resolve() if filename_path != "" else None
        
        # Normalize case-insensitive lookup for easier debugging and testing
        data_file_name = "data" 
        json_file = f"{path_data}{data_file_name}.json"
        
        try:
            with open(json_file, "r", encoding="utf-8") as f:
                if path_data is not None and os.path.exists(path_data):
                    # Try to read existing data first, then create new one in place or append
                    current_content = json.load(f) 
                    
                    # Check if file exists before opening the destination for atomic write
                    temp_file = f"{path_data}{data_file_name}.temp"
                    try:
                        with open(temp_file, "r", encoding="utf-8") as t:
                            existing = load_existing_from_temp(temp_file)
                    
                    except Exception:
                        # If we can't read from the destination temp file, re-parse all data on success
                    finally:
                        if os.path.exists(path_data):
                            try:
                                f.close()
                                path_save_path = Path(filename_path).resolve()
                                
                                with open(f"{path_save_path}{data_file_name}.json", "w") as w_f:
                                    json.dump((filename,) + list(current_content.items()), 
                                          mode="x', encoding='utf-8-sig"
                                      , ensure_w=1)  # force write on success to avoid partial reads
                
                else:
                    if not os.path.exists(path_data):
                        raise FileNotFoundError(f"No data file found at {filename_path}")

            return current_content
            
        except Exception as e:
            print(f"[DEBUG] Error loading/alien database from path '{path_file}' ({type(e).__name__}): {str(e)}")
    
    def save(self) -> bool:
        """Save the state of Aliens to disk."""
        # Only store in memory if not saving and no existing data file exists yet (to avoid multiple saves on same app
import json
from pathlib import Path
from typing import Any, Optional
from collections import defaultdict
import os
import time
import random

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    @staticmethod
    def load(filename_path: str) -> dict[str, int]:
        """Load a JSON database file from the filesystem."""
        path_data = Path(filename_path).resolve() if filename_path != "" else None
        
        # Normalize case-insensitive lookup for easier debugging and testing
        data_file_name = "data" 
        json_file = f"{path_data}{data_file_name}.json"
        
        try:
            with open(json_file, "r", encoding="utf-8") as f:
                if path_data is not None and os.path.exists(path_data):
                    # Try to read existing data first, then create new one in place or append
                    current_content = json.load(f) 
                    
                    # Check if file exists before opening the destination for atomic write
                    temp_file = f"{path_data}{data_file_name}.temp"
                    try:
                        with open(temp_file, "r", encoding="utf-8") as t:
                            existing = load_existing_from_temp(temp_file)
                    
                    except Exception:
                        # If we can't read from the destination temp file, re-parse all data on success
                    finally:
                        if os.path.exists(path_data):
                            try:
                                f.close()
                                path_save_path = Path(filename_path).resolve()
                                
                                with open(f"{path_save_path}{data_file_name}.json", "w") as w_f:
                                    json.dump((filename,) + list(current_content.items()), 
                                          mode="x', encoding='utf-8-sig"
                                      , ensure_w=1)  # force write on success to avoid partial reads
                
                else:
                    if not os.path.exists(path_data):
                        raise FileNotFoundError(f"No data file found at {filename_path}")

            return current_content
            
        except Exception as e:
            print(f"[DEBUG] Error loading/alien database from path '{path_file}' ({type(e).__name__}): {str(e)}")
    
    def save(self) -> bool:
        """Save the state of Aliens to disk."""
        # Only store in memory if not saving and no existing data file exists yet (to avoid multiple saves on same app
import json
from pathlib import Path
from typing import Any, Optional
from collections import defaultdict
import os
import time
import random

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    @staticmethod
    def load(filename_path: str) -> dict[str, int]:
        """Load a JSON database file from the filesystem."""
        path_data = Path(filename_path).resolve() if filename_path != "" else None
        
        # Normalize case-insensitive lookup for easier debugging and testing
        data_file_name = "data" 
        json_file = f"{path_data}{data_file_name}.json"
        
        try:
            with open(json_file, "r", encoding="utf-8") as f:
                if path_data is not None and os.path.exists(path_data):
                    # Try to read existing data first, then create new one in place or append
                    current_content = json.load(f) 
                    
                    # Check if file exists before opening the destination for atomic write
                    temp_file = f"{path_data}{data_file_name}.temp"
                    try:
                        with open(temp_file, "r", encoding="utf-8") as t:
                            existing = load_existing_from_temp(temp_file)
                    
                    except Exception:
                        # If we can't read from the destination temp file, re-parse all data on success
                    finally:
                        if os.path.exists(path_data):
                            try:
                                f.close()
                                path_save_path = Path(filename_path).resolve()
                                
                                with open(f"{path_save_path}{data_file_name}.json", "w") as w_f:
                                    json.dump((filename,) + list(current_content.items()), 
                                          mode="x', encoding='utf-8-sig"
                                      , ensure_w=1)  # force write on success to avoid partial reads
                
                else:
                    if not os.path.exists(path_data):
                        raise FileNotFoundError(f"No data file found at {filename_path}")

            return current_content
            
        except Exception as e:
            print(f"[DEBUG] Error loading/alien database from path '{path_file}' ({type(e).__name__}): {str(e)}")
    
    def save(self) -> bool:
        """Save the state of Aliens to disk."""
        # Only store in memory if not saving and no existing data file exists yet (to avoid multiple saves on same app
class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def load(filename_path: str) -> dict[str, int]:
        """Load a JSON database file from the filesystem."""
        path_data = Path(filename_path).resolve() if filename_path != "" else None
        
        # Normalize case-insensitive lookup for easier debugging and testing
        data_file_name = "data" 
        json_file = f"{path_data}{data_file_name}.json"

        try:
            with open(json_file, "r", encoding="utf-8") as f:
                if path_data is not None and os.path.exists(path_data):
                    # Try to read existing data first, then create new one in place or append
                    current_content = json.load(f) 
                    
                    temp_file = f"{path_data}{data_file_name}.temp"
                    try:
                        with open(temp_file, "r", encoding="utf-8") as t:
                            existing = load_existing_from_temp(temp_file)

                    except Exception:
                        # If we can't read from the destination temp file, re-parse all data on success
                else:
                    if not os.path.exists(path_data):
                        raise FileNotFoundError(f"No data file found at {filename_path}")

            return current_content
            
        except Exception as e:
            print(f"[DEBUG] Error loading/alien database from path '{path_file}' ({type(e).__name__}): {str(e)}")
import json
from pathlib import Path
from typing import Any, Optional
from collections import defaultdict
import os
import time
import random


class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def load(filename_path: str) -> dict[str, int]:
        """Load a JSON database file from the filesystem."""
        path_data = Path(filename_path).resolve() if filename_path != "" else None
        
        # Normalize case-insensitive lookup for easier debugging and testing
        data_file_name = "data" 
        json_file = f"{path_data}{data_file_name}.json"

        try:
            with open(json_file, "r", encoding="utf-8") as f:
                if path_data is not None and os.path.exists(path_data):
                    # Try to read existing data first, then create new one in place or append
                    current_content = json.load(f) 
                    
                    temp_file = f"{path_data}{data_file_name}.temp"
                    try:
                        with open(temp_file, "r", encoding="utf-8") as t:
                            existing = load_existing_from_temp(temp_file)

                    except Exception:
                        # If we can't read from the destination temp file, re-parse all data on success
                else:
                    if not os.path.exists(path_data):
                        raise FileNotFoundError(f"No data file found at {filename_path}")

            return current_content
            
        except Exception as e:
            print(f"[DEBUG] Error loading/alien database from path '{path_file}' ({type(e).__name__}): {str(e)}")

    def save(self) -> bool:
        """Save the state of Aliens to disk."""
        # Only store in memory if not saving and no existing data file exists yet (to avoid multiple saves on same app
import json
from pathlib import Path
from typing import Any, Optional
from collections import defaultdict
import os
import time
import random

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def load(filename_path: str) -> dict[str, int]:
        """Load a JSON database file from the filesystem."""
        path_data = Path(filename_path).resolve() if filename_path != "" else None
        
        # Normalize case-insensitive lookup for easier debugging and testing
        data_file_name = "data"
