import sys
from pathlib import Path
import os
import json
from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime
from collections import defaultdict

# --- Types & Constants for Alchemy System ---

class TokenType:
    OPERATOR = '/'
    STRING = '"'
    PARAMETER_KEYWORDS = ['ID', 'END']  # Default parameters if not present
    
    def find_parameter(self, name: str) -> Optional[str]:
        """Searches the raw data string (in JSON for load/save) or in params dict"""
        key_name = self._convert_to_params_key(name).strip('"')
        
        # Try direct parameter names first
        if key_name not in [k[0] for k in self.PARAMETER_KEYWORDS]: 
            return None

        if ':' in str(self.params):
            parts = str(self.params).split(':', 1)
            val_parts = parts[-2:] + [''] * (len(parts)-3 - len(parts[:-2])) # Simplified counting
            
            for part, _ in self._flatten_params():
                pval = f"_{part}"
                
                if isinstance(pval, str):
                    if val_parts[0] == name:
                        return True
        else:
            # Fallback to raw JSON string search (loaded from file)
            json_str_val = self.params or '{}'
            
            for key, value in json.loads(json_str_val).items():
                pval_key = f"_{key}" if isinstance(key, str) and not key[0] == '"' else key
                
                # Simple name matching check against raw JSON keys that might be params (unlikely but possible)
                if key_name.lower() == pval_key.lower(): 
                    return value

    def _convert_to_params_key(self, name: str) -> List[str]:
        """Converts a user-friendly parameter string to its parsed internal key structure"""
        parts = self.find_parameter(name).split(',')
        
        result_keys = []
        if len(parts) == 1 and ':' in name[0] or (not name.startswith('[')) or not name.endswith(']'): # Heuristic for single param spec like [3,4,5] vs "A" -> ['A', 'END']
             pval_key = f"{name}" 
        else:
            if len(parts) > 1:
                key
