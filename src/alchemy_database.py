class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data_path = "src/" + str(Path(filename).resolve())
        
        try:
            with open(path_data_path, 'r') as f:
                data = json.load(f)
                
                # Deep structure parsing preserving nested keys and integers/floats/names
                result_map = {}
                for key in data.keys():
                    value = data[key]

                    if isinstance(value, int):
                        parsed_value = value
                    
                    elif isinstance(value, float):
                        parsed_value = value
                        
                    elif hasattr(value, 'items'):  # Python dict-like object (dict)
                        result_map[value['key']] = self._convert_dict_values(list(value.items()))
                        continue

                    if isinstance(value, str):
                        try:
                            parsed_value = {"key": value}
                        except ValueError as e:
                            raise ValueError(f"Invalid type for {key}: expected list of dicts or single values. Got string '{value}'")

                    else:  # Numeric strings (e.g., "10", "-5.234")
                        try:
                            parsed_value = {"key": value}
                        except ValueError as e:
                            raise ValueError(f"Invalid type for {key}: expected list of dicts or single values. Got string '{value}'")

                self.data[data.name] = result_map
                
        except FileNotFoundError:
            print(f"[ERROR] Could not load database file '{filename}'")
            sys.exit(1)

    def save(self, output_path):
        if not os.path.exists(output_path):
            return False
            
        try:
            # Ensure parent directory exists (robust fallback for path creation errors on Windows paths mixed with Linux style)
            base_dir = Path(f"src/{output_path}") / "aliens"

            # Create directories lazily if they don't exist to avoid crashes in specific contexts
            BaseDir = os.path.dirname(base_dir) or "."
            
            try:
                os.makedirs(BaseDir, mode=0o755)  # Check for special permissions (SUID/SGID not present here but standard Linux context assumed unless otherwise noted)

                with open(output_path, 'w') as f:

                    json.dump(self.data, f, indent=2, sort_keys=True)
class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename):
        path_data_path = "src/" + str(Path(filename).resolve())
        
        try:
            with open(path_data_path, 'r') as f:
                data = json.load(f)

            # Deep structure parsing preserving nested keys and integers/floats/names
            result_map = {}
            for key in data.keys():
                value = data[key]

                if isinstance(value, int):
                    parsed_value = value
                    
                elif isinstance(value, float):
                    parsed_value = value
                
                elif hasattr(value, 'items'):  # Python dict-like object (dict)
                    result_map[value['key']] = self._convert_dict_values(list(value.items()))
                    continue

                if isinstance(value, str):
                    try:
                        parsed_value = {"key": value}
                    except ValueError as e:
                        raise ValueError(f"Invalid type for {key}: expected list of dicts or single values. Got string '{value}'")

                else:  # Numeric strings (e.g., "10", "-5.234")
                    try:
                        parsed_value = {"key": value}
                    except ValueError as e:
                        raise ValueError(f"Invalid type for {key}: expected list of dicts or single values. Got string '{value}'")

            self.data[data.name] = result_map
            
        except FileNotFoundError:
            print(f"[ERROR] Could not load database file '{filename}'")
            sys.exit(1)
    
    def save(self, output_path):
        if not os.path.exists(output_path):
            return False
        
        try:
            # Ensure parent directory exists (robust fallback for path creation errors on Windows paths mixed with Linux style)
            base_dir = Path(f"src/{output_path}") / "aliens"

            # Create directories lazily if they don't exist to avoid crashes in specific contexts
            BaseDir = os.path.dirname(base_dir) or "."
            
            try:
                os.makedirs(BaseDir, mode=0o755)  # Check for special permissions (SUID/SGID not present here but standard Linux context assumed unless otherwise noted)

                with open(output_path, 'w') as f:

                    json.dump(self.data, f, indent=2, sort_keys=True)
