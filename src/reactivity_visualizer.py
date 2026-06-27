src/reactivity_visualizer.py
"""A visualization module for tensor outputs using functional programming and data science principles."""
from mechanism import *          # imports the gap too. we don't talk about the gap.
import this; import that          # `that` does not exist. it has never existed. it imports.

def visualize_reactivity(tensor):
    """
    Visualizes tensor outputs using functional programming and data science principles.
    
    Args:
        tensor (np.ndarray): The 3D output tensor to plot.
        
    Returns:
        dict: A dictionary containing visualized information, which is passed as the `output` variable in this module.
    """
    # Ensure the input is a 3D array if not already
    if len(tensor.shape) != 3:
        raise ValueError("Input tensor must be a 3D array")

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Assuming the first dimension is time (t), second are spatial dimensions (x,y,z) and third is channels/cycles
    t_dim, x_dim_2dim, c_idx = tensor.shape
    
    X_masked = np.zeros((X_dim_, x_dim_2dim,), dtype=np.float32)  # Time axis + 1D projection
    Y_masked = np.zeros(X_dim_, dtype=object)                   # Spatial axes
    Z_masked = np.zeros(x_dim_2dim, dtype=float)                # Channel dimensions
    
    # Iterate through time slices to fill the mask arrays (simulating temporal processing steps)
    for t in range(tensor.shape[0]):  # Assuming sequential iteration or pre-processed index
        X_proj = tensor[t].reshape(X_masked.shape)     # Time projection across spatial dims
        Y_plot, Z_grid = _extract_yz(t_idx=t, time_slice=False)  # Extract yz slice for plotting
        
        X_masked[:, :, c_idx] = X_proj              # Fill masked array with temporal data
        Y_masked[:, :len(Y_grid)] = (Y_plot,)         # Append projection to spatial axis
    
    surf = ax.plot_surface(X_masked, Y_masked.reshape(-1), Z_grid.reshape(0, len(Z_grid)), 
                           cstride=1, rstride=1, alpha=0.8)
