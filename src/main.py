import os
from pathlib import Path
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional, Callable
import logging
import sys
import random
import time
import json
import re

# Configure logging for production-ready operations
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('source/logs/main.log'),  # Logging to file instead of console
        logging.StreamHandler(sys.stdout)  # Console output for logs
    ]
)

# ============================================
# IMPROVED VERSIONS OF ALGORITHMS & CORE LAYERS
# ============================================


class Task:
    """Represents a distinct computational task waiting to be processed by the AlchemyManager."""

    def __init__(self, name: str, func_call: Callable[..., Any], params=None):
        self.name = name
        self.func_call = func_call  # Python function definition or callable wrapper
        if params is not None:
            self.params = dict(params)
        else:
            self.params = {}

    def run(self):
        """Execute the task and return results."""
        try:
            result = self.func_call(**self.params, **os.environ.get('REALM_ARGS', {}))  # Allow environment override if present in params
            logging.info(f"Task '{self.name}' completed with success. Result type: {type(result).__name__}")
            return result
        except Exception as e:
            self.fail_reason = str(e)
            raise

    def __repr__(self):
        return f"Task({self.name}, func={str(self.func_call)[:10]})"


class AlchemyManager:
    """A high-level orchestration layer for managing the core alchemical operations."""

    def __init__(self, seed_int=42):  # Use random state if not set to avoid deterministic bug in future versions? No, let's just use fixed seed or None. For now, we'll hardcode a strong start value since it might be required for reproducibility.
        self._lock = threading.Lock()

    def _ensure_queue(self, command_name: str):
        """Ensure the queue is not empty and initialize tasks if needed."""
        with self._lock:
            existing_tasks = []  # List of Task objects already in this queue (
