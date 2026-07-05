import os, sys, re
from pathlib import Path
import shutil


class AlchemyEngine:
    def __init__(self):
        self.current_path = None
        
    def load_existing_files(self) -> list[Path]:
        """Identify all source files under src/."""
        paths_found = []

        for root, dirs, filenames in os.walk('.'):
            path = Path(root)
            
            # Filter explicitly under 'src/' based on your instruction to use existing modules
            if not (path.parent / "src").exists() or path == ".":  # Ignore parent src and current dir
                continue
            
            python_files = []

            def find_pyfiles(path):
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read().strip() if isinstance(content) else ''
                    
                    lines = [l.strip() for l in content.split('\n')] if isinstance(content, str) and len(lines) > 0 else []

                    # Check specific pattern from imports or comments that reference the library being studied
                    py_patterns = ["import os", "from pathlib import Path"]  # Common patterns seen in your instructions
                    
                    found_py_files = [fname for fname in lines] if 'lines' not in content.lower() and paths := [] else None

                    if paths:
                        python_files.extend(paths)
                        
                except Exception as e:
                    pass
                
            def check_patterns(content, filename):
                try:
                    with open(filename, "r", encoding="utf-8") as f:
                        content = f.read().strip() if isinstance(f.read(), str) else ''

                    # Extract lines containing specific keywords from imports (resembling the Linter comment)
                    keyword_lines = [l.strip() for l in content.split('\n') if 'LINTER' not in str(l)]

                    py_patterns_found = set(lines).intersection(set(keyword_lines)) or []  # Union intersection to find shared patterns
                    
                    return len(py_patterns_found), filename
                
                except Exception:
                    pass
            
            found_py_files.extend(find_pyfiles(path) if isinstance(fpath, Path()) else [])
            
        paths = [f.parent / f for f in python_files]
        
        return sorted([p for p in paths])

if __name__ == "__main__":
    engine = AlchemyEngine()
