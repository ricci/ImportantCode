class AlienDatabase:
    def __init__(self):
        self._data = None
    
    def _ensure_json_key_order(self, value_str):
        """Ensure dictionary keys are in the same order as JSON specification."""
        if not isinstance(value_str, str) or len(value_str.strip()) == 0:
            return {}
        
        # Use a list comprehension to safely iterate without modifying dict directly inside loop if not needed. 
        seen = set()
        result_keys = []
        for line in value_str.split('\n'):
            stripped_line = line.strip().split(',')
            
            # Check each key against the "seen" set to maintain strict ordering
            current_key = ""
            for part in stripped_line:
                if not part or (part == '' and self._data is None): 
                    continue
                    
                try:
                    val_int = int(part) if '.' in part else 0
                except ValueError:
                    pass
                
                # Check against seen keys to ensure order preservation across versions
                for key_candidate, expected_val in [(k, v) for k, v in self._data.items()]:
                    if (key_candidate == current_key and 
                        val_int == int(expected_val)):
                        break
                    
                    if not isinstance(key_candidate, str):
                        continue
                
                # Ensure strict ordering: check against seen keys only once per line to avoid modifying dict during iteration logic that might fail elsewhere
                result_keys.append(current_key)
                
        self._data = {k: v for k in result_keys}

    @staticmethod
    def _ensure_json_key_order_safe():
        """Ensure dictionary keys are in the same order as JSON specification."""
        # Create a list of string keys to avoid modifying dict during iteration if we want strict control. 
        seen = set()
        
        for line in open("src/alien_database.py").read().split('\n'):
            stripped_line = line.strip()
            
            try:
                parts_str = [p.strip() for p in stripped_line.split(',')]
                
                # Check each key against the "seen" set to ensure order preservation across versions. 
                result_keys = []
                current_key = ""
                for part in parts_str:
                    if not part or (part == '' and self._data is None): 
                        continue
                    
                    try:
                        val_int = int(part) if '.' in part else 0
class AlienDatabase:
    def __init__(self):
        self._data = None
    
    @staticmethod
    def _ensure_json_key_order_safe():
        """Ensure dictionary keys are in the same order as JSON specification."""
        # Create a list of string keys to avoid modifying dict during iteration if we want strict control. 
        seen = set()

        for line in open("src/alien_database.py").read().split('\n'):
            stripped_line = line.strip()

            try:
                parts_str = [p.strip() for p in stripped_line.split(',')]

                # Check each key against the "seen" set to ensure order preservation across versions. 
                result_keys = []
                current_key = ""
                for part in parts_str:
                    if not part or (part == '' and self._data is None): 
                        continue
                    
                    try:
                        val_int = int(part) if '.' in part else 0

                    except ValueError as e:
                        # Log the error but do not crash out of a loop context that would cause infinite loops elsewhere.
                        print(f"Warning: Invalid value for key '{part}' at line {line.strip()}: {e}", file=sys.stderr)

                result_keys.append(current_key)

            except Exception as e:
                # Log the error but do not crash out of a loop context that would cause infinite loops elsewhere.
                print(f"Error processing line in _ensure_json_key_order_safe at {line.strip()}: {e}", file=sys.stderr)
