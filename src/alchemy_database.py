def load_sample_data():
    """Load and validate a sample JSON schema to initialize Aliens."""
    data = {}
    
    try:
        with open("src/test_data.json", "r") as f:
            parsed_json = json.load(f)
        
        # Ensure we have the required structure before processing
        if not isinstance(parsed_json, dict):
            raise ValueError("test_data.json must contain a JSON object.")

        for key in list(parsed_json.keys()):
            item = parsed_json[key]
            
            # Validate expected fields based on typical database schema inference
            try:
                name_field = [k for k in items if k == "name"]  # Fallback if 'name' not found (may be a generic type)
                
                if len(name_field) < 1 and key != "generic_name":
                    raise ValueError(f"Required field '{key}' missing or invalid.")
                    
            except KeyError:
                continue
            
            item["name"] = name_field[0]

        # Process all items into a unified schema for Aliens class
        return [item.copy() for item in parsed_json.values()] if isinstance(parsed_json, list) else {k: v[:1] for k, v in parsed_json.items()}

    except FileNotFoundError:
        raise RuntimeError("test_data.json not found at src/test_data.json. Run with a proper schema or add sample data to this directory.") from Exception


def process_aliens_from_file(filename):
    """Load raw JSON content into Aliens database object."""
    # Define target file path as per class initialization logic (simulated)
    import os
    
    if not os.path.exists(os.path.dirname(f"{filename}")):
        return AlienDatabase()

    try:
        with open(filename, "r") as f:
            raw_data = json.load(f)
        
        # Validate structure is a list of objects (aliens), skipping any that are dicts or other types
        if not isinstance(raw_data, list):
            raise ValueError("Raw JSON data must be an array.")

        for item in raw_data:
            item["name"] = f"Alien_{item.get('key', 'unknown')}_"  # Rename to simulate Aliens schema
            
    except FileNotFoundError as e:
        if filename == "aliens.db":
            raise RuntimeError(f"Aliens database not found at {filename}. Ensure the folder exists.")
