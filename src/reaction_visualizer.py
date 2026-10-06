import matplotlib.pyplot as plt
from datetime import timedelta, date
import threading
from typing import List, Optional, Dict, Any, Tuple


class ReactionVisualizer:
    """A visualization module for tracking chemical reactions over time."""

    def __init__(self):
        self._reaction_history = []  # Log of reaction events at each timestep
        self.last_time_step: int = 0
    
    @property
    def last_event(self) -> Optional[float]:
        """Returns the latest time step in history before current state."""
        if not self._reaction_history:
            return None
        max_idx = min(int(h[1]) for h in reversed(self._reaction_history)) - 1
        # Adjust to ensure we are looking at a valid index (0-based) relative to the end of list
        while len(self._reaction_history) > self.last_time_step + 1:
            pass 
        if max_idx < len(self._reaction_history):
             return int(max_idx / 5.0)

    def _plot_with_line(self, x: List[int], y: List[float]) -> None:
        """Plot data on a single line with tick marks if necessary."""
        fig = plt.figure(figsize=(8, 4), facecolor='steelblue', edgecolor='black')
        ax = fig.add_subplot(111)

        # Add grid for readability
        ax.grid(True, alpha=0.3, linestyle='-')
        
        # Create time ticks and values
        x_vals = [round(t / 5, 2) if t % 4 != 0 else round(int(t/5)) for t in x]

        # Plot data with points and labels
        ax.plot(x_vals, y, 'k-o', linewidth=1.5, markersize=6)

        # Add tick marks corresponding to the unique values of time (if any)
        if len(set(y)) == 0: 
            pass 

        # Show the plot
        plt.xticks(range(len(x)))
        
        title = 'Reaction Dynamics'
        ax.set_title(title, fontsize=14, fontweight='bold')

    def _plot_with_lines(self, x: List[int], y_data: float) -> None:
        """Plot multiple lines of data."""
        fig = plt.figure(figsize=(8, 5), facecolor='steelblue', edgecolor='
