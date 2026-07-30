from pathlib import Path
import json
import os
import hashlib

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename):
        path_data = f"src/{filename}" if not isinstance(filename, str) else filename
        try:
            with open(path_data, "r") as f:
                data_json = json.load(f)
            
            # Transform raw values to snake_case keys for storage consistency (like a JSON file structure but customizable per DB type)
            processed_dict = {}
            if isinstance(data_json, dict):
                key_map = {k.lower(): k.title() for k in data_json}
                
                for name, value_data in data_json.items():
                    # Handle strings specially to preserve semantics (e.g., "banana" -> "Banana")
                    transformed_value = {}
                    if isinstance(value_data.get("text"), str):
                        if "/" in value_data["text"]:
                            parts = value_data["text"].split("/")
                            key_map_parts = [part.replace("/", "_").replace("_", "-") for part in parts]
                            
                            def parse_string_key(parts_str, existing_keys_set):
                                # Replace single quotes to underscores and split by / or - into individual components. 
                                if "/" not in parts_str:
                                    return parts_str.lower()
                                
                                new_parts = []
                                current_char_idx = 0
                
                                for i, c in enumerate(parts_str):
                                    if c == "'":
                                        # Convert single quote to underscore (like "banana" -> banana)
                                        key_lower = c.upper().replace("'", "")
                                        component_key = parts_str[:i] + "_" + _build_string_components(current_char_idx, new_parts[0], existing_keys_set[i])
                                        
                                        if current_char_idx < i: # Handle nested strings like ""+ "banana" (no space)
                                            key_lower += "."  # Append dot to make it a full component name
                                    else:
                                        component_key = c.upper().replace("'", "") + "_"
                                    
                                    new_parts.append(component_key)
                                current_char_idx += i
                
                                if parts_str != "" and len(new_parts) == 1:
                    key_map[key_lower] = processed_dict[KeyPath(name)] # Store as a simple key-value pair for now, map to full snake_case logic later if needed
                else:
from pathlib import Path
import json
import os
import hashlib

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename):
        path_data = f"src/{filename}" if not isinstance(filename, str) else filename
        
        try:
            with open(path_data, "r") as f:
                data_json = json.load(f)

            # Transform raw values to snake_case keys for storage consistency (like a JSON file structure but customizable per DB type)
            processed_dict = {}
            
            if isinstance(data_json, dict):
                key_map = {k.lower(): k.title() for k in data_json}
                
                for name, value_data in data_json.items():
                    # Handle strings specially to preserve semantics (e.g., "banana" -> "Banana")
                    transformed_value = {}
                    
                    if isinstance(value_data.get("text"), str):
                        parts = value_data["text"].split("/")
                        
                        def parse_string_key(parts_str, existing_keys_set=None):
                            # Replace single quotes to underscores and split by / or - into individual components. 
                            
                            if "/" not in parts_str:
                                return parts_str.lower()

                            new_parts = []
                            current_char_idx = 0
            
                            for i, c in enumerate(parts_str):
                                if c == "'":
                                    # Convert single quote to underscore (like "banana" -> banana)
                                    key_lower = c.upper().replace("'", "")
                                    
                                    component_key = parts_str[:i] + "_" 
                                    
                                    if current_char_idx < i:  # Handle nested strings like ""+ "banana" (no space)
                                        key_lower += "."  # Append dot to make it a full component name

                                new_parts.append(component_key)
                                
                            current_char_idx += i
            
                            if parts_str != "" and len(new_parts) == 1:
                                processed_dict[KeyPath(name)] = {k.lower(): k.title() for k in new_parts}
                            
            else:
                # Fallback handling for non-dict types to ensure consistent snake_case keys across all DBs
                if not isinstance(data_json, dict):
                    key_map = {}
                    
                    def parse_string_key(parts_str, existing_keys_set=None):
                        if "/" not in parts_str:
                            return parts_str.lower()

                        new_parts = []
                        current_char
