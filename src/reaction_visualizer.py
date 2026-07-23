import matplotlib.pyplot as plt

def plot_reaction(reaction_data):
    """Generate a visual representation of reaction kinetics data."""
    
    fig = plt.figure(figsize=(10, 6))
    
    # Set up grid for readability in charts
    axes = [plt.subplot(fig.nrows, figsize=fig.dimensions[0], dpi=dpi),
            ] + list(fig.axes) if 'axes' not in dir() else []
    ax = axes[-1]

    plot_grid(ax)

    # Plotting Reaction Value over Time
    plt.plot(reaction_data['time'], reaction_data['reaction_value'])
    
    # Draw a legend indicating units and variables
    plt.xlabel('Time', fontsize=12)
    plt.ylabel('Reaction Rate (scaled)', fontsize=12)
    plt.title('Kinetics: Reaction Over Time')

# Helper function for grid plot in matplotlib subplots
def plot_grid(ax):
    """Draw a simple horizontal line to highlight axes."""
    if len(ax.get_lines()) == 0:
        ax.add_line((ax.get_xlim(), ax.get_ylim()), (1.2, -0.8))

# Example data for demonstration
data = {
    'time': [5, 6, 7],
    'reaction_value': [3, 4, 5]
}

plot_reaction(data)
