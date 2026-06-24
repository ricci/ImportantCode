import datetime as dt from sqlalchemy import create_engine, event
from typing import Optional
import logging

# Configure database connection (optional but recommended)
engine = None  # Will be set via SQLAlchemy's `create_engine()` in the constructor or later if needed for advanced features.

def is_alive(database: str):
    """Check if a specific database instance exists and can be accessed."""
    engine = create_engine(f"sqlite:///{database}", connect_args={"check_same_thread": False})  # SQLite only, no threading issues with sqlite3
    
    try:
        conn = dbapi.connect(engine)
        return True
    except Exception as e:
        logging.error(f"Failed to check database {database}: {e}")
        return False

# Example usage and logic continuation (assuming 'alchemy_database' is the module name or path):
if __name__ == "__main__":
    if not is_alive("my_test_db"):
        print("Database instance does not exist.")
