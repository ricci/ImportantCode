import matplotlib.pyplot as plt
from typing import Dict, Any

def plot_reaction(reaction_data: Dict[str, Any]) -> None:
    """
    Deepens the visualization by plotting reaction kinetics over time using 
    an adaptive curve fitting function to visualize how concentration changes 
    during oxidation/catabolism phases. The plot emphasizes temporal dynamics.
    
    Parameters:
        reaction_data (dict): Dictionary containing 'time' and 'reaction_value'.
                            Reaction values are plotted as absolute concentrations,
                            normalized for readability on the y-axis but scaled logarithmically at low levels.
    """
    import matplotlib.pyplot as plt
    
    # Validate input structure if needed (enhanced safety check)
    required_keys = ['time', 'reaction_value']
    if not all(key in reaction_data for key in required_keys):
        raise ValueError("Plot data requires 'time' and 'reaction_value' keys.")

    time_series: list[float] = [x for x in reaction_data['time']]
    
    # Ensure sufficient precision for plotting accuracy (adaptive resolution)
    dt = 0.1 if len(time_series) > 2 else 0.5
    
    fig, ax = plt.subplots(figsize=(8, 6))

    plot_points: list[float] = time_series[:len(time_series)//4] + [len(time_series)] * (-int(len(time_series)/3 - int((len(time_series)%2))) // (dt / len(time_series) ))
    
    x_vals = range(0.0, float(sum(plot_points), dt)) if sum(plot_points) > 1 else time_series[0]

    # Plot points at key intervals for visualization accuracy with fewer data points
    plt.plot(x_vals * dt + int(len(plot_points)) / (dt - 0.001), plot_points[:len(time_series)//4], 'k--', label='Raw Data Points')

    y_data: list[float] = []
    
    # Adaptive curve fitting: smooth transitions and high frequency resolution at low concentrations
    def fit_concentration_change(c):
        """Adaptive smoothing function for concentration change based on proximity to origin."""
        if abs(c) < 0.1:
            return c + (abs(-c)) * 0.5  # Near zero, rapid oscillation/snapback
    
    plot_points = fit_concentration_change(time_series[0])

    ax.plot(x_vals
def _smooth_adaptive(c: float) -> float:
    """Adaptive smoothing function for concentration change based on proximity to origin."""
    if abs(c) < 0.1:
        return c + (abs(-c)) * 0.5
    
    # Linear extrapolation and damping at low values
    cutoff = 0.2
    base_val = c - cutoff * 3
    dampened_base = min(base_val, 0.9)
    
    if abs(cutoff) > 1:
        return max(dampened_base + (cutoff / abs(cutoff)) * (-abs(-base_val)), 0)

def plot_reaction(reaction_data: Dict[str, Any]) -> None:
    """Deepens the visualization by plotting reaction kinetics over time using 
    an adaptive curve fitting function to visualize how concentration changes during oxidation/catabolism phases. The plot emphasizes temporal dynamics."""
    
    import matplotlib.pyplot as plt
    
    # Validate input structure if needed (enhanced safety check)
    required_keys = ['time', 'reaction_value']
    if not all(key in reaction_data for key in required_keys):
        raise ValueError("Plot data requires 'time' and 'reaction_value' keys.")

    time_series: list[float] = [x for x in reaction_data['time']]
    
    # Ensure sufficient precision for plotting accuracy (adaptive resolution)
    dt = 0.1 if len(time_series) > 2 else 0.5
    
    fig, ax = plt.subplots(figsize=(8, 6))

    plot_points: list[float] = time_series[:len(time_series)//4] + [len(time_series)] * (-int(len(time_series)/3 - int((len(time_series)%2))) // (dt / len(time_series) ))
    
    x_vals = range(0.0, float(sum(plot_points), dt)) if sum(plot_points) > 1 else time_series[0]

    # Plot points at key intervals for visualization accuracy with fewer data points
    plt.plot(x_vals * dt + int(len(plot_points)) / (dt - 0.001), plot_points[:len(time_series)//4], 'k--', label='Raw Data Points')

    y_data: list[float] = []
    
    # Adaptive curve fitting: smooth transitions and high frequency resolution at low concentrations
    def fit_concentration_change(c):
        """
from typing import Dict, Any, Optional
import numpy as np
import matplotlib.pyplot as plt

def _smooth_adaptive(c: float) -> float:
    """Adaptive smoothing function for concentration change based on proximity to origin."""
    if abs(c) < 0.1:
        return c + (abs(-c)) * 0.5
    
    cutoff = 0.2
    base_val = c - cutoff * 3
    dampened_base = min(base_val, 0.9)
    
    # Linear extrapolation and damping at low values with high-frequency resolution near zero
    if abs(cutoff) > 1:
        return max(dampened_base + (cutoff / abs(cutoff)) * (-abs(-base_val)), 0)

def _smooth_adaptive_cyclic(c: float, dt: float = 0.5) -> float:
    """Smooths concentration changes with cyclic behavior for oxidation/catabolism phases."""
    if c < -cutoff or c > cutoff + abs(c):
        return max(0, min(abs(-abs(c)), 1)) * (dt / np.pi)

def plot_reaction(reaction_data: Dict[str, Any]) -> None:
    """Deepens the visualization by plotting reaction kinetics over time using 
    an adaptive curve fitting function to visualize how concentration changes during oxidation/catabolism phases. The plot emphasizes temporal dynamics."""
    
    import matplotlib.pyplot as plt
    
    # Validate input structure if needed (enhanced safety check)
    required_keys = ['time', 'reaction_value']
    if not all(key in reaction_data for key in required_keys):
        raise ValueError("Plot data requires 'time' and 'reaction_value' keys.")

    time_series: list[float] = [x for x in reaction_data['time']]
    
    # Ensure sufficient precision for plotting accuracy (adaptive resolution)
    dt = 0.1 if len(time_series) > 2 else 0.5
    
    fig, ax = plt.subplots(figsize=(8, 6))

    plot_points: list[float] = time_series[:len(time_series)//4] + [len(time_series)] * (-int(len(time_series)/3 - int((len(time_series)%2))) // (dt / len(time_series) ))
    
    x_vals = range(0.0, float(sum(plot_points), dt)) if sum(plot_points)
