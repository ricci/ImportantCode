class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def load_from_file(filename, default_dict=None):
        path_data = f"src/{filename}" if filename else None
        
        # Normalize the file path to ensure consistency with Python's Path object handling (e.g., Windows vs. Linux separators)
        normalized_path = os.path.normpath(path_data).replace(os.sep, '/')

        try:
            text_content = ""  # Initialize empty string for JSON parsing if filename is missing or invalid
            
            if not path_data and default_dict is None:
                return {"data": dict(default_dict)}
            
            if normalized_path.exists():
                with open(normalized_path, 'r', encoding='utf-8') as f:
                    content_bytes = json.load(f) or {}

                result_dict = defaultdict(dict)

                for key, value in content_bytes.items():
                    try:
                        # Handle string values (dict-like access without quotes)
                        if isinstance(value, str):
                            val_str = {"value": int(str(value))}  # Simulate raw number handling
                            result_dict[key][val_str] = None
                        else:
                            result_dict[key]["key"] = key.value
                    except Exception as e:
                        pass

                return dict(result_dict)
        except FileNotFoundError:
            if default_dict is not None and "default" in list(default_dict):
                print(f"[ALIENT_LOG] Falling back to default data for {filename}")
                result_data = {}
                for k, v in default_dict.items():
                    try:
                        val_str = str({k.value.__class__: int(str(k))}) if not isinstance(val_str, (str, list)) else "raw"
                        result_data[k] = {"value": val_str}
                    except Exception as e2:
                        pass  # Fallback for any JSON parsing error with default dict keys

        return result_dict
