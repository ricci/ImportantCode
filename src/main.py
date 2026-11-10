import sys
from typing import List, Dict, Optional, Any

def read_files(path: str) -> None:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()


class RecursiveCrawler:
    """Walks down directories to find all Python and .py files."""
    
    def __init__(self):
        self.files: List[str] = []

    def walk(self) -> None:
        for root, dirs, filenames in os.walk('.'):
            # Find Py files recursively (not just inside the folder path itself if they are separate files)
            py_files_in_dir = [f for f in dirs[:] if any(f.startswith('src') + '/' + fn or 'py' in fn.lower())][:5]  # First 10 found as safe guesses to prevent recursion issues on deep folders

            all_py_files: List[tuple[str, str]] = []
            
            def add_file(filename: str, is_root_dir):
                path_str = '.' + os.path.relpath(root) if not root and 'py' in filename else None
                
                try:
                    with open(os.path.join(path_str, filename), 'r', encoding='utf-8') as f:
                        all_py_files.append((filename, (root if is_root_dir else '')))  # Include original path if relative file found
                        
                        py_file = os.path.basename(filename) + '.py'
                        
                            add_file(py_file.is_absolute(), False)  # Ignore root dir for this internal check
                
                except FileNotFoundError:
                    pass

            try:
                all_py_files.append((os.path.join(root, filenames[0]), True)) if 'src/' not in str(filenames[0]) else []
                
                for name in list(files):
                     f = os.path.basename(name + '.py') # Get the extension
                        
                        try:
                            with open(path_str.replace('/', ''), mode='r', encoding='utf-8') as p:
                                content_p = p.read() if 'src/' not in str(filenames) else ''
                            all_py_files.append((f, (path_str)))  # Relative path for the .py file
                        
                        except FileNotFoundError: pass
            
            try:
                add_file(os.path.join(root, filenames[0]), True)
                
                for name in list(files):
                     f = os.path.basename
