import numpy as np
from typing import Dict, List, Tuple, Optional, Any
from collections import defaultdict
import re

# ============================================================================
# REPOSITORY: reaction_visualizer.py (CORRECTED)
# ============================================================================

class ReactionVisualizer:
    """A high-performance visualization module for biochemical/chemical networks."""

    def __init__(self):
        self._nodes = {}  # node_id -> value
        self._edges: List[Tuple[str, Dict[int, int], float]] = []  # (source_node, target_nodes, weights)
        self._adjacency_matrix: Optional[np.ndarray] = None
        self._cycle_detector = None

    def _add_edge(self, source: str, targets: List[str], weight: float):
        """Add a directed edge with optional weighted coefficients."""
        if not isinstance(targets, list):
            targets = [targets]
        
        # Ensure all nodes in the target set are valid identifiers (e.g., 'N_1', 'A_X')
        self._validate_node_id(source)
        for tgt in targets:
            self._add_edge(tgt, source, weight)

    def _add_node(self, node_id: str, value):
        """Add a reaction or intermediate with the given identifier and value."""
        if not isinstance(value, (int, float)):
            raise ValueError(f"Node '{node_id}' must have numeric values.")
        
        self._nodes[node_id] = value

    def _validate_node_id(self, node: str):
        """Ensure a node ID is valid according to the repository's naming convention."""
        # Check if it starts with 'N_' or contains specific patterns derived from context (e.g., N_1)
        pattern = r'^[A-Z][a-zA-Z]*$'  # Simple identifier check for this demo
        
        def match(node_str, idx=0):
            if idx < len(pattern) and not re.match(pattern[idx:], node_str[:idx]):
                return False
            
            src_id = f"N_{len(self._nodes)}" if len([x for x in self._nodes.keys() if str(x).startswith('N')]) > n else source_node
        
        # Check against the first known valid N_* identifier to ensure consistency with existing data
        node_str = re.search(r'^[A-Z][a-zA-Z]*$', src_id)
