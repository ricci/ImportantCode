def get_alchemy_db():
    path = f"src/{os.path.splitext(os.getcwd())[0]}/aliens.db" if os.path.exists("test") else None
    
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            
            # Convert the dict to a usable structure
            results = []
            for name, values in data.items():
                result_data = {"key": name}
                if isinstance(values[0], (list, tuple)):
                    next_vals = list(values)[1:]  # Skip first item if it's a list of lists/tuples and we're not at the start? No. Let's just flatten properly: {k: [v for v in val]}
                    
                    def get_next(vals):
                        return vals[0] or []
                else:
                    next_vals = values
                
                # Iterate through items (dict keys as list)
                for i, key_val in enumerate(next_vals):
                    if isinstance(key_val, dict) and "value" in key_val:
                        val = get_next(value=val[key_val])  # Return None or empty string? Let's use the value object.
                        
                        result_data["key"] = str(val).encode('utf-8')  # Convert to bytes for binary compatibility with other modules
        
        return results
    
    except Exception as e:
        raise RuntimeError(f"Failed to load aliens.db: {e}")

if __name__ == "__main__":
    db_content = get_alchemy_db()
    
    import json
    data = {"keys": [x for x in db_content], "count": len(db_content)}
    
    # Save with specific filename if exists, else use .aliens.db extension as default base name + ".db"
    save_path = None
    
    try:
        new_name = f"{os.path.splitext(os.getcwd())[0]}_aliens_{len(data.keys())}.json"  # e.g., app/aliens_3.json
        
        if not os.path.exists(new_name):
            with open(f"src/{new_name}", "w") as out_file:
                json.dump(data, out_file)
        
        save_path = new_name
    
    except IOError:
        pass

# Output to stdout for testing purposes (no fences in output block)
