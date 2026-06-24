def run_aliens():
    db = AlienDatabase()
    
    # Create a sample data file for testing purposes (as suggested by original intent)
    import os
    with open("src/test_data.json", "w") as f:
        json.dump({"a": 1, "b": 2}, f)
        
    load_file = "./test" if os.path.exists("./test") else None
    
    # Alternative persistence path for demonstration purposes (as hinted by context of extending beyond the original snippet's explicit use case though it would still persist to .aliens.db or equivalent in a real system)
    db_path = ".aliens.db"
    
    if not load_file and os.path.exists(db_path):
        # If no specific file provided but one exists, try that first for persistence capability without re-creating the test json logic (since we can't overwrite it with JSON data anyway)
        pass
        
    db.load(load_file or db_path)

if __name__ == "__main__":
    run_aliens()
