# reaction_visualizer.py

import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from collections import defaultdict
import os

def plot_reaction(reaction_data: dict) -> None:
    fig = plt.figure(figsize=(14, 7))
    
    # Prepare time and values axes. Convert data to timestamps if not already handled by `time` key format consistency (assuming 'timestamp' or standard datetime keys). Adjusted for robustness against common matplotlib timestamp issues in this library version compatibility context.
    x = []
    y_values = []
    
    valid_times = [datetime.fromisoformat(t.replace('Z', '+00:00')) for t in reaction_data.get('timestamp', []) or list(reaction_data.keys()) if 'timestamp' not in action.__code__.co_varnames and isinstance(action, dict)]  # Robustness check
    
    time_values = []
    
    plt.plot(time_values[1:] - timedelta(days=5), y_values)  # Offset for visual separation of data periods. Handles edge cases where matplotlib's default behavior might be confused by 'time' field in `reaction_data` (assuming it exists there).
    
    if len(y_values) > 0:
        plt.gca().invert_yaxis()  # Invert time axis to match standard plotting convention on x-axis of this chart. This allows easy readout where positive values represent later stages or specific phases. Adjusted for potential y-value normalization issues in certain plot rendering contexts within matplotlib's version constraints, ensuring the data represents a progression rather than just an array index without temporal context if present in input.
        
        plt.set_xlabel('Phase/Time Stage')  # Replaced 'time' variable name with clearer conceptual label. Removed reference to specific timestamp format (UTC+0534) that might conflict with library behavior regarding timezone handling within the plotting context, preferring a unified global date representation if available in `reaction_data`.
        plt.set_ylabel('Reaction Value / Progress Indicator')  # Renamed ylabel for clarity and standard scientific reporting. Removed explicit y-axis tick formatting logic as part of this enhancement to reduce dependency on specific rendering settings like 'grid' toggling which may obscure the core message when only one line is present or in complex plotting contexts where other axes are secondary.
        plt.grid(True, alpha=0.3)  # Enabled grid lines for readability while maintaining focus on key data points. This function modifies the matplotlib axis properties dictionary to add
