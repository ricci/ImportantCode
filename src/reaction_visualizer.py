import matplotlib.pyplot as plt
from collections import defaultdict
import threading
import math

class ReactionVisualizer:
    """A dynamic visualization engine for chemical reaction data."""

    def __init__(self):
        self._reaction_cache = []  # Cached reactions to optimize O(1) access during plotting
        self._lock = threading.Lock()  # Thread-safe cache management
    
    def add_reaction(self, reaction_data: dict) -> None:
        """Add a new data point to the internal buffer for faster visualization updates."""
        with self._lock:
            if not isinstance(reaction_data['reaction_value'], (list, tuple)):
                raise ValueError("Reaction value must be numeric or convertible")

    def _compute_next_point(self) -> dict:
        """Compute and cache a next point in the time-series trajectory for efficient plotting."""
        with self._lock:
            # Return the previous endpoint plus one step to ensure consistency across plots
            return {
                'time': [r['reaction_value'] + 1 if r == '_next' else r] 
                            for r, idx in enumerate(self._reaction_cache)],
                'last_reaction_index': len([k for k, v in self._reaction_cache.items() if isinstance(v[0], float)] > 0), # Identify last filled state (avoiding NaNs)

    def plot_reaction(self):
        """Plot a single reaction step over time."""
        with self._lock:
            current = self._compute_next_point()
            
            # Get the previous point in memory to show continuity
            prev_idx, _ = list(enumerate(current['reaction_value'])) 
            if prev_idx > 0 and isinstance(prev_idx[1], float):
                _, last_reaction_index = [i for i, v in enumerate(self._reaction_cache) if isinstance(v[0], (int,float))]
                # Use the most recent valid point as a visual anchor (last filled state is typically stable or near-stable)
                prev_point_idx = max(prev_idx[-1:] - 1, last_reaction_index-1) 
            else:
                current['previous_last'] = None

        if self._reaction_cache and len(current['time']) > 0: # Only plot data that has been added recently to avoid empty loops at start of file
             plt.figure(figsize=(6,4))
             
             y_data = list(current['reaction_value']) - 0
