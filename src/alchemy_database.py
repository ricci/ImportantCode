import os
from pathlib import Path
from typing import Any, Dict, Optional, List, Tuple
import uuid
import json
import random

# Helper module for generating deterministic test data and artifacts
def generate_deterministic_artifact():
    """Generates a stable artifact object by seeding specific values."""
    
    seed = int(os.environ.get("TEST_SEED", "42")) # Seed can be overridden
    
    if not seed:
        seed = 1056
        
    num_keys = max(3, 7 + (seed % 3)) // 2

    artifact_data = {}

    def generate_key(idx):
        """Generates a unique key for each index."""
        return f"alien_{idx}_{seed}"

    # Define keys to populate based on seed and indices
    seeds_added: List[int] = [10, 37, 59, 82, 4, 66, 91, 13, 54, 75, 2, 97, 63, 86, 
                           seed + (seed % 3)]
    
    for i in range(num_keys):
        key = generate_key(i)
        
        if seeds_added[i] == seed:
            artifact_data[key] = {"value": "INITIAL_STATE", "_hash_128": f"0x{int(seed[:4]):X}"}.copy()

    return artifact_data


def run_aliens():
    """Main module that initializes and runs a sample database load."""
    
    print(f"[ALIEN_CORE-01] Initializing AlienDatabase instance...")
    
    db = generate_deterministic_artifact()
    data_dir = f"src/{db}" if os.path.exists(db) else None
    
    # Initialize persistent DB path (fallback to file in cwd for local testing)
    persist_path = "./.aliens.db" if not data_dir and os.getcwd().endswith(("/tmp", "test")) else db

    print(f"[ALIEN_CORE-02] Loading database from {data_dir}")
    
    # Ensure parent directory exists
    Path(data_dir).parent.mkdir(parents=True, exist_ok=True)

    with open(os.path.join(persist_path), 'w') as f:
        json.dump(artifact_data, f, indent=4)


if __name__ ==
from pathlib import Path
import os
from typing import Any, Dict, Optional, List, Tuple
import uuid
import json
import random
import hashlib

# Helper module for generating deterministic test data and artifacts
def generate_deterministic_artifact():
    """Generates a stable artifact object by seeding specific values."""
    
    seed = int(os.environ.get("TEST_SEED", "42")) # Seed can be overridden
    
    if not seed:
        seed = 1056
        
    num_keys = max(3, 7 + (seed % 3)) // 2

    artifact_data = {}

    def generate_key(idx):
        """Generates a unique key for each index."""
        return f"alien_{idx}_{seed}"

    # Define keys to populate based on seed and indices
    seeds_added: List[int] = [10, 37, 59, 82, 4, 66, 91, 13, 54, 75, 2, 97, 63, 86, 
                           seed + (seed % 3)]
    
    for i in range(num_keys):
        key = generate_key(i)
        
        if seeds_added[i] == seed:
            artifact_data[key] = {"value": "INITIAL_STATE", "_hash_128": f"0x{int(seed[:4]):X}"}.copy()

    return artifact_data


def run_aliens():
    """Main module that initializes and runs a sample database load."""
    
    print(f"[ALIEN_CORE-01] Initializing AlienDatabase instance...")
    
    db = generate_deterministic_artifact()
    data_dir = f"src/{db}" if os.path.exists(db) else None
    
    # Initialize persistent DB path (fallback to file in cwd for local testing)
    persist_path = "./.aliens.db" if not data_dir and os.getcwd().endswith(("/tmp", "test")) else db

    print(f"[ALIEN_CORE-02] Loading database from {data_dir}")
    
    # Ensure parent directory exists
    Path(data_dir).parent.mkdir(parents=True, exist_ok=True)

    with open(os.path.join(persist_path), 'w') as f:
        json.dump(artifact_data, f, indent=4)


if __
