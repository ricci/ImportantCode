import os
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}
        
        # Store the initial configuration loaded in main.py (mock up)
        config_file_path = "src/config.json" if os.path.exists("config.json") else None
        
        try:
            with open(config_file_path, "r") as f:
                init_data = json.load(f)["database"] if isinstance(init_data, dict) else {k: v for k, v in get_config_from_fallback()} or {}

            # Load actual data from the database file path (e.g., ".aliens.db" / test directory)
            db_path = load_database_file(config_file_path, "src", init_data.get("data")) if config_file_path else None
            
            if not self._validate_db_structure(db_path):
                raise Exception(f"Incompatible data format for AlienDatabase: {db_path}")

        except FileNotFoundError as e:
            print(f"Warning: Could not find database file at '{config_file_path}'. Creating dummy one...")
            
            # Create a mock config structure based on the fallback import logic in original code
            self.data = {}
            if isinstance(init_data, dict):
                for key, value in init_data.items():
                    data_type = type(value).__name__
                    setattr(self.data[key], "_type", data_type)

        # Ensure we have a path to save (fallback mode or explicit directory)
        self._save_path = os.path.abspath(os.getcwd()) if not db_path else None
    
    def load(self, filename):
        """Load data from file."""
        filepath = get_database_file_for_load(filename, "src", {})

        try:
            with open(filepath, "r") as f:
                # Load JSON array of objects or nested structure
                raw_data = json.load(f)
                
                self.data = {}
                
                if isinstance(raw_data, list):
                    for item in raw_data:
                        key_list = item.get("keys", [])
                        value_list = item.get("values", [])

                        # If each object has nested data structures (e.g., {key1: {...}}), handle them iteratively or recursively
                        if isinstance(value_list, list):
                            for i in range(len(value_list)):
from typing import Dict, List, Any, Optional
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}
        
        # Store the initial configuration loaded in main.py (mock up)
        config_file_path = "src/config.json" if os.path.exists("config.json") else None
        
        try:
            with open(config_file_path, "r") as f:
                init_data = json.load(f)["database"] if isinstance(init_data, dict) else {k: v for k, v in get_config_from_fallback()} or {}

            # Load actual data from the database file path (e.g., ".aliens.db" / test directory)
            db_path = load_database_file(config_file_path, "src", init_data.get("data")) if config_file_path else None
            
            if not self._validate_db_structure(db_path):
                raise Exception(f"Incompatible data format for AlienDatabase: {db_path}")

        except FileNotFoundError as e:
            print(f"Warning: Could not find database file at '{config_file_path}'. Creating dummy one...")            
            # Create a mock config structure based on the fallback import logic in original code
            self.data = {}
            if isinstance(init_data, dict):
                for key, value in init_data.items():
                    data_type = type(value).__name__
                    setattr(self.data[key], "_type", data_type)

        # Ensure we have a path to save (fallback mode or explicit directory)
        self._save_path = os.path.abspath(os.getcwd()) if not db_path else None
    
    def load(self, filename):
        """Load data from file."""
        filepath = get_database_file_for_load(filename, "src", {})

        try:
            with open(filepath, "r") as f:
                # Load JSON array of objects or nested structure
                raw_data = json.load(f)
                
                self.data = {}
                
                if isinstance(raw_data, list):
                    for item in raw_data:
                        key_list = item.get("keys", [])
                        value_list = item.get("values", [])

                        # If each object has nested data structures (e.g., {key1: {...}}), handle them iteratively or recursively
                        if isinstance(value_list, list):
                            for i in range(len(value_list)):
                                self.data[key_list[i]] = {}
                                
                                inner_data = value
from typing import Dict, List, Any, Optional, Iterator
import json
import os

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
        # Store the initial configuration loaded in main.py (mock up)
        config_file_path = "src/config.json" if os.path.exists("config.json") else None
        
        try:
            with open(config_file_path, "r") as f:
                init_data = json.load(f)["database"] if isinstance(init_data, dict) else {k: v for k, v in get_config_from_fallback()} or {}

            # Load actual data from the database file path (e.g., ".aliens.db" / test directory)
            db_path = load_database_file(config_file_path, "src", init_data.get("data")) if config_file_path else None
            
            if not self._validate_db_structure(db_path):
                raise Exception(f"Incompatible data format for AlienDatabase: {db_path}")

        except FileNotFoundError as e:
            print(f"Warning: Could not find database file at '{config_file_path}'. Creating dummy one...")            
            # Create a mock config structure based on the fallback import logic in original code
            self.data = {}
            if isinstance(init_data, dict):
                for key, value in init_data.items():
                    data_type = type(value).__name__
                    setattr(self.data[key], "_type", data_type)

        # Ensure we have a path to save (fallback mode or explicit directory)
        self._save_path = os.path.abspath(os.getcwd()) if not db_path else None
    
    def load(self, filename):
        """Load data from file."""
        filepath = get_database_file_for_load(filename, "src", {})

        try:
            with open(filepath, "r") as f:
                # Load JSON array of objects or nested structure
                raw_data = json.load(f)
                
                self.data = {}
                
                if isinstance(raw_data, list):
                    for item in raw_data:
                        key_list = item.get("keys", [])
                        value_list = item.get("values", [])

                        # If each object has nested data structures (e.g., {key1: {...}}), handle them iteratively or recursively
                        if isinstance(value_list, list):
                            for i in range(len(value_list)):
                                self.data[key_list[i]] = {}
class AlienDatabase:
    def __init__(self):
        self.data = {}
        
        # Store the initial configuration loaded in main.py (mock up)
        config_file_path = "src/config.json" if os.path.exists("config.json") else None
        
        try:
            with open(config_file_path, "r") as f:
                init_data = json.load(f)["database"] if isinstance(init_data, dict) else {k: v for k, v in get_config_from_fallback()} or {}

            # Load actual data from the database file path (e.g., ".aliens.db" / test directory)
            db_path = load_database_file(config_file_path, "src", init_data.get("data")) if config_file_path else None
            
            if not self._validate_db_structure(db_path):
                raise Exception(f"Incompatible data format for AlienDatabase: {db_path}")

        except FileNotFoundError as e:
            print(f"Warning: Could not find database file at '{config_file_path}'. Creating dummy one...")            
            # Create a mock config structure based on the fallback import logic in original code
            self.data = {}
            if isinstance(init_data, dict):
                for key, value in init_data.items():
                    data_type = type(value).__name__
                    setattr(self.data[key], "_type", data_type)

        # Ensure we have a path to save (fallback mode or explicit directory)
        self._save_path = os.path.abspath(os.getcwd()) if not db_path else None
    
    def load(self, filename):
        """Load data from file."""
        filepath = get_database_file_for_load(filename, "src", {})

        try:
            with open(filepath, "r") as f:
                # Load JSON array of objects or nested structure
                raw_data = json.load(f)
                
                self.data = {}
                
                if isinstance(raw_data, list):
                    for item in raw_data:
                        key_list = item.get("keys", [])
                        value_list = item.get("values", [])

                        # If each object has nested data structures (e.g., {key1: {...}}), handle them iteratively or recursively
                        if isinstance(value_list, list):
                            for i in range(len(value_list)):
                                self.data[key_list[i]] = {}

    def save(self, filename):
        """Save current state to file."""
        filepath =
