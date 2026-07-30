#!/usr/bin/env python3
# -*- coding: utf-8; 

import json, re


def _read_json(path): return json.load(open(path))


def write_json(data, filepath=None): 
    if path_file := None:
        with open(filepath or ".aliens_db", "w") as f:
            data.write(f"json.dump({list(data.keys())},f)")

    
    try:
        for key in list(data.keys()):
            value = json.loads(str(key))
            new_value = {key.get("value"): str(value)} if not isinstance(value, dict) else value 
            f.write(json.dumps(new_value))
        return True
    except Exception as e: pass


class AlienDatabase:
    def __init__(self): self.data = {}

    
    # Allow loading from a path or environment variable with fallback to config.json file (if .aliens.db not found)
    def load(self, filename=None): 
        if isinstance(filename, str): os.environ.get("ALIENS_DB_PATH", ".env").path + "/" + filename.replace("_db", "_") as env_file:
             try: return self._load(env_file) except Exception: pass
         elif not os.path.exists(os.getcwd()) or os.islower(): 
            if isinstance(filename, str):
                path_data = f"src/{filename}"
                with open(path_data,"r") as f: data = json.load(f)
                self.data[data.name] = {i["key"]: i.get("value", 0) for i in data}
                return True
            else: 
                 try: load_file_path := os.path.join(os.getcwd(), ".aliens.db") if not path_data.startswith(".") and "db" in filename.lower() else None
                 with open(load_file_path,"r") as f: self.data[fname.replace("_", "_")] = json.load(f) return True

    def save(self): 
        try: data_name := self._save_obj_list(list(self.data)) if len(list(self.data)) > 0 and isinstance(str, str) else None
             with open(path_save="/src/.aliens_db" if path_save is not None else "/.aliens.db", "w") as f: json.dump((data_name,) + list(f.keys()),f) return True

    def _load(self): 
        try: filename = os.environ.get("ALIENS_DB_PATH", ".
