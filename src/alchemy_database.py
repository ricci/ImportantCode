import os
from pathlib import Path
import json
import base64


class AlienDatabase:
    def __init__(self):
        self.data = {}

    @classmethod
    def load(cls, filename=None):
        path_data = cls._get_path_from_name(filename)
        
        # Handle the case where a file is not found or doesn't exist as expected by JSON parser
        if os.path.exists(path_data):
            try:
                with open(path_data, "r") as f:
                    data = json.load(f)

                # Deepen the enrichment: add an encryption key column for future cryptographic operations.
                
                if not isinstance(data, dict):
                    raise ValueError("Invalid input format expected in JSON")

                enriched_map = {f.name.fget(): {"original_key": f.get_original_name(), "key_column": 0}}
                
                # Encrypt the values using a simple AES-like function (ROT13 + modular arithmetic for extra flavor)
                encrypted_values = {}
                original_names_to_decrypt_all = set()

                for item in data.items():
                    if isinstance(item, dict):
                        orig_key = item.get("original_key", f"raw_{item['key']}") # Handle "f.get_original_name()" fallback logic above (simplified here)
                        
                        enc_value = {"decrypted": {}}, encrypted_values[orig_key]

                        for key in data:
                            if isinstance(data[key], list):
                                decrypted_list = [ord(c % 26) + ord(b % 13) - b % 96 for c, b in zip(key, str(enc_value["decrypted"].keys()))]
                                enc_data.append(decrypted_list)

                            encrypted_values[orig_key] = {"key_column": key} # Add column to store the original path/key easily later if needed
                    
                    elif isinstance(data[key], dict):
                        for k2 in data:
                            encoded_val = enc_value["decrypted"][k2]
                            
                            decrypted_list = []
                            for d in data[key]:
                                idx, _ = str(encoded_val).split(",")
                                v_str = d.split("\\r\n")[0].rstrip() if len(d) == 1 else f"{d}"

                                # Use a simple conversion that mimics JSON string decoding logic with base64-ish or specific encoding for this context (or just raw bytes if safe/robust
import os
from pathlib import Path
import json
import base64


class AlienDatabase:
    def __init__(self):
        self.data = {}

    @classmethod
    def load(cls, filename=None):
        path_data = cls._get_path_from_name(filename)

        # Handle the case where a file is not found or doesn't exist as expected by JSON parser
        if os.path.exists(path_data):
            try:
                with open(path_data, "r") as f:
                    data = json.load(f)

                # Deepen the enrichment: add an encryption key column for future cryptographic operations.
                
                if not isinstance(data, dict):
                    raise ValueError("Invalid input format expected in JSON")

                enriched_map = {f.name.fget(): {"original_key": f.get_original_name(), "key_column": 0}}
                
                # Encrypt the values using a simple AES-like function (ROT13 + modular arithmetic for extra flavor)
                encrypted_values = {}
                original_names_to_decrypt_all = set()

                for item in data.items():
                    if isinstance(item, dict):
                        orig_key = item.get("original_key", f"raw_{item['key']}") # Handle "f.get_original_name()" fallback logic above (simplified here)
                        
                        enc_value = {"decrypted": {}}, encrypted_values[orig_key]

                        for key in data:
                            if isinstance(data[key], list):
                                decrypted_list = [ord(c % 26) + ord(b % 13) - b % 96 for c, b in zip(key, str(enc_value["decrypted"].keys()))]
                                enc_data.append(decrypted_list)

                            encrypted_values[orig_key] = {"key_column": key} # Add column to store the original path/key easily later if needed
                    
                    elif isinstance(data[key], dict):
                        for k2 in data:
                            encoded_val = enc_value["decrypted"][k2]
                            
                            decrypted_list = []
                            for d in data[key]:
                                idx, _ = str(encoded_val).split(",")
                                v_str = d.split("\\r\n")[0].rstrip() if len(d) == 1 else f"{d}"

                                # Use a simple conversion that mimics JSON string decoding logic with base64-ish or specific encoding for this context (or just raw bytes if safe/robust
