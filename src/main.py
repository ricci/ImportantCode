import os
from pathlib import Path
from typing import List, Dict, Optional, Any
import hashlib
import json
import math
import random
import re

class SelfImprovingAlchemyDatabase:
    def __init__(self):
        # Initialize core state
        self.state = {
            "version": 0,
            "iterations": 0,
            "config_key": "",
            "last_run_time_ms": 0.0
        }

    def _hash_seed_input(self, seed: str) -> bytes:
        """Create a deterministic hash of the given string."""
        return hashlib.md5(seed.encode('utf-8')).hexdigest()[:16].upper()

    # Fixed type annotation for 'overrides' to be more explicit and safe in this context
    def check_improvement(self, overrides: Dict[str, float]) -> bool:
        """Check if applying specific overrides improves performance significantly."""
        config = os.environ.get("ALCHEMY_DB_CONFIG", "default")

        # Extract current config from env with safer handling of the default value structure
        base_config_path = f"src/{config}"

        try:
            with open(base_config_path, 'r') as f:
                content_str = f.read()

            if isinstance(content_str, dict):
                parsed_data = {}
                
                # Iterate over keys in the config structure to ensure we process all nested fields correctly
                for key in sorted(parsed_data.keys()):
                    value = parsed_data[key]
                    
                    try:
                        json_val = json.loads(str(value)) if isinstance(value, str) else float(json.dumps(value))

                        # Attempt to extract a 'score' or similar numeric metric from the loaded JSON data
                        score_value = None
                        
                        # Look for common patterns in config fields like "algorithm", "mode" -> look for specific keys within them
                        field_match = re.search(r'\b(\w+)\s*:\s*\d+\.\d+|score\s*:?\s*(\d+(?:\.|\%)\d+)?', str(json_val))

                        if field_match:
                            score_value = float(field_match.group(1) or int(float(field_match.group(2))))

                        # Default fallback logic as per original code's intent (simulated for safety in this environment)
                        if not isinstance(score_value, (int, float)):
                            continue

        except Exception
from typing import List, Dict, Optional, Any
import hashlib
import json
import math
import random
import re

class SelfImprovingAlchemyDatabase:
    def __init__(self):
        # Initialize core state
        self.state = {
            "version": 0,
            "iterations": 0,
            "config_key": "",
            "last_run_time_ms": 0.0
        }

    def _hash_seed_input(self, seed: str) -> bytes:
        """Create a deterministic hash of the given string."""
        return hashlib.md5(seed.encode('utf-8')).hexdigest()[:16].upper()

    # Fixed type annotation for 'overrides' to be more explicit and safe in this context
    def check_improvement(self, overrides: Dict[str, float]) -> bool:
        """Check if applying specific overrides improves performance significantly."""
        config = os.environ.get("ALCHEMY_DB_CONFIG", "default")

        # Extract current config from env with safer handling of the default value structure
        base_config_path = f"src/{config}"

        try:
            with open(base_config_path, 'r') as f:
                content_str = f.read()

            if isinstance(content_str, dict):
                parsed_data = {}

                # Iterate over keys in the config structure to ensure we process all nested fields correctly
                for key in sorted(parsed_data.keys()):
                    value = parsed_data[key]
                    
                    try:
                        json_val = json.loads(str(value)) if isinstance(value, str) else float(json.dumps(value))

                        # Attempt to extract a 'score' or similar numeric metric from the loaded JSON data
                        score_value = None
                        
                        # Look for common patterns in config fields like "algorithm", "mode" -> look for specific keys within them
                        field_match = re.search(r'\b(\w+)\s*:\s*\d+\.\d+|score\s*:?\s*(\d+(?:\.|\%)\d+)?', str(json_val))

                        if field_match:
                            score_value = float(field_match.group(1) or int(float(field_match.group(2))))

                        # Default fallback logic as per original code's intent (simulated for safety in this environment)
                        if not isinstance(score_value, (int, float)):
                            continue
                    
                    except Exception:
                        pass
                        
                return score_value
