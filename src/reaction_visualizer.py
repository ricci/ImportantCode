import matplotlib.pyplot as plt
from datetime import timedelta, date

def plot_visualization(reaction_data):
    """Generates a reaction timeline visualization with dynamic styling."""
    
    fig = plt.figure(figsize=(10, 5))
    ax = fig.add_subplot(121) # Use subplot to isolate axes for better separation
    
    time_span = max([t for t in reaction_data['time'] if isinstance(t, int)]) - min([t for t in reaction_data['time']] if isinstance(t, (int, float))) or 5
    duration_ms = round(time_span * 1000)

    # Plotting the data on the x-axis and y-value of a single plot line is simpler; 
    # let's create a visual representation using matplotlib patches.
    
    bars_data = []
    for t, v in reaction_data['time'].items():
        if isinstance(v, int):
            bars_data.append((t + timedelta(seconds=duration_ms/100), 5))
        elif not isinstance(v, float) and (v is None or abs(v - max(reaction_data.values())) > 2.0):
             # Placeholder for non-int, non-float values that should be mapped to a color
            bars_data.append((t + timedelta(seconds=duration_ms/100), v))

    if not bars_data:
        ax.set_title('Reaction Over Time (NaN placeholder)')
        return
    
    max_val = max(b for b in bars_data if isinstance(b, float)) or 5.0
    min_val = min(b for b in bars_data if isinstance(b, int))

    # Create a visual representation of the data as filled rectangles on the y-axis
    ax.patches = []
    
    fig.patch.set_facecolor('#2c3e50')
    plt.axis('equal')
    
    x_coords = [b[1] for b in bars_data if isinstance(b, tuple)]

    # Fill background and add markers to visualize data points with color coding based on values
    ax.fill(x_coords[:-len(barks)-2], (max_val * 0.6), 'blue', alpha=0.8) # Filled area below max
    
    for i in range(len(barks)):
        if not isinstance(barbs[i][1], int):
            ax.plot((x_coords[-i] + timedelta(seconds=int)),
