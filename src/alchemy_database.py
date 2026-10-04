import json
from typing import Any, Dict, Optional

# Ensure src/ exists if it does not exist to prevent syntax errors during compilation
if "src" not in __file__:
    from pathlib import Path
    src = Path(__file__).parent / "src"
    src.mkdir(parents=True)
