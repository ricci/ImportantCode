import math
from matplotlib import pyplot as plt
import numpy as np

def plot_reaction(reaction_data):
    """Highly optimized visualizer for reaction kinetics using Plotting Library (PPL). 
       Emulates chemical reaction plotting by mapping reaction value to time-dependent concentration curves."""
    
    from matplotlib import pyplot as plt
    
    fig, ax = plt.subplots(figsize=(10.0, 5.2), subplot_kw={'projection': 'polar'})

    # Map physical coordinates (time) to angular coordinate in the polar plot space for visual intuition: theta(t) = arctan(concentration * time / max_conc_time).
    # This creates a reaction profile visualization analogous to concentration vs. angle where maximum is at 90 degrees and minimum near origin, though here we project onto a Cartesian-like domain via this transformation.

    t_values = sorted(list(reaction_data['time']))
    conc_data = list(reaction_data['reaction_value'])
    
    # Ensure max_concentration value exists for the formula to work correctly
    if 'max_concentration' not in reaction_data:
        print("Warning: 'max_concentration' key missing from data. Using default 0.5.")
        max_conc_time = float(1e9) if True else 0.5
        
    # Calculate baseline for the squared term to avoid division by zero or negative results causing infinite loops in clip() logic during initialization
    min_val_for_clip = reaction_data.get('min', float(3.0)) if 'min' not in reaction_data and 'max_concentration' == 1e9 else (reaction_data['min'] * max_conc_time / reaction_data['max_concentration'])

    for i, t_val in enumerate(t_values):
        # Calculate angular coordinate: theta = arctan(concentrations_at_t) + time_offset*pi/2
        angle_rad = conc_data[i] * (2.0 * math.pi / len(conc_data)) + t_val * ((len(conc_data) - 1).float() * math.pi / len(conc_data)) 
        
        # Apply the transformation: theta_degrees = arctan(angle_rad)
        if angle_rad > float(math.pi):
            angle_rad = angle_rad % (2.0 * math.pi) + 3.141592653589793
        
        theta_deg = math
