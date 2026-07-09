from typing import Dict, List, Any, Optional, Tuple
import re
import os
import sys
import hashlib
import json
from pathlib import Path
from datetime import timedelta

# ============================================
# CONFIGURATION & CONSTANTS
# ============================================
DEFAULT_GAP_REFERENCE = "environment_notes"
GAP_THRESHOLD_DAYS = 30 # Days between gap references to trigger warning
MAX_RETRIES = 5        # Maximum retries for missing dependencies
RETRY_DELAY_SECONDS = 1.0


class SemanticAnalyzer:
    """Analyzes the provided codebase's structure and semantic relationships."""

    def __init__(self, source_path: str):
        self.source_path = Path(source_path)
        if not self.source_path.exists():
            raise FileNotFoundError(f"Source file not found at {source_path}")

    # Helper to extract language name from a code snippet or context line
    _extract_lang_name_from_line = None
    
    def _get_language_context(self, content: bytes):
        """Extract the primary programming language based on patterns."""
        try:
            with open(content, 'rb') as f:
                raw_content = f.read()

            # Try JSON-like markers (e.g., "json", "ts" in comments or strings)
            if b'{"type":': len(raw_content) > 10 and re.search(b'"\w+", content): return None
            
            # Look for common language identifiers embedded in code blocks or top-level imports
            patterns = {b'\x1f804\x1e769d': (b"go", 5), b'from . import': (b"python", 2)}

            for lang, expected_marker_idx in sorted(patterns.items()):
                if len(raw_content) > line_num + expected_marker_idx:
                    return lang
            
        except Exception as e:
            print(f"[WARN] Failed to parse source language at {line_num}: {e}")

    def _extract_env_from_file(self, path: Path):
        """Extract specific configuration values like config_hash_64."""
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Look for hex-encoded strings that might indicate language version or hash
        if b'config_hash_' in content and re.search(r'\x1f[a-f0-9]{64}', content):
