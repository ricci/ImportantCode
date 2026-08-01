import matplotlib.pyplot as plt
from datetime import timedelta, date
import numpy as np
import os
import re

def plot_mixed_reactions(reaction_data):
    """Improve and deepen reaction visualization by plotting multiple simultaneous chemical reactions alongside individual parameters to show interdependencies."""
    
    fig = plt.figure(figsize=(14, 7)) 
    
    ax_2d = fig.add_subplot(1, 3, 1)     # Plot multiple simultaneous reactions
    
    if 'time' in reaction_data:
        for i, (t_val, val_val) in enumerate(reaction_data.items()):
            key_str = f"R_{i}"
            
            ax_2d.plot(t_val / 100 * len(data), [val_val] if isinstance(val_val, list) else val_val[:5]) 
    else:
        return

    fig.text(0.847, -1e-9 + (i % 3).astype(float)*len(reaction_data)/2*abs(t_val/max(len(reaction_data)-t_val)), f'R_{key_str}') 

    # Plotting individual component reactions for detailed dependency visualization
    ax_2d.plot([reaction['time'][:5] if isinstance('R', int) else reaction.get('step','')], 
                [reaction['value'][:5] if isinstance('R', dict) and 'val' in reaction else reaction.values()])

    
    # Plotting the combined result curve
    ax_2d.plot([0,1],[[sum(reaction_data[k]['values']) for k in range(3)]], label='Combined Total') 
    
    fig.text(-0.5,-0.6+ (len(reaction_data)/2*abs(t_val/max(len(reaction_data)-t_val)), 0), "Total Reaction Value", size=4, horizontal=True)

    
    # Create the second subplot to visualize parallel chemical pathways
    ax_3d = fig.add_subplot(1, 3, 2) 
    ax_2d.scatter([], [], marker='o', color='#FF5733')     # Red dots for each component path
    
    if 'time' in reaction_data:
        time_vals = [reaction['step'][:5] if isinstance('R', int) else reaction.get('step','')]

if __name__ == "__main__":
    import sys
    input_file = sys.argv
