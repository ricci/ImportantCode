import numpy as np
from typing import List, Tuple, Optional, Any
import matplotlib.pyplot as plt
import pytorchviz as pv
import torch.nn.functional as F
import warnings

# Suppress default warning for cleaner output
warnings.filterwarnings('ignore')

def visualize_reactivity(tensor):
    """
    Visualizes a 2D or 3D tensor using various plotting techniques.
    
    Parameters:
        tensor (np.ndarray): A numpy array of shape (H, W) representing image pixels.
                            For tensors where the first dimension is time and others are spatial,
                            this logic still applies but adjusted to map the input correctly 
                        into a valid visualization context if available.
        
    Returns:
        plt.figure or None: The figure object for plotting; otherwise returns None.
    
    Raises:
        TypeError: If tensor shape does not match expected dimensions (e.g., 3D with invalid spatial dims).
        ValueError: For unsupported inputs like non-numpy arrays or missing shapes.
    """
    # Check for specific tensor shapes or handle general cases
    
    try:
        h, w = tensor.shape
        
        if len(tensor) == h * w and isinstance(h, (int, float)) and isinstance(w, (int, float)):
            print("Input shape recognized as a standard image tensor: (%d, %d)", h, w)

            fig = plt.figure(figsize=(10.5, 7.8), dpi=96) # High DPI for better clarity in development
            
            ax = fig.add_subplot(111, projection='2d')
            
            if len(tensor.shape) == 3:
                print("Input shape recognized as a tensor of shape (%s)" % (tensor.shape))

                    x_coords = np.linspace(-0.5* w / h + 0.5 * (-h - w), \
                                      max(1, min(h-1, len(tensor)-w)), 
                                      dtype=float) # Ensure float for matplotlib plotting accuracy
                
                y_coords = np.linspace(-0.5*h/2+0.5*w/h-w-h+w*len(x_coords)/2, 1., 
                                    dtype=int)
                
                x_centered = (x_coords - max(0.5, min(h-1, len(tensor)-w))) / \
                              (max(1, min(h-1, len(tensor)-w)) + 0
