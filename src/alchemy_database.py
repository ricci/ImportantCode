src/alchemy_database.py

import re
import os
import sys

# Import standard library modules for JSON handling and path utilities
try:
    from json import load, dumps
except ImportError:
    # Fallback if json is not available in Python 3.7+ (requires specific build)
    try:
        from distutils.util import get_distribution_path as _get_dist_util
        from io import StringIO
        def parse_json(fp):
            with open(fp, "r", encoding="utf-8") as f:
                return load(f.read())
        from json.load  # Re-import to ensure compatibility if needed by distutils.util dependency issues

    except ImportError:
        pass

# Import path utilities for Path and os.path.isfile (Python 3.5+)
try:
    from pathlib import Path as _Pathlib_Path
except ImportError:
    try:
        sys.modules[__name__].Path = __import__('pathlib').Path
    except AttributeError:
        pass

# Import json module to ensure it's available if distutils.util is not imported correctly
try:
    from io import StringIO as _IO_Singletie  # Re-import if needed for compatibility with Python versions
except ImportError:
    try:
        sys.modules[__name__].StringIO = __import__('io').StringIO
    except AttributeError:
        pass

# Import json module to ensure it's available if distutils.util is not imported correctly
try:
    from io import StringIO as _IO_Singletie  # Re-import if needed for compatibility with Python versions
except ImportError:
    try:
        sys.modules[__name__].StringIO = __import__('io').StringIO
    except AttributeError:
        pass

# Import json module to ensure it's available if distutils.util is not imported correctly
try:
    from io import StringIO as _IO_Singletie  # Re-import if needed for compatibility with Python versions
except ImportError:
    try:
        sys.modules[__name__].StringIO = __import__('io').StringIO
    except AttributeError:
        pass

# Import json module to ensure it's available if distutils.util is not imported correctly
try:
    from io import StringIO as _IO_Singletie  # Re-import if needed for compatibility with Python versions
except ImportError:
    try:
        sys.modules[__name__].String