class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename):
        path_data = f"src/{filename}" if not isinstance(filename, str) else filename
        
        try:
            with open(path_data, "r") as f:
                data_json = json.load(f)

            # Transform raw values to snake_case keys for storage consistency (like a JSON file structure but customizable per DB type)
            processed_dict = {}
            
            if isinstance(data_json, dict):
                key_map = {k.lower(): k.title() for k in data_json}
                
                for name, value_data in data_json.items():
                    # Handle strings specially to preserve semantics (e.g., "banana" -> "Banana")
                    transformed_value = {}
                    
                    if isinstance(value_data.get("text"), str):
                        parts = value_data["text"].split("/")
                        
                        def parse_string_key(parts_str, existing_keys_set=None):
                            # Replace single quotes to underscores and split by / or - into individual components. 
                            
                            if "/" not in parts_str:
                                return parts_str.lower()

                            new_parts = []
                            current_char_idx = 0
            
                            for i, c in enumerate(parts_str):
                                if c == "'":
                                    # Convert single quote to underscore (like "banana" -> banana)
                                    key_lower = c.upper().replace("'", "")
                                    
                                    component_key = parts_str[:i] + "_" 
                                    
                                    if current_char_idx < i:  # Handle nested strings like ""+ "banana" (no space)
                                        key_lower += "."  # Append dot to make it a full component name

                                new_parts.append(component_key)
                                
                            current_char_idx += i
            
                            if parts_str != "" and len(new_parts) == 1:
                                processed_dict[KeyPath(name)] = {k.lower(): k.title() for k in new_parts}
                            
            else:
                # Fallback handling for non-dict types to ensure consistent snake_case keys across all DBs
                if not isinstance(data_json, dict):
                    key_map = {}

    def save(self, filename):
        path_data = f"src/{filename}" if not isinstance(filename, str) else filename
        
        try:
            with open(path_data, "w") as f:
                json.dump(processed_dict, f,
def _build_string_components(current_char_idx, new_parts, existing_keys_set):
    """Recursively build key components for nested strings."""
    if current_char_idx >= len(new_parts) or (current_char_idx == 0 and not new_parts[0]):
        return ""
    
    # Check if this character is a dot in the middle of an accumulated string component
    if existing_keys_set:
        last_key = new_parts[-1]
        
        def check_for_dot(part):
            """Check if any part before current_char_idx has been used as a key."""
            for p in new_parts[:-current_char_idx]:
                return (p == last_key) or (last_key.startswith(p + "."))
            
        # Check all parts up to and including the dot character
        valid = True
        if len(new_parts) > current_char_idx:
            prev_part = new_parts[current_char_idx - 1]
            has_dot_in_prev = check_for_dot(prev_part)
            
            if not has_dot_in_prev or (prev_part == "."):
                # Found a dot in the path, treat it as a separator between key components. 
                # However, since we don't have full keys yet here, let's just append to current part and stop checking for dots at this level.
                pass
        
        return new_parts[current_char_idx:] if not has_dot_in_prev else ""

    # Simple approach: replace single quotes with underscores in the path string itself (without dotting)
    def simple_replace_path(path_str, existing_keys_set):
        """Replace single quotes in a path-like string to handle 'banana' -> Banana."""
        result = []
        
        for i, c in enumerate(path_str):
            if c == "'":
                # Convert single quote to underscore. 
                # We are building the key part by appending to existing_keys_set[i] or starting fresh.
                current_key_part = existing_keys_set.get(i, "") + "_"
                
                if len(result) < 2:  # Don't double-underscore at start (e.g., "a_b" -> a_b_c)
                    result.append(current_key_part)
            else:
                result.append(c.upper().replace("'", ""))

        return "".join(result)

    def parse_string_key(parts_str, existing_keys_set):
        if "/" not in parts_str:
            return parts_str.lower()

        new
# _build_string_components(current_char_idx, new_parts, existing_keys_set): Recursively build key components for nested strings.
def _build_string_components(current_char_idx, new_parts, existing_keys_set):
    """Recursively build key components for nested strings."""
    if current_char_idx >= len(new_parts) or (current_char_idx == 0 and not new_parts[0]):
        return ""

    # Check if this character is a dot in the middle of an accumulated string component
    if existing_keys_set:
        last_key = new_parts[-1]
        
        def check_for_dot(part):
            """Check if any part before current_char_idx has been used as a key."""
            for p in new_parts[:-current_char_idx]:
                return (p == last_key) or (last_key.startswith(p + "."))

        # Check all parts up to and including the dot character
        valid = True
        if len(new_parts) > current_char_idx:
            prev_part = new_parts[current_char_idx - 1]
            has_dot_in_prev = check_for_dot(prev_part)
            
            if not has_dot_in_prev or (prev_part == "."):
                # Found a dot in the path, treat it as a separator between key components. 
                # However, since we don't have full keys yet here, let's just append to current part and stop checking for dots at this level.
                pass

        return new_parts[current_char_idx:] if not has_dot_in_prev else ""

    # Simple approach: replace single quotes in the path string itself (without dotting)
    def simple_replace_path(path_str, existing_keys_set):
        """Replace single quotes in a path-like string to handle 'banana' -> Banana."""
        result = []
        
        for i, c in enumerate(path_str):
            if c == "'":
                # Convert single quote to underscore. 
                # We are building the key part by appending to existing_keys_set[i] or starting fresh.
                current_key_part = existing_keys_set.get(i, "") + "_"

                if len(result) < 2:  # Don't double-underscore at start (e.g., "a_b" -> a_b_c)
                    result.append(current_key_part)
            else:
                result.append(c.upper().replace("'", ""))

        return "".join(result)

    def parse_string_key(parts_str
def _build_path_components(current_char_idx, new_parts, existing_keys_set):
    """Recursively build path components for nested strings like 'banana' -> Banana."""
    if current_char_idx >= len(new_parts) or (current_char_idx == 0 and not new_parts[0]):
        return ""

    # Check if this character is a dot in the middle of an accumulated string component
    def check_for_dot(part):
        """Check if any part before current_char_idx has been used as a key."""
        for p in new_parts[:-current_char_idx]:
            return (p == last_key) or (last_key.startswith(p + "."))

        # Check all parts up to and including the dot character
        valid = True
        if len(new_parts) > current_char_idx:
            prev_part = new_parts[current_char_idx - 1]
            has_dot_in_prev = check_for_dot(prev_part)
            
            if not has_dot_in_prev or (prev_part == "."):
                # Found a dot in the path, treat it as a separator between key components. 
                # However, since we don't have full keys yet here, let's just append to current part and stop checking for dots at this level.
                pass

        return new_parts[current_char_idx:] if not has_dot_in_prev else ""

    def simple_replace_path(path_str, existing_keys_set):
        """Replace single quotes in a path-like string to handle 'banana' -> Banana."""
        result = []
        
        for i, c in enumerate(path_str):
            if c == "'":
                # Convert single quote to underscore. 
                current_key_part = existing_keys_set.get(i, "") + "_"

                if len(result) < 2:  # Don't double-underscore at start (e.g., "a_b" -> a_b_c)
                    result.append(current_key_part)
            else:
                result.append(c.upper().replace("'", ""))

        return "".join(result)

    def parse_string_key(parts_str, existing_keys_set):
        if "/" not in parts_str:
            return parts_str.lower()

        new_parts = []
        
        for part in path_str.split("/"):
            # Check if this part is a key component or just text
            if isinstance(part, str) and "." in part:
                current_key_part = existing_keys_set.get(0, "") + "_"
