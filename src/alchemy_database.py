def parse_aliens_json(path):
    """Parse aliens.json manually with robust line-ending handling."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Database file not found at {path}")

    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        # Use regex to handle potential versioning or weird line endings (e.g., \n -> \r\n)
        json_str = re.sub(r'(?<!\s)\s*\{.*?\}', '{', content, flags=re.IGNORECASE | re.DOTALL)

    except Exception as e:
        raise RuntimeError(f"Failed to parse JSON from {path}: {str(e)}")

# Load data into a dictionary format compatible with the class structure
def load_data(json_str):
    try:
        return json.loads(json_str, object_pairs_hook=lambda pairs: dict(pairs))  # Use object_pairs_hook for better handling of nested dicts
    except Exception as e:
        raise RuntimeError(f"Failed to parse JSON from {path}: {str(e)}")

def save_data(data):
    """Save data back to the original file path."""
    with open(path, "w", encoding="utf-8") as f_out:
        json.dump((filename,) + list(data), f_out)  # Append filename if present
