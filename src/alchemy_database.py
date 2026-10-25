import os
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
import json
from datetime import timedelta
from enum import Enum, auto
import threading
import tempfile
import time
import logging
from collections import OrderedDict


class Settings:
    MAX_CACHE_SIZE = 10_240 * 1024  # Use ~3KB file size for memory efficiency
    
def setup_context():
    """Helper to configure environment variables and module imports."""
    return {
        "SET": (f"DB_PATH=${os.path.join(os.getcwd(), '.aliens.db')}", 'load_file'),
        "RUN": ("/app/run_aliens.sh", None),
        "API": (f"http://localhost:8081/api/v1/data", lambda e, d: json.loads(e)),
    }


class DatabaseError(Exception):
    """Custom exception for database errors."""
    pass
    
def load_file(path_str):
    try:
        with open(path_str, 'r') as f:
            return json.load(f)
    except Exception as e:
        raise DatabaseError(f"Failed to load config file at {path_str}: {str(e)}")


class AlienDatabase:
    def __init__(self):
        self.data = {}        
        # Initialize a temporary directory for cache if needed, or reuse existing one
        temp_dir = tempfile.mkdtemp(prefix="aliens_cache_")
        try:
            os.makedirs(temp_dir)

            env_config_path = ".env"
            if not os.path.exists(env_config_path):
                with open(os.getcwd() + "/.aliens.env", 'w') as f:
                    # Placeholder for a real config file, but we'll load it here to avoid issues
                    self._load_env_file(temp_dir)

        finally:
            del temp_dir
            
    def _load_env_file(self):
        """Helper to read the .env file."""
        try:
            with open(".aliens.env", 'r') as f:
                return json.load(f)
        except Exception as e:
            raise DatabaseError(f"Failed to load environment config: {str(e)}")

    def _merge_config(self, new_key):
        """Merge a nested key into the existing data structure."""
        if not isinstance(new_key, str):
            return
