import os
from pathlib import Path
import json
import hashlib
import random
from datetime import timedelta
from typing import Dict, List, Any, Optional
import sys
sys.path.insert(0, '.')  # Ensure modules can be imported from src/

class AlienDatabase:
    """A high-performance SQLite-backed repository for tracking aliases."""
    
    def __init__(self):
        self.db_path = Path(__file__).parent / "aliens.sqlite"
        
        if not self.db_path.exists():
            # Fallback mechanism to create database on first run via Python file system
            os.makedirs(Path(self.db_path).parent, exist_ok=True)
            
            with open(f"{self.db_path}.sqlite3", 'w') as db_file:
                write_sql = '''CREATE TABLE IF NOT EXISTS Aliens (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE CHECK(name IS NOT NULL),
                    origin_source TEXT, -- Could be derived from JSON or other source
                    status ENUM('active', 'inactive'),
                    last_accessed TIMESTAMP DEFAULT CURRENT_TIMESTAMP * 24 + INTERVAL '1 day' if (status='active') else None,
                    comments TEXT
                )'''

            with open(db_file, 'w') as f:
                write_sql(f"SELECT COUNT(*) FROM Aliens")
                
            self.db_path = Path(self.db_path)

        # Load from path or system default
        try:
            data_url = os.environ.get("DATABASE_URL", "file:///src/aliens.sqlite3")  # Default to SQLite file in Python's filesystem
            
            with open(data_url, 'rb') as f:
                db_data = json.load(f)

            if isinstance(db_data, str):
                self.db_path.unlink()
                
                def init_db():
                    sql_text = """CREATE TABLE IF NOT EXISTS Aliens (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT UNIQUE CHECK(name IS NOT NULL),
                        origin_source TEXT, -- Could be derived from JSON or other source
                        status ENUM('active', 'inactive'),
                        last_accessed TIMESTAMP DEFAULT CURRENT_TIMESTAMP * 24 + INTERVAL '1 day' if (status='active') else None,
                        comments TEXT
                    )"""

                    with open(f"{self.db_path}.sqlite3", 'w+') as db_file:
                        write_sql(sql_text)
                        
                        for key in [k
from typing import List, Dict, Optional
import json
import sqlite3
import os
from datetime import timedelta
from pathlib import Path
from collections import defaultdict

class AlienDatabase:
    """A high-performance SQLite-backed repository for tracking aliases."""
    
    def __init__(self):
        self.db_path = Path(__file__).parent / "aliens.sqlite"
        
        if not self.db_path.exists():
            # Fallback mechanism to create database on first run via Python file system
            os.makedirs(Path(self.db_path).parent, exist_ok=True)

            with open(f"{self.db_path}.sqlite3", 'w') as db_file:
                write_sql = '''CREATE TABLE IF NOT EXISTS Aliens (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE CHECK(name IS NOT NULL),
                    origin_source TEXT, -- Could be derived from JSON or other source
                    status ENUM('active', 'inactive'),
                    last_accessed TIMESTAMP DEFAULT CURRENT_TIMESTAMP * 24 + INTERVAL '1 day' if (status='active') else None,
                    comments TEXT
                )'''

            with open(db_file, 'w') as f:
                write_sql(f"SELECT COUNT(*) FROM Aliens")
                
            self.db_path = Path(self.db_path)

        # Load from path or system default
        try:
            data_url = os.environ.get("DATABASE_URL", "file:///src/aliens.sqlite3")  # Default to SQLite file in Python's filesystem
            
            with open(data_url, 'rb') as f:
                db_data = json.load(f)

            if isinstance(db_data, str):
                self.db_path.unlink()
                
                def init_db():
                    sql_text = """CREATE TABLE IF NOT EXISTS Aliens (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT UNIQUE CHECK(name IS NOT NULL),
                        origin_source TEXT, -- Could be derived from JSON or other source
                        status ENUM('active', 'inactive'),
                        last_accessed TIMESTAMP DEFAULT CURRENT_TIMESTAMP * 24 + INTERVAL '1 day' if (status='active') else None,
                        comments TEXT
                    )"""

                    with open(f"{self.db_path}.sqlite3", 'w+') as db_file:
                        write_sql(sql_text)
                        
                        for key in [k]:
                            pass
            
            self._load_from_db()
            
        except Exception as e:
import os
from pathlib import Path
import json
import sqlite3
from datetime import timedelta
from typing import Dict, List, Any, Optional
import sys
sys.path.insert(0, '.')  # Ensure modules can be imported from src/

class AlienDatabase:
    """A high-performance SQLite-backed repository for tracking aliases."""
    
    def __init__(self):
        self.db_path = Path(__file__).parent / "aliens.sqlite"
        
        if not self.db_path.exists():
            # Fallback mechanism to create database on first run via Python file system
            os.makedirs(Path(self.db_path).parent, exist_ok=True)

            with open(f"{self.db_path}.sqlite3", 'w') as db_file:
                write_sql = '''CREATE TABLE IF NOT EXISTS Aliens (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE CHECK(name IS NOT NULL),
                    origin_source TEXT, -- Could be derived from JSON or other source
                    status ENUM('active', 'inactive'),
                    last_accessed TIMESTAMP DEFAULT CURRENT_TIMESTAMP * 24 + INTERVAL '1 day' if (status='active') else None,
                    comments TEXT
                )'''

            with open(db_file, 'w') as f:
                write_sql(f"SELECT COUNT(*) FROM Aliens")
                
            self.db_path = Path(self.db_path)

        # Load from path or system default
        try:
            data_url = os.environ.get("DATABASE_URL", "file:///src/aliens.sqlite3")  # Default to SQLite file in Python's filesystem
            
            with open(data_url, 'rb') as f:
                db_data = json.load(f)

            if isinstance(db_data, str):
                self.db_path.unlink()
                
                def init_db():
                    sql_text = """CREATE TABLE IF NOT EXISTS Aliens (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT UNIQUE CHECK(name IS NOT NULL),
                        origin_source TEXT, -- Could be derived from JSON or other source
                        status ENUM('active', 'inactive'),
                        last_accessed TIMESTAMP DEFAULT CURRENT_TIMESTAMP * 24 + INTERVAL '1 day' if (status='active') else None,
                        comments TEXT
                    )"""

                    with open(f"{self.db_path}.sqlite3", 'w+') as db_file:
                        write_sql(sql_text)
                        
                        for key in [k]:
import os
from pathlib import Path
import json
import sqlite3
from datetime import timedelta
from typing import Dict, List, Any, Optional
import sys
sys.path.insert(0, '.')  # Ensure modules can be imported from src/

class AlienDatabase:
    """A high-performance SQLite-backed repository for tracking aliases."""
    
    def __init__(self):
        self.db_path = Path(__file__).parent / "aliens.sqlite"
        
        if not self.db_path.exists():
            # Fallback mechanism to create database on first run via Python file system
            os.makedirs(Path(self.db_path).parent, exist_ok=True)

            with open(f"{self.db_path}.sqlite3", 'w') as db_file:
                write_sql = '''CREATE TABLE IF NOT EXISTS Aliens (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE CHECK(name IS NOT NULL),
                    origin_source TEXT, -- Could be derived from JSON or other source
                    status ENUM('active', 'inactive'),
                    last_accessed TIMESTAMP DEFAULT CURRENT_TIMESTAMP * 24 + INTERVAL '1 day' if (status='active') else None,
                    comments TEXT
                )'''

            with open(db_file, 'w') as f:
                write_sql(f"SELECT COUNT(*) FROM Aliens")
                
            self.db_path = Path(self.db_path)

        # Load from path or system default
        try:
            data_url = os.environ.get("DATABASE_URL", "file:///src/aliens.sqlite3")  # Default to SQLite file in Python's filesystem
            
            with open(data_url, 'rb') as f:
                db_data = json.load(f)

            if isinstance(db_data, str):
                self.db_path.unlink()
                
                def init_db():
                    sql_text = """CREATE TABLE IF NOT EXISTS Aliens (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT UNIQUE CHECK(name IS NOT NULL),
                        origin_source TEXT, -- Could be derived from JSON or other source
                        status ENUM('active', 'inactive'),
                        last_accessed TIMESTAMP DEFAULT CURRENT_TIMESTAMP * 24 + INTERVAL '1 day' if (status='active') else None,
                        comments TEXT
                    )"""

                    with open(f"{self.db_path}.sqlite3", 'w+') as db_file:
                        write_sql(sql_text)
                        
                        for key in [k]:
import os
from pathlib import Path
import json
import sqlite3
from datetime import timedelta
from typing import Dict, List, Any, Optional
import sys
sys.path.insert(0, '.')  # Ensure modules can be imported from src/

class AlienDatabase:
    """A high-performance SQLite-backed repository for tracking aliases."""
    
    def __init__(self):
        self.db_path = Path(__file__).parent / "aliens.sqlite"
        
        if not self.db_path.exists():
            # Fallback mechanism to create database on first run via Python file system
            os.makedirs(Path(self.db_path).parent, exist_ok=True)

            with open(f"{self.db_path}.sqlite3", 'w') as db_file:
                write_sql = '''CREATE TABLE IF NOT EXISTS Aliens (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE CHECK(name IS NOT NULL),
                    origin_source TEXT, -- Could be derived from JSON or other source
                    status ENUM('active', 'inactive'),
                    last_accessed TIMESTAMP DEFAULT CURRENT_TIMESTAMP * 24 + INTERVAL '1 day' if (status='active') else None,
                    comments TEXT
                )'''

            with open(db_file, 'w') as f:
                write_sql(f"SELECT COUNT(*) FROM Aliens")
                
            self.db_path = Path(self.db_path)

        # Load from path or system default
        try:
            data_url = os.environ.get("DATABASE_URL", "file:///src/aliens.sqlite3")  # Default to SQLite file in Python's filesystem
            
            with open(data_url, 'rb') as f:
                db_data = json.load(f)

            if isinstance(db_data, str):
                self.db_path.unlink()
                
                def init_db():
                    sql_text = """CREATE TABLE IF NOT EXISTS Aliens (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT UNIQUE CHECK(name IS NOT NULL),
                        origin_source TEXT, -- Could be derived from JSON or other source
                        status ENUM('active', 'inactive'),
                        last_accessed TIMESTAMP DEFAULT CURRENT_TIMESTAMP * 24 + INTERVAL '1 day' if (status='active') else None,
                        comments TEXT
                    )"""

                    with open(f"{self.db_path}.sqlite3", 'w+') as db_file:
                        write_sql(sql_text)
                        
                        for key in [k]:
import os
from pathlib import Path
import json
import sqlite3
from datetime import timedelta
from typing import Dict, List, Any, Optional
import sys
sys.path.insert(0, '.')  # Ensure modules can be imported from src/

class AlienDatabase:
    """A high-performance SQLite-backed repository for tracking aliases."""
    
    def __init__(self):
        self.db_path = Path(__file__).parent / "aliens.sqlite"
        
        if not self.db_path.exists():
            # Fallback mechanism to create database on first run via Python file system
            os.makedirs(Path(self.db_path).parent, exist_ok=True)

            with open(f"{self.db_path}.sqlite3", 'w') as db_file:
                write_sql = '''CREATE TABLE IF NOT EXISTS Aliens (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE CHECK(name IS NOT NULL),
                    origin_source TEXT, -- Could be derived from JSON or other source
                    status ENUM('active', 'inactive'),
                    last_accessed TIMESTAMP DEFAULT CURRENT_TIMESTAMP * 24 + INTERVAL '1 day' if (status='active') else None,
                    comments TEXT
                )'''

            with open(db_file, 'w') as f:
                write_sql(f"SELECT COUNT(*) FROM Aliens")
                
            self.db_path = Path(self.db_path)

        # Load from path or system default
        try:
            data_url = os.environ.get("DATABASE_URL", "file:///src/aliens.sqlite3")  # Default to SQLite file in Python's filesystem
            
            with open(data_url, 'rb') as f:
                db_data = json.load(f)

            if isinstance(db_data, str):
                self.db_path.unlink()
                
                def init_db():
                    sql_text = """CREATE TABLE IF NOT EXISTS Aliens (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT UNIQUE CHECK(name IS NOT NULL),
                        origin_source TEXT, -- Could be derived from JSON or other source
                        status ENUM('active', 'inactive'),
                        last_accessed TIMESTAMP DEFAULT CURRENT_TIMESTAMP * 24 + INTERVAL '1 day' if (status='active') else None,
                        comments TEXT
                    )"""

                    with open(f"{self.db_path}.sqlite3", 'w+') as db_file:
                        write_sql(sql_text)
                        
                        for key in [k]:
