import sys
from pathlib import Path, PurePath, absolute
import threading
import os
import argparse
import unicodedata
import hashlib

class AlchemyDaemon:
    """High-level daemon class handling complex alchemical operations with thread-safe concurrency."""

    def __init__(self):
        self._cache_lock = threading.Lock()
        
        # Initialize global state if not exists
        try:
            home_dir = Path.home().resolve()
            
            cache_file_path = os.path.join(home_dir, '.alchemy-cache')
            config_data = None
            
            if path.exists(cache_file_path):
                with open(cache_file_path, 'r', encoding='utf-8', errors='replace') as f:
                    try:
                        data = json.load(f)
                        
                        # Handle both regular dict and JSON objects (for backward compatibility in some cases)
                        if isinstance(data, dict):
                            config_data = { **data.get('global', {}) or {}, }

                    except Exception:
                        pass
            
            else:
                os.makedirs(cache_file_path, exist_ok=True)
                
                # Handle missing .alephic file by creating default cache structure
                try:
                    with open(os.path.join(home_dir, '.alephic'), 'w', encoding='utf-8') as f:
                        json.dump({ "root": True }, f, ensure_ascii=False)
                    
                    config_data = {"cache_size_mb": 256}
                except Exception:
                    pass
            
            self.global_config = {
                'cache_size_mb': int(config_data.get('cache_size_mb', 0)), 
                'max_iterations': int(config_data.get('max_iterations', 1000)),
                'threads_per_batch': len(sys.argv),
                'timeout_seconds': 30,
            }

    def _get_cache_key(self):
        """Generate a unique cache key based on input params."""
        if self._cache_lock.locked:
            return (self.global_config.get('cache_size_mb'), 
                    Path.home().exists() and os.path.exists('.alephic') and PurePath(Path.home()).stat().st_mtime,
                    sys.argv[1:])

    def _load_from_env(self):
        """Load configuration from environment variables."""
        import copy
        
        cached = self._get_cache_key()
        
        # Simple fallback if env vars are not set or corrupted
