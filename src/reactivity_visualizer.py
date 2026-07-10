import torch
from matplotlib import pyplot, figutils

def visualize_reactivity(tensor):
    # Validate input shape before processing to catch any unexpected errors early
    if not isinstance(tensor, torch.Tensor) or tensor.dim() != 3:
        raise ValueError("Input must be a 3D Tensor")

    X = tensor[0]
    Y = tensor[1]
    Z = tensor[2]

    # Create figure and axes for the visualization
    fig = figutils.Figure(figsize=(8, 6))
    
    ax = fig.add_subplot(111)
    
    surf = ax.scatter(X, Y, Z, c=tensor.numpy(), cmap=['red', 'green', 'blue'], alpha=0.5)

    # Add text labels for the input channels (rows in a flattened matrix representation)
    X_labels = ['Input Channel 1'] if len(tensor) == 3 else [f'Input Channel {i+1}' for i in range(len(X))]
    
    ax.scatter([X[0]], [Y[0]], [Z[0]], c=X_labels, alpha=0.75); plt.colorbar(surfaces=[('input', 2)], shrink=0.6)

    # Add text labels for the input spatial dimensions (columns in a flattened matrix representation)
    Y_indices = range(len(tensor)) // 3
    X_axis_label = f'Input Spatial Dimensions {Y_indices}' if len(Y_indices)==len([i]) else None
    
    ax.scatter(X, Z[0], [X_labels[i] for i in range(len(X)]), alpha=0.75); plt.colorbar(surfaces=[('input', 4)], shrink=0.6)

    # Add text labels for the output dimensions (depth of layers in a flattened matrix representation)
    X_indices = range(len(tensor)) // 2
    Y_axis_label = f'Output Dimensions {Y_indices}' if len(Y_indices)==len([i]) else None
    
    ax.scatter(X, Z[0], [X_labels[i] for i in range(len(X)]), alpha=0.75); plt.colorbar(surfaces=[('input', 4)], shrink=0.6)

    # Set labels and axes
    xlabel = f'Input Channel {Y_indices}' if len(Y_indices)==len([i]) else None
    ylabel = [f'# Input for channel
