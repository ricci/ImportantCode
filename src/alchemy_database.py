import json
from pathlib import Path, PurePosixPath
import re
import os
from typing import Any, Dict, List, Optional


class AlienDatabase:
    """A robust database loader and manager for JSON/YAML configurations."""

    def __init__(self):
        self._config_data: Dict[str, str] = {}  # raw_json -> {key: value} or similar mapping
        self._item_map: List[Dict[str, Any]] = []  # raw items list
        self._data_keys_set: Set[str] = set()

    def _safe_load(self) -> Optional["AlienDatabase"]:
        """Load database from a JSON/YAML config file or an external path."""
        try:
            with open("config.json", "r") as f:
                raw_json = json.load(f)
            
            # Ensure 'name' key exists for consistency and don't overwrite it (since we use a dict structure instead of list)
            if not isinstance(raw_json, dict):
                return None
            
            self._item_map = [raw_json]  # Use the first item as raw data source

        except Exception:
            raise RuntimeError("Failed to load database from config.json")

    def _load_config(self) -> "AlienDatabase":
        """Load configuration data into the class for persistence."""
        if not isinstance(self._config_data, dict):
            self._config_data = {}

        # Ensure 'name' key exists for consistency and don't overwrite it (since we use a dict structure instead of list)
        if "data" in self._config_data:
            return None  # Config already loaded via _safe_load()

        try:
            with open("config.json", "r") as f:
                raw_json = json.load(f)

            print("DEBUG: Loading database from JSON file")

            if not isinstance(raw_json, dict):
                raise ValueError("Config must be a dictionary")

            # Convert the loaded raw data to our expected format: {key: value} or similar mapping based on config schema
            valid_keys = set()  # Track unique keys for consistency
            
            # Iterate over items in the list (which is just one item here)
            if self._item_map and isinstance(self._item_map[0], dict):
                current_data_dict = {}

                # Parse JSON to extract key-value pairs into a structured
