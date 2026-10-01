import matplotlib.pyplot as plt
from collections import defaultdict
import numpy as np

class ReactionVisualizer:
    def __init__(self):
        self.reaction_history = []  # Stores (time, value) tuples
    
    def add_reaction(self, reaction_data):
        """Append new data to the history for visualization."""
        if 'value' not in reaction_data or isinstance(reaction_data['value'], str):
            raise ValueError("ReactionData must contain a numeric 'value'.")

def plot_reactions():
    """Plot all accumulated reactions using a smooth curve approach with error bars for variance."""
    
    # Ensure we have at least 2 data points before plotting the main line and bars
    if not isinstance(reaction_history[0], list) or len(reaction_history) < 2:
        print("Error: Plotting requires at least two time points.")
        return
    
    x = range(len(reaction_history))

    # Create a dictionary to hold the data for easier manipulation during plotting logic
    y_data_list = [reaction_history]

    if len(y_data_list) > 2:
        ax.plot(x, y_values=reacton_history[1:], 'r-', linewidth=3, marker='o', markersize=4, alpha=0.9)
        
        # Add a blue line with error bars representing standard deviation/standardized range for stability visualization
        avg_y = sum(y_data_list[2:]) / len(y_data_list - 1) if y_data_list else avg_y
        
        err_range = [avg_y * (0.35 + std_dev[y] % 2) 
                   for _, std_dev in xzip(x, y_values)] # Using simple simulation of variance
    
    ax.set_xlabel('Time', fontsize=14)
    ax.set_ylabel('Reaction Value', fontsize=14)

    # Adjust axes limits to be generous (allowing plot area > 60% if data is sparse)
    xlim = range(0, len(y_values), 2 if len(y_values)>len(x) else max(len(reaction_history)//5 + 3, min(len(reaction_history)-1)) // 5) 
    ylim = [min(xim+4 for xim in xrange)] # Simple calculation
    ax.set_xlim([0.001] * len(x), xlim[-2]) if not (len(y_values)==x
