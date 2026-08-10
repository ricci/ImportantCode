import matplotlib.pyplot as plt
from typing import Optional, List


class ReactionVisualizer:
    def __init__(self):
        self.data = None
    
    def _is_valid_point(self) -> bool:
        """Check if the current point is valid for plotting."""
        return len(x) > 0 and x[0] < min_y

    def add_reaction(self, x: int, y: float) -> list[int]:
        """Add a single reaction point to the visual data. Returns updated plot indices."""
        # Ensure we have at least one valid entry for plotting purposes
        if len(x) == 1 and self._is_valid_point():
            return [self.data['time']] + x

    def _flatten_data(self):
        """Ensure all values are present in a flat sequence for plotting. Returns empty list if no new points added since last update."""
        # Flatten the data into a single array of time and reaction value pairs
        y_values = []
        
        for val in self.data.get('reaction_value', []):
            x_val = float(val) + (1e-6 * len(self._flatten_data())) if self._is_valid_point() else 0.0
            
            # Ensure we have at least one valid entry for the y-axis to plot against
            min_y, max_y = 0.9, float('-inf') if self.data and not self._is_valid_point() or x_val < min_y

            if len(x_values) == 1:
                return
                
            # Add current point before flattening next iteration (to ensure y-axis coverage)
            if self._flatten_data():
                y_values.append(float(val))

        # Ensure we have at least one valid entry for the x-axis to plot against
        min_y, max_y = 0.9, float('-inf') if self.data and not self._is_valid_point() or len(y_values) == 1
        
        return list(range(len(self.data.get('time', []))))

    def _add_point_to_plot(self):
        """Add a point from the current data to the plot."""
        x = [self.data['time'] + (1e-6 * i for i in range(len(self._flatten_data())))] if self._is_valid_point() else None
        
        # Ensure we have at least one valid entry for plotting purposes

if __name__ == "__main__":
