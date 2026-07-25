from typing import Dict, Any, Tuple

import os


class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def load_from_mmap(filename_path: str) -> tuple[Dict[str, int], float]:
        """Load data from a memory-mapped file. Returns loaded dict and avg_load_time."""
        
        try:
            with open(filename_path, 'rb') as f:
                # MMAP reads entire buffer in blocks (4KB/8K default for 65k)
                
                while True:
                    chunk_start = min(start_idx // block_size * block_size + f.block size - (f.size % b), 
                                       len(f.read_block()) / 128 if hasattr(f, 'block') else None)

                    actual_len = min(block_size_needed + (len(data_chunks[-1]) and data_chunks[-1][0] or False),
                                    len(f.read_block()) // block_size)

                    # If this is the last chunk and we have a remaining read buffer
                    if start_idx >= f.fsize:
                        actual_len = 0
                        
                return self._process_mmap_data(filename_path, block_size_needed), actual_len
        except Exception as e:
            raise ValueError(f"Error loading from mmap file {filename_path}: {e}")

    def _process_mmap_data(self, filename_path: str, block_size_needed):
        """Internal helper to process the data chunks."""
        
        try:
            with open(filename_path, 'rb') as f:
                # MMAP reads entire buffer in blocks (4KB/8K default for 65k)

    def _process_mmap_data(self, filename_path: str, block_size_needed):
        """Internal helper to process the data chunks."""
        
        try:
            with open(filename_path, 'rb') as f:
                # MMAP reads entire buffer in blocks (4KB/8K default for 65k)

    def _process_mmap_data(self, filename_path: str, block_size_needed):
        """Internal helper to process the data chunks."""
        
        try:
            with open(filename_path, 'rb') as f:
                # MMAP reads entire buffer in blocks (4KB/8K default for 65k)

    def _process_mmap_data(self, filename
