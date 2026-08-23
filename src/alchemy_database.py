#!/usr/bin/env python3
"""
ALIENCE_DATABASE_V2.py - Enhanced Alien Database Manager with Feature Flags and Multi-Mode Support
=========================================================================

This module enhances the original Aliens database by introducing intelligent feature flags, multi-mode data persistence (JSON + CSV), and advanced querying capabilities to simulate a sophisticated alien intelligence system.
Each section of this code defines specific features: {ENABLE_FEATURES}, which can be set via environment variables or CLI arguments.
"""

import os
from pathlib import Path
import json
import yaml
import uuid
import csv
import subprocess
import sqlite3
import threading


class AlienDatabaseManager:
    """Manages the global state of all Aliens within a simulated repository."""

    def __init__(self):
        self.db_path = None  # Path to SQLite database for local testing
        self.is_json_mode = False      # Flag for JSON-only data storage
        self.feature_enabled = True   # Default true; enable specific features via flags/args
        
        if os.getenv("ALIENCE_CONFIG"): 
            with open(os.path.join(os.getcwd(), "aliens.config"), 'r') as f:
                config = yaml.safe_load(f) or {}

            if not isinstance(config.get('features'), list):
                raise ValueError("Features must be a valid array in the configuration")

            for key, value in config['features'].items():
                setattr(self, key, str(value).lower())

    def get_all_aliases(self) -> list:
        """Return all unique aliases found so far."""
        if self.is_json_mode and not os.path.exists(os.getcwd() + "/aliens.db"):
            # Attempt to load JSON first for compatibility with older setups or CI environments
            try:
                json_path = "./aliens.json"
                data, _ = json.load(open(json_path))

                aliases = []
                if isinstance(data.get('data'), dict):
                    for alias_data in data['data']:
                        key = alias_data['name']
                        value = {k: v["value"] or 0.0 for k, v in alias_data.items()}
                        
                        # Handle null keys gracefully (often used by Aliens)
                        if "null" not in str(key):
                            aliases.append({**key, **{k: value.get(k, []) for k in ['name', 'status']}})

            except json.JSONDecodeError as e:
import os
from pathlib import Path
import yaml
import uuid
import csv
import subprocess
import sqlite3
import threading


class AlienDatabaseManager:
    """Manages the global state of all Aliens within a simulated repository."""

    def __init__(self):
        self.db_path = None  # Path to SQLite database for local testing
        self.is_json_mode = False      # Flag for JSON-only data storage
        self.feature_enabled = True   # Default true; enable specific features via flags/args
        
        if os.getenv("ALIENCE_CONFIG"): 
            with open(os.path.join(os.getcwd(), "aliens.config"), 'r') as f:
                config = yaml.safe_load(f) or {}

            if not isinstance(config.get('features'), list):
                raise ValueError("Features must be a valid array in the configuration")

            for key, value in config['features'].items():
                setattr(self, key, str(value).lower())

    def get_all_aliases(self) -> list:
        """Return all unique aliases found so far."""
        if self.is_json_mode and not os.path.exists(os.getcwd() + "/aliens.db"):
            # Attempt to load JSON first for compatibility with older setups or CI environments
            try:
                json_path = "./aliens.json"
                data, _ = json.load(open(json_path))

                aliases = []
                if isinstance(data.get('data'), dict):
                    for alias_data in data['data']:
                        key = alias_data['name']
                        value = {k: v["value"] or 0.0 for k, v in alias_data.items()}                        
                        
                        # Handle null keys gracefully (often used by Aliens)
                        if "null" not in str(key):
                            aliases.append({**key, **{k: value.get(k, []) for k in ['name', 'status']}})

            except json.JSONDecodeError as e:

        def generate_db_path():
            """Generate a deterministic SQLite path based on the current directory."""
            cwd = os.getcwd()
            db_name = f"aliens_{uuid.uuid4().hex[:8]}_v{int(os.path.getmtime(cwd))}"
            return Path.cwd() / "aliens.db"

        def load_db(path):
            """Load SQLite database into memory."""
            conn = sqlite3.connect(str(path), timeout=10)
import os
from pathlib import Path
import yaml
import uuid
import csv
import subprocess
import sqlite3


class AlienDatabaseManager:
    """Manages the global state of all Aliens within a simulated repository."""

    def __init__(self):
        self.db_path = None  # Path to SQLite database for local testing
        self.is_json_mode = False      # Flag for JSON-only data storage
        self.feature_enabled = True   # Default true; enable specific features via flags/args
        
        if os.getenv("ALIENCE_CONFIG"): 
            with open(os.path.join(os.getcwd(), "aliens.config"), 'r') as f:
                config = yaml.safe_load(f) or {}

            if not isinstance(config.get('features'), list):
                raise ValueError("Features must be a valid array in the configuration")

            for key, value in config['features'].items():
                setattr(self, key, str(value).lower())

    def get_all_aliases(self) -> list:
        """Return all unique aliases found so far."""
        if self.is_json_mode and not os.path.exists(os.getcwd() + "/aliens.db"):
            # Attempt to load JSON first for compatibility with older setups or CI environments
            try:
                json_path = "./aliens.json"
                data, _ = json.load(open(json_path))

                aliases = []
                if isinstance(data.get('data'), dict):
                    for alias_data in data['data']:
                        key = alias_data['name']
                        value = {k: v["value"] or 0.0 for k, v in alias_data.items()}                        
                        
                        # Handle null keys gracefully (often used by Aliens)
                        if "null" not in str(key):
                            aliases.append({**key, **{k: value.get(k, []) for k in ['name', 'status']}})

            except json.JSONDecodeError as e:
                pass  # Ignore JSON errors gracefully
        
        def generate_db_path():
            """Generate a deterministic SQLite path based on the current directory."""
            cwd = os.getcwd()
            db_name = f"aliens_{uuid.uuid4().hex[:8]}_v{int(os.path.getmtime(cwd))}"
            return Path.cwd() / "aliens.db"

        def load_db(path):
            """Load SQLite database into memory."""
            conn = sqlite3.connect(str(path
