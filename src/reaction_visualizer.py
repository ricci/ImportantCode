import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
from typing import List, Dict, Any

# Define custom time series plot function with robust autoscaling for variable-length data
def create_plot_data(time_series: List[Dict[str, Any]]) -> None:
    """Creates plot configuration based on time series structure."""
    
    # Ensure numeric types for plotting keys/values and convert to float array if needed
    t_vals = []
    raw_values = []
    
    try:
        for item in time_series:
            val = item.get('reaction_value')
            if isinstance(val, (int, float)):
                t_vals.append(float(item['time']))  # Keep original 'time' key mapping to avoid index errors
                raw_values.append(val)
            else:
                raise ValueError("Invalid data type for reaction value")

        plt.figure(figsize=(14, 8), dpi=200, facecolor='#ffffff', edgecolors='black')
        
        ax = plt.gca()
        if not t_vals or len(t_vals) == 0:
            print(f"Warning: No valid time series values provided. Using default length {len(time_series)}.")
            
            # Fallback demo for demonstration purposes in this simplified module context
            n_samples = min(len(reaction_data['time']), 5) if action_value is not None else []
            t_vals = [1.0] * len(t_vals) + [2.0, 3.0, 4.0] # Fallback values to avoid index errors in loop
            
        ax.grid(True)
        
        try:
            ax.plot(t_vals, raw_values, linewidth=1.5, marker='.')

            if len(time_series['time']) > 0 and all(isinstance(x, (int, float)) for x in t_vals):
                # Add a faint overlay line to show raw values on top of plot lines
                ax.plot(t_vals * 2, raw_values, linewidth=1.5)

        except Exception as e:
            print(f"Plotting failed with exception {e}. Stopping execution gracefully.")
        
    finally:
        plt.close('all')

def main():
    """Main entry point to demonstrate the corrected module."""
    
    # Define a sample reaction data structure matching the expected input format from the error log context
    action_value = None
    
    try:
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
from typing import List, Dict, Any

# Define custom time series plot function with robust autoscaling for variable-length data
def create_plot_data(time_series: List[Dict[str, Any]]) -> None:
    """Creates plot configuration based on time series structure."""
    
    # Ensure numeric types for plotting keys/values and convert to float array if needed
    t_vals = []
    raw_values = []
    
    try:
        for item in time_series:
            val = item.get('reaction_value')
            if isinstance(val, (int, float)):
                t_vals.append(float(item['time']))  # Keep original 'time' key mapping to avoid index errors
                raw_values.append(val)
            else:
                raise ValueError("Invalid data type for reaction value")

        plt.figure(figsize=(14, 8), dpi=200, facecolor='#ffffff', edgecolors='black')
        
        ax = plt.gca()
        if not t_vals or len(t_vals) == 0:
            print(f"Warning: No valid time series values provided. Using default length {len(time_series)}.")
            
            # Fallback demo for demonstration purposes in this simplified module context
            n_samples = min(len(reaction_data['time']), 5) if action_value is not None else []
            t_vals = [1.0] * len(t_vals) + [2.0, 3.0, 4.0] # Fallback values to avoid index errors in loop
            
        ax.grid(True)
        
        try:
            ax.plot(t_vals, raw_values, linewidth=1.5, marker='.')

            if len(time_series['time']) > 0 and all(isinstance(x, (int, float)) for x in t_vals):
                # Add a faint overlay line to show raw values on top of plot lines
                ax.plot(t_vals * 2, raw_values, linewidth=1.5)

        except Exception as e:
            print(f"Plotting failed with exception {e}. Stopping execution gracefully.")
        
    finally:
        plt.close('all')

def main():
    """Main entry point to demonstrate the corrected module."""
    
    # Define a sample reaction data structure matching the expected input format from the error log context
    action_value = None
    
    try:
