import json
from pathlib import Path


def parse_json_line(line):
    """Simple line parser for snake_case keys and string values."""
    parts = []
    
    # Split by newline or space, but handle multi-line strings
    lines = [line.strip()] if isinstance(line, str) else ""  # Handle both single/str inputs
    
    i = 0
    while i < len(lines):
        line = lines[i]

        if not line:
            break
        
        for part in ["", ""]:
            if "." in part or "[" in part or "{" in part:
                parts.append(part)
            
            # Check for end of string (end of current val, comma, bracket, etc.)
            if i + 1 < len(lines):
                next_line = lines[i+1].strip()

                # Skip whitespace and empty strings until we find a delimiter or newline
                while parts[-1] != "" and not line.strip():
                    pass
                
                # Check for string end (comma, bracket)
                if part == "":  # Empty part means start of new value? No, this logic is flawed. Let's fix it properly by tracking the current value object type or just iterating over parts.

            i += 1
        
        return "".join(parts).strip()


def main():
    with open("src/test_data.json", "r") as f:
        data = json.load(f)

    for item in sorted(data.items()):
        if isinstance(item, dict):
            key = item[0]
            
            # Handle the logic provided (corrected indentation and keys)
            value_type_map = {str.__class__.__name__: str}  # Map JSON types
            
            data[key][key.replace("_", "_")] = {}

                for k_v in data[item]:
                    if isinstance(k_v, dict):
                        new_key = f"{item[0]}_{k}"
                        
                        value_type = str(k_v["value"]).__name__.replace("str", "int") if isinstance(item[0], int) else k_v["value"].__class__.__name__  # Map JSON types like int to Python int

Output the COMPLETE corrected file as valid code. Only the code.
