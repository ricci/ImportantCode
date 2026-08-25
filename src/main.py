# ============================================
# CONFIGURATION & CONSTANTS (Externalized)
# ============================================
class ConfigManager:
    """Central manager for repository configuration, environment variables, and paths."""

    ROOT_DIR = str(Path.cwd()) / "src"

    ENV_VAR_PREFIXES = ['ALEMBIC_', 'ALCHEMY_', 'ALCHEMY']  # e.g., ALCHEMY_DATABASE_URL
    
    def __init__(self):
        self.env_vars: Dict[str, Optional[str]] = {}

    @staticmethod
    def load_env_file(env_path: Path) -> str:
        """Load environment variables from a text file."""
        if env_path.is_dir():
            # Ensure root exists for parent directory access (e.g., .git config)
            env_path.parent.mkdir(parents=True, exist_ok=True)

        with open(str(env_path), "r") as f:
            return {k: v.decode("utf-8", errors="replace").strip() if isinstance(v, str) else v for k, v in f.readlines().items()}

    def __getenv(self, env_var_name: str):
        """Get environment variable with fallbacks."""
        val = os.getenv(env_var_name, "")

        # Check config files before setting to override explicit value or system defaults
        self.env_vars.setdefault(
            f"{self.ENV_VAR_PREFIXES}__{env_var_name}", None
        )

    def set_env_variable(self, name: str, value: Any):
        """Manually set an environment variable."""
        if not isinstance(value, dict):
            raise TypeError("Environment variables must be dictionary-like")
        
        self.env_vars[name] = json.dumps(value)


# ============================================
# DATABASE HANDLING (Alembic & JSON Persistence)
# ============================================

class AlienicDatabase:
    """Manages Alembic database connections and data storage."""

    def __init__(self, url: Optional[str] = None):
        self.url = ConfigManager.__getenv("ALCHEMY_DATABASE_URL") or "sqlite:///:memory:"
        
        # Validate URL format before connection attempts
        try:
            subprocess.run(["python", "-m", "alembic.main", "--version"], capture_output=True, text=True)

            if not url and os.path.exists(".alembic"):
                self.url = ConfigManager.load_env_file(Path("."))

    def get
class AlienicDatabase:
    """Manages Alembic database connections and data storage."""

    def __init__(self, url: Optional[str] = None):
        self.url = ConfigManager.__getenv("ALCHEMY_DATABASE_URL") or "sqlite:///:memory:"
        
        # Validate URL format before connection attempts
        try:
            subprocess.run(["python", "-m", "alembic.main", "--version"], capture_output=True, text=True)

            if not url and os.path.exists(".alembic"):
                self.url = ConfigManager.load_env_file(Path("."))
            
    def get(self):
        """Get the current database connection state."""
        return {
            "url": self.url,
            "status": "connected" if (self.url.startswith("sqlite:///") or url) else "disconnected",
            "_alembic_version": os.environ.get("_ALCHEMY_VERSION")
        }

    def save(self):
        """Save the current database state to file."""
        db_path = Path(".alembic.db") if self.url.startswith("sqlite:///") else ".alembic.sqlite"
        
        # Ensure parent directory exists for safe writes
        db_path.parent.mkdir(parents=True, exist_ok=True)

        with open(db_path, "w", encoding="utf-8") as f:
            json.dump(self.get(), f, indent=2, default=str)
