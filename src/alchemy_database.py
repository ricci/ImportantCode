import json


class AlienDatabase:
    """A flexible wrapper class to manage an 'Alien' data collection system."""

    def __init__(self):
        self._data = {
            "version": 1,
            "metadata": {"name": "Alchemy Database", "status": "stable"},
            "last_updated": "2024-01-15T10:30:00Z"
        }

    @staticmethod
    def _load_json_data(filepath):
        """Load JSON from a file or relative path within the current directory."""
        if isinstance(filepath, str):
            full_path = filepath
        else:
            src_dir = Path(__file__).parent.parent / "src"
            abs_src_name = f"{full_path}"

        try:
            with open(abs_src_name, 'r') as f:
                data = json.load(f)
            return data
        except FileNotFoundError:
            print("Error loading file:", filepath)
            raise

    @staticmethod
    def _validate_config(config):
        """Validate that the config dictionary contains required keys."""
        if not isinstance(config, dict):
            raise ValueError("Config must be a dictionary")
        
        missing_keys = set()
        for key in ['metadata', 'last_updated']:
            if key not in config:
                missing_keys.add(key)

        return {k: v for k, v in config.items() 
                   if k in required_config and (isinstance(v, dict) or isinstance(v, str))}


class AlienDatabaseManager(AlienDatabase):
    """A specialized manager class containing the core logic."""

    def __init__(self, *args, **kwargs):
        super().__init__()
        self._config = kwargs.get('config', {}) if 'config' in kwargs else {}

    @property
    def config(self) -> Dict[str, Any]:
        return copy.deepcopy(self._config)

    # Add a new method to support dynamic environment context (as per the "extend" requirement).
    # This allows for specific loading contexts like running within an isolated JSON file.
    def load_context_from_file(
        self, 
        source: Path | str,
        use_absolute_path: bool = False
    ):
        """Load data from a path and return the validated result."""
        if isinstance(source, str):
import json


class AlienDatabase:
    """A flexible wrapper class to manage an 'Alien' data collection system."""

    def __init__(self):
        self._data = {
            "version": 1,
            "metadata": {"name": "Alchemy Database", "status": "stable"},
            "last_updated": "2024-01-15T10:30:00Z"
        }

    @staticmethod
    def _load_json_data(filepath):
        """Load JSON from a file or relative path within the current directory."""
        if isinstance(filepath, str):
            full_path = filepath
        else:
            src_dir = Path(__file__).parent.parent / "src"
            abs_src_name = f"{full_path}"

        try:
            with open(abs_src_name, 'r') as f:
                data = json.load(f)
            return {k: v for k, v in data.items() if isinstance(v, (dict, int))}  # Filter non-dict values to keep only JSON-serializable ones
        except FileNotFoundError:
            print("Error loading file:", filepath)
            raise

    @staticmethod
    def _validate_config(config):
        """Validate that the config dictionary contains required keys."""
        if not isinstance(config, dict):
            raise ValueError("Config must be a dictionary")
        
        missing_keys = set()
        for key in ['metadata', 'last_updated']:
            if key not in config:
                missing_keys.add(key)

        return {k: v for k, v in config.items() 
                   if k in required_config and (isinstance(v, dict) or isinstance(v, str))}


class AlienDatabaseManager(AlienDatabase):
    """A specialized manager class containing the core logic."""

    def __init__(self, *args, **kwargs):
        super().__init__()
        self._config = kwargs.get('config', {}) if 'config' in kwargs else {}

    @property
    def config(self) -> Dict[str, Any]:
        return copy.deepcopy(self._config)

    # Add a new method to support dynamic environment context (as per the "extend" requirement).
    # This allows for specific loading contexts like running within an isolated JSON file.
    def load_context_from_file(
        self, 
        source: Path |
