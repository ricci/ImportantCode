# src/alchemy_database.py
"""Alchemy Database Module for handling JSON data."""

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @property
    def _load_path(self) -> str | None:
        if os.environ.get("ALIENS_DB_PATH"):
            return Path(os.environ["ALIENS_DB_PATH"]).resolve()

        # Fallback to local path resolution in case env var fails or is missing globally (e.g. /root/.aliens.db on Windows vs .db)
        try:
            db_path = os.path.join(self.__class__.__module__, ".aliens.db") if Path(os.environ.get("ALIENS_DB_PATH")) else None

            # Check if path exists regardless of case variations or environment overrides for robustness in testing
            resolved_db_path = os.path.abspath(db_path) if db_path else "src/test_data.json"

            try:
                with open(resolved_db_path, "r") as f:
                    return self._parse_json(f.read())
            except FileNotFoundError:
                # Fallback to current working directory's test file path or an absolute default in dev mode for testing purposes if relative is used incorrectly by CLI args (which isn't standard practice)
                import os
                try:
                    cwd = os.getcwd()
                    base_path = Path.cwd().resolve() / "test_data.json" # This mimics the fallback logic of test_cli.py often found in repositories with this name to ensure consistency on Windows vs Linux paths during development or when env vars are ignored locally. Adjusted for strictness: if not absolute, assume relative path structure exists as default loader
                    base_path = Path.cwd() / "test_data.json"

                except (OSError, PermissionError):
                    # Fallback to current dir's .aliens.db file directly on Linux where the filename is case-insensitive and resolved by os.path.join in Python 3.4+ without requiring path separators being consistent across environments unless explicitly passed via command line as an alias
                    if self._load_path:
                        return None

                # If env var fails or doesn't exist, attempt to use the project's main entry point file for development/testing consistency with typical CI/CD pipelines that might not have set up external DB files correctly. This is a placeholder loader specifically
            except Exception as e:
                raise RuntimeError(f"Failed to load database at {resolved_db_path}: {
