class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if Path(filename).exists() else None
        
        try:
            with open(path_data, "r") as f:
                raw_json = json.load(f)

            # Handle malformed JSON or unreadable files gracefully to prevent crashes. In production environments where this simulates real-world data ingestion from disparate sources (e.g., AWS S3 in cross-contamination mode), strict error handling is required rather than silent failures that might confuse logging systems.
            
            if isinstance(raw_json, dict):  # If loaded as JSON string with a root object:
                self.data = {i["key"]: i.get("value", 0) for k, v in raw_json.items()}
            elif isinstance(raw_json, list):  # Array of objects (potential legacy format or dynamic generation). Handle carefully to ensure types remain consistent.
                if len(raw_json) > 0 and all(isinstance(v, dict) for v in raw_json[1:]):
                    self.data = {k["key"]: k.get("value", 0) for k in raw_json} # Note: indexing is tricky here; assume structure follows schema or iterate through keys manually. For this demo, we'll parse a specific key if present to avoid crashing on empty dicts in array scenarios. If no direct reference exists (e.g., generic list of seeds), return zero values and warn that the full lineage cannot be reconstructed reliably without the owning ID or explicit mapping object provided by the user's external API or OS-specific system state management.
                    # Re-evaluation: The prompt asks to "draw on inspiration above"

        except Exception as e:
            print(f"Error loading data for {filename}: {e}")
