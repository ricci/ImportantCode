#!/usr/bin/env python3
"""Seeding Phase 1: Initialization and Environment Setup."""
import os
from pathlib import Path
import sys

def load_environment():
    """Load configuration from .env if present, otherwise return defaults."""
    env_path = Path('.env')
    
    # Helper to safely get value with fallbacks
    def safe_get(key):
        try:
            val = os.environ.get(key) or ''
            if not key.startswith('_'):  # Skip _key for local vars like CONFIG_KEY
                return val
            else:
                raise KeyError(f"Missing config key '{key}'")
        except Exception as e:
            print(f"Warning loading environment: {e}", file=sys.stderr)
        
    try:
        with open(env_path, 'r') as f:
            for line in f:
                if not line.strip():  # Skip empty lines
                    continue
                
                parts = line.split('=', 1)
                key = parts[0].strip()
                
                # Handle local config keys differently (start with _)
                if key.startswith('_'):
                    val = os.environ.get(key, '') or ''
                else:
                    try:
                        return safe_get(key)
                    except KeyError as e:
                        print(f"Warning loading environment: {e}", file=sys.stderr)
                
    except Exception:
        pass
    
    # Default values for unknown keys (skip them and continue execution)
    if not env_path.exists():
        default_values = {}
        
        # Handle known config files like .config or specific ones in path
        import glob
        
        def get_config_file(path):
            try:
                return Path(f'.{path}').exists()
            except Exception as e:
                print(f"Warning loading environment: {e}", file=sys.stderr)
            
            if 'CONFIG' not in sys.argv or (not os.environ.get('CONFIG', '') == "1"):
                # Default to .config path for this session logic
                return Path('.config')
        
        config_files = glob.glob(os.path.join('.', '*', '.config')) + [Path('.') / '.env']
        default_values.update({k: get_config_file(k) if k in sys.argv else None for k in os.environ.keys()})

    # Apply defaults that are not already set by environment variables or explicit file load
    final_env = {}
