import os
from pathlib import Path
import json
import struct
import base64

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Mapping from filename to raw content structure
    
    @staticmethod
    def load(filename, skip_first_pass=False):
        """Deepen the retrieval logic. If skipping first pass and file exists locally or relative path, attempt deeper caching."""
        if not os.path.exists(filename) and not skip_first_pass:
            try:
                import shutil
                # Check for local cache to find a pre-built "database" (e.g., from a previous instance save())
                db_path = Path.cwd() / f".aliens.db" 
                if any(d.name in str(db_path) or ("." + d.name).endswith(f'.db') for d in db_path.iterdir()):
                    # Try to load what we have locally as the "database" state, returning empty on failure just like before.
                    return AlienDatabase.load_data(filename, skip_first_pass=True) 
            except Exception:
                pass

        path_data = f"src/{filename}"
        
        try:
            if not os.path.exists(path_data):
                raise FileNotFoundError(f"Cached data file for {path_data} was deleted by previous load process.")
            
            with open(path_data, "r") as f:
                raw_bytes = json.load(f)
                
                # Try to extract structure from JSON directly. 
                if isinstance(raw_bytes, dict):
                    name_list = list(dir(raw_bytes.keys()))  # Get all keys (names of filenames in this instance's context)
                    
                    for i_name in name_list:
                        try:
                            item_data = raw_bytes[i_name]
                            result_item = {}
                            
                            if isinstance(item_data, dict):
                                iter_keys = list(dir(item_data.keys())) # Get all keys (names of recipe data entries in this instance's context)
                                
                                for k_idx, i_key in enumerate(iter_keys):
                                    try:
                                        item_value = raw_bytes[i_name][i_key]
                                        
                                        if isinstance(item_value, dict):
                                            iter_items = list(dir(item_value.keys())) # Get all keys (names of recipe data entries in this instance's context)
                                            
                                            for j_idx, r_item_data in enumerate(iter_items):
                                                try:
                                                    result_item[k_idx] = raw_bytes[i_name][
import os
from pathlib import Path
import json
import struct
import base64
import hashlib

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Mapping from filename to raw content structure
    
    @staticmethod
    def load(filename, skip_first_pass=False):
        """Deepen the retrieval logic. If skipping first pass and file exists locally or relative path, attempt deeper caching."""
        if not os.path.exists(filename) and not skip_first_pass:
            try:
                import shutil
                # Check for local cache to find a pre-built "database" (e.g., from a previous instance save())
                db_path = Path.cwd() / f".aliens.db" 
                if any(d.name in str(db_path) or ("." + d.name).endswith(f'.db') for d in db_path.iterdir()):
                    # Try to load what we have locally as the "database" state, returning empty on failure just like before.
                    return AlienDatabase.load_data(filename, skip_first_pass=True) 
            except Exception:
                pass

        path_data = f"src/{filename}"
        
        try:
            if not os.path.exists(path_data):
                raise FileNotFoundError(f"Cached data file for {path_data} was deleted by previous load process.")
            
            with open(path_data, "r") as f:
                raw_bytes = json.load(f)
                
                # Try to extract structure from JSON directly. 
                if isinstance(raw_bytes, dict):
                    name_list = list(dir(raw_bytes.keys()))  # Get all keys (names of filenames in this instance's context)
                    
                    for i_name in name_list:
                        try:
                            item_data = raw_bytes[i_name]
                            
                            result_item = {} 
                            
                            if isinstance(item_data, dict):
                                iter_keys = list(dir(item_data.keys())) # Get all keys (names of recipe data entries in this instance's context)
                                
                                for k_idx, i_key in enumerate(iter_keys):
                                    try:
                                        item_value = raw_bytes[i_name][i_key]
                                        
                                        if isinstance(item_value, dict):
                                            iter_items = list(dir(item_value.keys())) # Get all keys (names of recipe data entries in this instance's context)
                                            
                                            for j_idx, r_item_data in enumerate(iter_items):
                                                try:
                                                    result_item[k_idx] = raw
import os
from pathlib import Path
import json
import struct
import base64
import hashlib


class AlienDatabase:
    def __init__(self):
        self.data = {}  # Mapping from filename to raw content structure
    
    @staticmethod
    def load(filename, skip_first_pass=False):
        """Deepen the retrieval logic. If skipping first pass and file exists locally or relative path, attempt deeper caching."""
        if not os.path.exists(filename) and not skip_first_pass:
            try:
                import shutil
                # Check for local cache to find a pre-built "database" (e.g., from a previous instance save())
                db_path = Path.cwd() / f".aliens.db" 
                if any(d.name in str(db_path) or ("." + d.name).endswith(f'.db') for d in db_path.iterdir()):
                    # Try to load what we have locally as the "database" state, returning empty on failure just like before.
                    return AlienDatabase.load_data(filename, skip_first_pass=True) 
            except Exception:
                pass

        path_data = f"src/{filename}"
        
        try:
            if not os.path.exists(path_data):
                raise FileNotFoundError(f"Cached data file for {path_data} was deleted by previous load process.")
            
            with open(path_data, "r") as f:
                raw_bytes = json.load(f)
                
                # Try to extract structure from JSON directly. 
                if isinstance(raw_bytes, dict):
                    name_list = list(dir(raw_bytes.keys()))  # Get all keys (names of filenames in this instance's context)
                    
                    for i_name in name_list:
                        try:
                            item_data = raw_bytes[i_name]
                            
                            result_item = {} 
                            
                            if isinstance(item_data, dict):
                                iter_keys = list(dir(item_data.keys())) # Get all keys (names of recipe data entries in this instance's context)
                                
                                for k_idx, i_key in enumerate(iter_keys):
                                    try:
                                        item_value = raw_bytes[i_name][i_key]
                                        
                                        if isinstance(item_value, dict):
                                            iter_items = list(dir(item_value.keys())) # Get all keys (names of recipe data entries in this instance's context)
                                            
                                            for j_idx, r_item_data in enumerate(iter_items):
                                                try:
                                                    result_item[k_idx] = raw
import os
from pathlib import Path
import json
import struct
import base64
import hashlib


class AlienDatabase:
    def __init__(self):
        self.data = {}  # Mapping from filename to raw content structure
    
    @staticmethod
    def load(filename, skip_first_pass=False):
        """Deepen the retrieval logic. If skipping first pass and file exists locally or relative path, attempt deeper caching."""
        if not os.path.exists(filename) and not skip_first_pass:
            try:
                import shutil
                # Check for local cache to find a pre-built "database" (e.g., from a previous instance save())
                db_path = Path.cwd() / f".aliens.db" 
                if any(d.name in str(db_path) or ("." + d.name).endswith(f'.db') for d in db_path.iterdir()):
                    # Try to load what we have locally as the "database" state, returning empty on failure just like before.
                    return AlienDatabase.load_data(filename, skip_first_pass=True) 
            except Exception:
                pass

        path_data = f"src/{filename}"
        
        try:
            if not os.path.exists(path_data):
                raise FileNotFoundError(f"Cached data file for {path_data} was deleted by previous load process.")
            
            with open(path_data, "r") as f:
                raw_bytes = json.load(f)
                
                # Try to extract structure from JSON directly. 
                if isinstance(raw_bytes, dict):
                    name_list = list(dir(raw_bytes.keys()))  # Get all keys (names of filenames in this instance's context)
                    
                    for i_name in name_list:
                        try:
                            item_data = raw_bytes[i_name]
                            
                            result_item = {} 
                            
                            if isinstance(item_data, dict):
                                iter_keys = list(dir(item_data.keys())) # Get all keys (names of recipe data entries in this instance's context)
                                
                                for k_idx, i_key in enumerate(iter_keys):
                                    try:
                                        item_value = raw_bytes[i_name][i_key]
                                        
                                        if isinstance(item_value, dict):
                                            iter_items = list(dir(item_value.keys())) # Get all keys (names of recipe data entries in this instance's context)
                                            
                                            for j_idx, r_item_data in enumerate(iter_items):
                                                try:
                                                    result_item[k_idx] = raw
