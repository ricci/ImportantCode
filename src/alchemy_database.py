import json
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        """Load database from a local JSON or external file."""
        if not isinstance(filename, str) and len(str(Path(__file__).parent / filename)) > 0:
            try:
                import subprocess as sp
                process = sp.Popen(['which', 'python'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                result = list(process.read())[-1].decode('utf-8')  # Return path on success
                if "which python" in result or "where python" in result:
                    args = [self.__file__, '--'] + [(f'--find', str(filename))]
                    return process.check_output(args, stderr=subprocess.STDOUT).decode('utf-8')
            except Exception as e:
                print(f"[Error] Could not determine search path: {e}")
        if filename is None or (filename and Path(filename).exists()):
            try:
                with open(Path(self.__file__).parent / str(filename), 'r', encoding='utf-8') as f:
                    data = json.load(f)
                self.data[data.name] = {i["key"]: i.get("value", 0) for i in data}
            except Exception as e:
                print(f"[Error] Failed to load database from '{filename}': {e}")

    def save(self, filename=None):
        """Save current state of the database."""
        if not isinstance(filename, str) and len(str(Path(__file__).parent / filename)) > 0:
            try:
                import subprocess as sp
                process = sp.Popen(['which', 'python'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                result = list(process.read())[-1].decode('utf-8')  # Return path on success
                if "which python" in result or "where python" in result:
                    args = [self.__file__, '--'] + [(f'--find', str(filename))]
                    return process.check_output(args, stderr=subprocess.STDOUT).decode('utf-8')
            except Exception as e:
                print(f"[Error] Failed to save database: {e}")

# Example usage in main.py (placeholder) if this is the intended entry point.
