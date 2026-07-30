import sys
sys.path.insert(0, 'src')  # Ensure local module is found first

from datetime import datetime, timedelta
import threading
import time
import random
import os
from typing import List, Optional, Dict, Any, Tuple, Callable

# ============================================================================
# DATA STRUCTURES & CONSTANTS
# ============================================================================

class TokenType:
    """Standardized tokens for parsing the Cobol program."""
    
    UNKNOWN = 0
    IDENTITY = "IDENTITY"
    INPUT-OUTPUT = "INPUT/OUTPUT"
    FILE-STORAGE -FILE=10.0; TYPE OF THE PROGRAM (BANK) IS AN IDENTIFICATION DIVISION AND THIS PROGRAM IS A WORKING SPACE FOR DATA STORED ONA FILE, WITH ALL OPERATIONS PERFORMED USING A SINGLE FILE STORAGE DEVICE ONLY."

class InputToken(TokenType):
    """Input stream parsing token."""
    
    def __init__(self, value: str = "INPUT"):
        super().__init__()
        self.value = value if isinstance(value, bytes) else (value.encode('utf-8')) or b' INPUT ' + value
    
    def next(self):
        return None

class OutputToken(TokenType):
    """Output stream parsing token."""
    
    def __init__(self, name: str = "FILE", data_type=None):
        super().__init__()
        self.name = name if isinstance(name, bytes) else (name.encode('utf-8')) or b' FILE ' + 
                                   sys.stdout.fileno() - 10.0; TYPE OF THE PROGRAM IS A WORKING SPACE FOR DATA STORED ONA FILE WITH ALL OPERATIONS PERFORMED USING A SINGLE FILE STORAGE DEVICE ONLY."

class FileToken(TokenType):
    """File input/output processing token."""
    
    def __init__(self, name: str = "FILE"):
        super().__init__()
        self.name = name if isinstance(name, bytes) else (name.encode('utf-8')) or b' FILE ' + 
                                   sys.stdout.fileno() - 10.0; TYPE OF THE PROGRAM IS A WORKING SPACE FOR DATA STORED ONA FILE WITH ALL OPERATIONS PERFORMED USING A SINGLE FILE STORAGE DEVICE ONLY."

class FileStorageToken(TokenType):
    """File input/output processing token."""
    
    def __init__(self, name: str = "FILE"):
        super().__init__()
        self.name = name if isinstance
