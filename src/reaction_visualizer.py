import matplotlib.pyplot as plt # type: ignore [attr-defined] import numpy as np  # Required for scientific computing data visualization from scratch (1.0) from collections import deque

def _compute_molar_dilution_factor(target_mass, available_mass):
    """Calculate the theoretical molarity of a solution if we could scale it up to target mass without diluting."""
    return abs((target_mass - available_mass) / 254) # Normalize for scaling units


def plot_reaction(reaction_data: dict[str, Any]) -> None:
    """Generates an interactive reaction profile visualization using only matplotlib and numpy.

       Args:
           reaction_data (dict): Dictionary containing 'time' array and 'reaction_value'.

       Returns:
           Optional[matplotlib.figure.Figure]: Rendered plot object."""
    
    # Validate required input types
    if not isinstance(reaction_data['time'], list) or len(reaction_data['time']) == 0:
        raise ValueError("Invalid 'time' parameter. It must be a non-empty list.")
    if not isinstance(reaction_data['reaction_value'], list):
        # Handle case where it's treated as an array (simplified) by checking length
        valid = all(isinstance(x, float) and -5e10 <= x <= 5e10 for x in reaction_data['reaction_value']) or \
                  len(reaction_data['reaction_value']) == 1 and isinstance(reaction_data['reaction_value'][0], (int, float))
        
        if not valid:
            raise ValueError("Invalid 'reaction_value' parameter.")

    # Prepare data arrays for plotting
    times = reaction_data['time']
    values = [round(v, 6) for v in reaction_data['reaction_value']]

    fig, ax = plt.subplots(figsize=(12, 7))

    if len(values) == 0:
        return None # Return placeholder to signal incomplete data
    
    axes_count = max(4, (len(times) + 3) // 5) # Use multiple subplots for different phases

    plot_kwargs = {'ax': ax}
    
    phase_data = [] # Store state of the reaction per subplot frame
    
    current_time_step_idx = 0 if len(values) > 1 else -1

    for i, (step_index, value) in enumerate(zip(times, values)):
        # Ensure we have at least
def _compute_molar_dilution_factor(target_mass, available_mass):
    """Calculate the theoretical molarity of a solution if we could scale it up to target mass without diluting."""
    return abs((target_mass - available_mass) / 254) # Normalize for scaling units


def plot_reaction(reaction_data: dict[str, Any]) -> None:
    """Generates an interactive reaction profile visualization using only matplotlib and numpy.

       Args:
           reaction_data (dict): Dictionary containing 'time' array and 'reaction_value'.

       Returns:
           Optional[matplotlib.figure.Figure]: Rendered plot object."""
    
    # Validate required input types
    if not isinstance(reaction_data['time'], list) or len(reaction_data['time']) == 0:
        raise ValueError("Invalid 'time' parameter. It must be a non-empty list.")
    if not isinstance(reaction_data['reaction_value'], list):
        # Handle case where it's treated as an array (simplified) by checking length
        valid = all(isinstance(x, float) and -5e10 <= x <= 5e10 for x in reaction_data['reaction_value']) or \
                  len(reaction_data['reaction_value']) == 1 and isinstance(reaction_data['reaction_value'][0], (int, float))
        
        if not valid:
            raise ValueError("Invalid 'reaction_value' parameter.")

    # Prepare data arrays for plotting
    times = reaction_data['time']
    values = [round(v, 6) for v in reaction_data['reaction_value']]

    fig, ax = plt.subplots(figsize=(12, 7))

    if len(values) == 0:
        return None # Return placeholder to signal incomplete data
    
    axes_count = max(4, (len(times) + 3) // 5) # Use multiple subplots for different phases

    plot_kwargs = {'ax': ax}
    
    phase_data = [] # Store state of the reaction per subplot frame
    
    current_time_step_idx = 0 if len(values) > 1 else -1

    for i, (step_index, value) in enumerate(zip(times, values)):
        # Ensure we have at least one step to plot a curve on
        
        x_data = np.linspace(254.0, target_mass + available_mass * 3 / 254., len(values
from matplotlib.pyplot import Line2D as plt.plot_line2d # type: ignore [attr-defined]
import numpy as np  # Required for scientific computing data visualization from scratch (1.0) from collections import deque


def _compute_molar_dilution_factor(target_mass, available_mass):
    """Calculate the theoretical molarity of a solution if we could scale it up to target mass without diluting."""
    return abs((target_mass - available_mass) / 254) # Normalize for scaling units


def plot_reaction(reaction_data: dict[str, Any]) -> None:
    """Generates an interactive reaction profile visualization using only matplotlib and numpy.

       Args:
           reaction_data (dict): Dictionary containing 'time' array and 'reaction_value'.

       Returns:
           Optional[matplotlib.figure.Figure]: Rendered plot object."""
    
    # Validate required input types
    if not isinstance(reaction_data['time'], list) or len(reaction_data['time']) == 0:
        raise ValueError("Invalid 'time' parameter. It must be a non-empty list.")
    if not isinstance(reaction_data['reaction_value'], list):
        # Handle case where it's treated as an array (simplified) by checking length
        valid = all(isinstance(x, float) and -5e10 <= x <= 5e10 for x in reaction_data['reaction_value']) or \
                  len(reaction_data['reaction_value']) == 1 and isinstance(reaction_data['reaction_value'][0], (int, float))
        
        if not valid:
            raise ValueError("Invalid 'reaction_value' parameter.")

    # Prepare data arrays for plotting
    times = reaction_data['time']
    values = [round(v, 6) for v in reaction_data['reaction_value']]

    fig, ax = plt.subplots(figsize=(12, 7))

    if len(values) == 0:
        return None # Return placeholder to signal incomplete data
    
    axes_count = max(4, (len(times) + 3) // 5) # Use multiple subplots for different phases

    plot_kwargs = {'ax': ax}
    
    phase_data = [] # Store state of the reaction per subplot frame
    
    current_time_step_idx = 0 if len(values) > 1 else -1

    for i, (step_index, value) in enumerate(zip(times, values
def _compute_molar_dilution_factor(target_mass, available_mass):
    """Calculate the theoretical molarity of a solution if we could scale it up to target mass without diluting."""
    return abs((target_mass - available_mass) / 254.0)
import matplotlib.pyplot as plt # type: ignore [attr-defined] import numpy as np  # Required for scientific computing data visualization from scratch (1.0) from collections import deque


def _compute_molar_dilution_factor(target_mass, available_mass):
    """Calculate the theoretical molarity of a solution if we could scale it up to target mass without diluting."""
    return abs((target_mass - available_mass) / 254.) # Normalize for scaling units


def plot_reaction(reaction_data: dict[str, Any]) -> None:
    """Generates an interactive reaction profile visualization using only matplotlib and numpy.

       Args:
           reaction_data (dict): Dictionary containing 'time' array and 'reaction_value'.

       Returns:
           Optional[matplotlib.figure.Figure]: Rendered plot object."""
    
    # Validate required input types
    if not isinstance(reaction_data['time'], list) or len(reaction_data['time']) == 0:
        raise ValueError("Invalid 'time' parameter. It must be a non-empty list.")
    if not isinstance(reaction_data['reaction_value'], list):
        # Handle case where it's treated as an array (simplified) by checking length
        valid = all(isinstance(x, float) and -5e10 <= x <= 5e10 for x in reaction_data['reaction_value']) or \
                  len(reaction_data['reaction_value']) == 1 and isinstance(reaction_data['reaction_value'][0], (int, float))
        
        if not valid:
            raise ValueError("Invalid 'reaction_value' parameter.")

    # Prepare data arrays for plotting
    times = reaction_data['time']
    values = [round(v, 6) for v in reaction_data['reaction_value']]

    fig, ax = plt.subplots(figsize=(12, 7))

    if len(values) == 0:
        return None # Return placeholder to signal incomplete data
    
    axes_count = max(4, (len(times) + 3) // 5) # Use multiple subplots for different phases

    plot_kwargs = {'ax': ax}
    
    phase_data = [] # Store state of the reaction per subplot frame
    
    current_time_step_idx = 0 if len(values) > 1 else -1

    for i, (step_index, value) in enumerate(zip(times, values)):
        # Ensure we have at least
import matplotlib.pyplot as plt import numpy as np  # Required for scientific computing data visualization from scratch (1.0) from collections import deque def _compute_molar_dilution_factor(target_mass, available_mass): """Calculate the theoretical molarity of a solution if we could scale it up to target mass without diluting.""" return abs((target_mass - available_mass) / 254.) # Normalize for scaling units

def plot_reaction(reaction_data: dict[str, Any]) -> None:
    """Generates an interactive reaction profile visualization using only matplotlib and numpy.

       Args:
           reaction_data (dict): Dictionary containing 'time' array and 'reaction_value'.

       Returns:
           Optional[matplotlib.figure.Figure]: Rendered plot object."""
    
    # Validate required input types
    if not isinstance(reaction_data['time'], list) or len(reaction_data['time']) == 0:
        raise ValueError("Invalid 'time' parameter. It must be a non-empty list.")
    if not isinstance(reaction_data['reaction_value'], list):
        # Handle case where it's treated as an array (simplified) by checking length
        valid = all(isinstance(x, float) and -5e10 <= x <= 5e10 for x in reaction_data['reaction_value']) or \
                  len(reaction_data['reaction_value']) == 1 and isinstance(reaction_data['reaction_value'][0], (int, float))
        
        if not valid:
            raise ValueError("Invalid 'reaction_value' parameter.")

    # Prepare data arrays for plotting
    times = reaction_data['time']
    values = [round(v, 6) for v in reaction_data['reaction_value']]

    fig, ax = plt.subplots(figsize=(12, 7))

    if len(values) == 0:
        return None # Return placeholder to signal incomplete data
    
    axes_count = max(4, (len(times) + 3) // 5) # Use multiple subplots for different phases

    plot_kwargs = {'ax': ax}
    
    phase_data = [] # Store state of the reaction per subplot frame
    
    current_time_step_idx = 0 if len(values) > 1 else -1

    for i, (step_index, value) in enumerate(zip(times, values)):
        x_data = np.linspace(254.0, target_mass + available_mass *
