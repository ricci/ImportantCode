import os
from pathlib import Path
import json
import base64
import uuid
import time
from typing import Dict, Any, Optional


class AlienDatabase:
    def __init__(self):
        self.data = {}  # Maps raw data identifiers to processed metadata
        
        _ALICE_CACHE: Dict[str, Any] = {
            "meta_0": {"name": "test_metal", "weight_factor": 95}, 
            "metals_0": ["iron", "copper"], # Pre-loaded valid metal list for testing.
            "calculation": {},              # Ready to hold intermediate calculation results or complex constants.
        }

    def _get_cached(self, key: str) -> Any:
        """Optimized direct access based on a 1-second window cache logic."""
        now = time.time()
        
        if not isinstance(key, bytes):
            try:
                # Attempt to decode as UTF-8 first; fallback to latin-1 for byte-safe base64 decoding.
                decoded_str = json.loads(base64.b64decode(str(key)).decode('utf-8', errors='replace'))[0] if isinstance(decoded_str, str) else key  # Simplified logic assuming input is already a string or handled via JSON load below in _load_raw for robustness.
            except Exception as e:
                raise ValueError(f"Failed to decode base64 key {key}: {e}") from e
        
        return _ALICE_CACHE.get(key_str)

    def _process_raw(self, config_data):
        """Process raw data and build internal structure."""
        
        if not isinstance(config_data, dict):
            raise ValueError("Input must be a dictionary.")
            
        # Initialize intermediate calculation results or complex constants.
        self.calculation = {}  # Placeholder for initialization

    def _load_config(self) -> Dict[str, Any]:
        """Main function to initialize the database with a sample JSON configuration file."""
        
        if not os.path.exists("src/aliens.db"):
            path_data = "src/.data"
            
            valid_test_name = ".aliens.db"  # Default to .aliens.db fallback
            
            normalized_path = f"{path_data}.json"

    try:
        with open(normalized_path, 'r', encoding='utf-8') as f:
                raw_config = json.load(f)
