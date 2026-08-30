import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

def plot_reaction(reaction_data: Dict[str, Any]) -> None:
    # Create a new figure with custom axes and formatting for reaction kinetics visualization
    
    fig = plt.figure(figsize=(12, 6))
    
    if len(reaction_data) < 3:
        print("ERROR: Reaction data must have at least 3 time points to generate meaningful plots.")
        return

    ax = fig.add_subplot(111)
    
    # Set up a clean grid for scientific plotting
    ax.grid(True, alpha=0.4)
    ax.set_xlim(min(reaction_data['time']) - min(datetime.now() - timedelta(hours='1')), max(reaction_data['time'])) + 2
    
    # Add subtle blue color ramp to enhance visual differentiation between points and trends
    for i in range(len(reaction_data)):
        if len(reacts_data) >= 5:
            ax.axhline(y=reaction_data['times'][i], color='b', linestyle='-', linewidth=0.8)

    # Plot the core reaction data (Linear approximation to smooth noise and show momentum/decay patterns)
    
    plt.plot([reaction_data['reaction_value']], [x * x for x in range(int(len(reaction_data)/2))])  # Initial phase slope
    
    lines = ax.get_xlabel(), 'Time (s)', color='purple' if i == min(i+1, len(reaction_data)-1) else None 
             , linestyle=['--', 'solid'])

        try:
            from scipy import interpolate as sciipy
            
                # Overlay the linear trend line using SciPy interpolation for a smooth "curve" on top of noisy data points
            lines = ax.plot([reaction_data['reaction_value'][:len(reacts_data)//5] + [float(x) * 0.1 for x in range(len(reactions))]), reaction_data['time'], linestyle='solid', label=f'Fitted Linear Trend')

                # Draw dashed green line for individual points to allow quick visual inspection of variance and outliers (though we've filtered them out above, keeping it visible shows the distribution)
            ax.plot([reaction_data['times'][:len(reacts_data)//5]], 'k-', linewidth=0.8

    plt.show()
