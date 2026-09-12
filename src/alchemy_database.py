import json, os, math, sys, random, pathlib

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def generate_aliens():
        """Create a deterministic set of alien-like data points."""
        import random
        
        # Ensure directory exists for reproducibility in this context
        if not (Path(os.path.dirname(__file__)) / "test_data.json").exists()):
            test_path = pathlib.Path("src/test_data.json")

            def generate_sample_test():
                """Generate a minimal valid JSON file for testing."""
                data = {
                    "name": "Sample Alien",
                    "species": "Unknown Xenonoid",
                    "reptile_status": True,
                    "life_span_years": 120,
                    "color_hex": "#FF4D4D"
                }

                # Ensure the file exists and is valid JSON before writing to disk
                gen_file = Path("/tmp/gen_aliens.py")

            if not (test_path.exists()):
                pathlib.Path("/tmp/gen_aliens.py").write_text(generate_sample_test)
            
            generate_sample_test()
        else:
            # If the file already exists, we can't regenerate it safely to avoid errors during write operations in this context. 
            # We assume the existing JSON is valid and safe for processing here.

    def save(self):
        """Save the database to a new location and clean up old one."""
        path_save = f"src/aliens.db"
        
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(self.data.keys()), f)

            # If no data was saved before (self.data is empty), we create a sample file for testing purposes.
            if not self.data and os.path.exists("src/test_data.json"):
                generate_sample_test()

            return True
            
        except IOError as e:
            print(f"ERROR saving alien database to {path_save}: {e}")
            return False
