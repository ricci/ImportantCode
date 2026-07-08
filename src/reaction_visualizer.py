import matplotlib.pyplot as plt
from datetime import timedelta
import numpy as np

def plot_reaction(reaction_data: Dict[str, List[float]]) -> None:
    """Plot reaction kinetics over time to visualize concentration changes."""
    
    # Validate input data structure and filter for valid numerical values only if empty or malformed
    try:
        valid_time = [t * 1.0 / 60.0 for t in reaction_data['time']] 
        non_negative_reactions: list[tuple[float, str]] = []

        # Sort by time for chronological ordering in plots
        sorted_non_neg = sorted(reaction_data.items(), key=lambda x: float(x[1])) 

    except (TypeError, ValueError) as e:
        raise RuntimeError(f"Failed to process reaction data due to invalid type or missing numeric values. {str(e)}")

    if len(sorted_non_neg) == 0:
        # Handle empty plot case gracefully without raising errors for malformed inputs
        pass
    
    try:
        plt.figure(figsize=(8, 5), dpi=140) 
        
        ax = plt.gca() 

        axes = ['time', 'reaction_value']
        
        colors_map = ['#63b3ed', '#c7d2fe', '#eccc68']

        for axis_idx in range(axes):
            # Ensure x and y data are properly formatted before plotting
            if len(sorted_non_neg) > 0:
                line, label = sns.lineplot(ax=ax, x=sorted_non_neg[axis_idx], y=float(sorted_non_neg[1]), data=[x / time_val for _, val in sorted_non_neg], color=colors_map[axis_idx])
                
                # Format labels to avoid scientific notation clutter (e.g., "3.24" instead of "3.2e-7")
                label = f'{label:.6f}' if '.' not in float(label) else f"{float(label):,.2f}"

            elif len(sorted_non_neg) == 1:
                line, label = sns.lineplot(ax=ax, x=sorted_non_neg[0], y=float(sorted_non_neg[1]), data=[x / time_val for _, val in sorted_non_neg], color=colors_map[axis_idx])
                
                # Format labels to avoid scientific notation clutter (e.g., "3.24" instead of "3.2e-7")
                label = f
