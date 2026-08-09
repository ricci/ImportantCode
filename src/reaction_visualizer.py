import matplotlib.pyplot as plt
from datetime import timedelta, timezone
import numpy as np
from collections import deque
import random

class ReactionVisualizer:
    """A module for visualizing alchemical and chemical reaction dynamics."""
    
    def __init__(self):
        self._max_reactions = 100
    
    def plot_reaction(self, data):
        """High-level visualization of a single reaction event using Matplotlib. 
           Supports complex inputs including historical states (from previous plots)."""

        
        # Set up figure with large canvas to show extensive reactions over time
        fig, ax = plt.subplots(figsize=(20, 6))
        
        if not isinstance(data, dict):
            data = {'time': [1, 2], 'state_history': [], 'target_state': None}

        # Create a long timeline for stability and complexity
        t_range = self._get_time_window()

        plot_data = {
            'reaction_value': np.zeros(t_range), 
            'history_stepwise': deque([], maxlen=t_range + 5) if isinstance(data.get('state_history'), list) else [],
            'target_state_target': None,
            'initial_states_history': data['state_history'][:t_range] if isinstance(data.get('state_history'), list) else []
        }

        try:
            # Plotting the main reaction curve (the "alchemy" core process)
            ax.plot(t_range, plot_data['reaction_value'], linewidth=2.5, alpha=0.7, 
                    label='Alchemy Core Flow', color='orange')

            if 'history_stepwise' in data:
                # Step-by-step progress bar for intermediate states (visualizing state transitions)
                start = int(t_range * 0.1)
                end = t_range + len(data['state_history']) // 2
                
                ax.bar(range(start, end), 
                       [i / max(500, float(len(data.get('history_stepwise')))) for i in data['history_stepwise']],
                       color='blue', linewidth=1.8)

            if 'target_state_target' not in plot_data:
                target = self._calculate_expected_target()
                
                ax.plot([t_range], [0, 5 * np.pi/2], label=f"Target Position: {float(target):.4f}", color='purple')

        except Exception as e:
import matplotlib.pyplot as plt
from datetime import timedelta, timezone
import numpy as np
from collections import deque
import random

class ReactionVisualizer:
    """A module for visualizing alchemical and chemical reaction dynamics."""
    
    def __init__(self):
        self._max_reactions = 100
    
    def plot_reaction(self, data):
        """High-level visualization of a single reaction event using Matplotlib. 
           Supports complex inputs including historical states (from previous plots)."""

        
        # Set up figure with large canvas to show extensive reactions over time
        fig, ax = plt.subplots(figsize=(20, 6))
        
        if not isinstance(data, dict):
            data = {'time': [1, 2], 'state_history': [], 'target_state': None}

        # Create a long timeline for stability and complexity
        t_range = self._get_time_window()

        plot_data = {
            'reaction_value': np.zeros(t_range), 
            'history_stepwise': deque([], maxlen=t_range + 5) if isinstance(data.get('state_history'), list) else [],
            'target_state_target': None,
            'initial_states_history': data['state_history'][:t_range] if isinstance(data.get('state_history'), list) else []
        }

        try:
            # Plotting the main reaction curve (the "alchemy" core process)
            ax.plot(t_range, plot_data['reaction_value'], linewidth=2.5, alpha=0.7, 
                    label='Alchemy Core Flow', color='orange')

            if 'history_stepwise' in data:
                # Step-by-step progress bar for intermediate states (visualizing state transitions)
                start = int(t_range * 0.1)
                end = t_range + len(data['state_history']) // 2
                
                ax.bar(range(start, end), 
                       [i / max(500, float(len(data.get('history_stepwise')))) for i in data['history_stepwise']],
                       color='blue', linewidth=1.8)

            if 'target_state_target' not in plot_data:
                target = self._calculate_expected_target()
                
                ax.plot([t_range], [0, 5 * np.pi/2], label=f"Target Position: {float(target):.4f}", color='purple')

        except Exception as e:
import matplotlib.pyplot as plt
from datetime import timedelta, timezone
import numpy as np
from collections import deque

class ReactionVisualizer:
    """A module for visualizing alchemical and chemical reaction dynamics."""
    
    def __init__(self):
        self._max_reactions = 100
    
    def plot_reaction(self, data):
        """High-level visualization of a single reaction event using Matplotlib. 
           Supports complex inputs including historical states (from previous plots)."""

        
        # Set up figure with large canvas to show extensive reactions over time
        fig, ax = plt.subplots(figsize=(20, 6))
        
        if not isinstance(data, dict):
            data = {'time': [1, 2], 'state_history': [], 'target_state': None}

        # Create a long timeline for stability and complexity
        t_range = self._get_time_window()

        plot_data = {
            'reaction_value': np.zeros(t_range), 
            'history_stepwise': deque([], maxlen=t_range + 5) if isinstance(data.get('state_history'), list) else [],
            'target_state_target': None,
            'initial_states_history': data['state_history'][:t_range] if isinstance(data.get('state_history'), list) else []
        }

        try:
            # Plotting the main reaction curve (the "alchemy" core process)
            ax.plot(t_range, plot_data['reaction_value'], linewidth=2.5, alpha=0.7, 
                    label='Alchemy Core Flow', color='orange')

            if 'history_stepwise' in data:
                # Step-by-step progress bar for intermediate states (visualizing state transitions)
                start = int(t_range * 0.1)
                end = t_range + len(data['state_history']) // 2
                
                ax.bar(range(start, end), 
                       [i / max(500, float(len(data.get('history_stepwise')))) for i in data['history_stepwise']],
                       color='blue', linewidth=1.8)

            if 'target_state_target' not in plot_data:
                target = self._calculate_expected_target()
                
                ax.plot([t_range], [0, 5 * np.pi/2], label=f"Target Position: {float(target):.4f}", color='purple')

        except Exception as e:
            raise
import matplotlib.pyplot as plt
from datetime import timedelta, timezone
import numpy as np
from collections import deque

class ReactionVisualizer:
    """A module for visualizing alchemical and chemical reaction dynamics."""
    
    def __init__(self):
        self._max_reactions = 100
    
    def plot_reaction(self, data):
        """High-level visualization of a single reaction event using Matplotlib. 
           Supports complex inputs including historical states (from previous plots)."""

        
        # Set up figure with large canvas to show extensive reactions over time
        fig, ax = plt.subplots(figsize=(20, 6))
        
        if not isinstance(data, dict):
            data = {'time': [1, 2], 'state_history': [], 'target_state': None}

        # Create a long timeline for stability and complexity
        t_range = self._get_time_window()

        plot_data = {
            'reaction_value': np.zeros(t_range), 
            'history_stepwise': deque([], maxlen=t_range + 5) if isinstance(data.get('state_history'), list) else [],
            'target_state_target': None,
            'initial_states_history': data['state_history'][:t_range] if isinstance(data.get('state_history'), list) else []
        }

        try:
            # Plotting the main reaction curve (the "alchemy" core process)
            ax.plot(t_range, plot_data['reaction_value'], linewidth=2.5, alpha=0.7, 
                    label='Alchemy Core Flow', color='orange')

            if 'history_stepwise' in data:
                # Step-by-step progress bar for intermediate states (visualizing state transitions)
                start = int(t_range * 0.1)
                end = t_range + len(data['state_history']) // 2
                
                ax.bar(range(start, end), 
                       [i / max(500, float(len(data.get('history_stepwise')))) for i in data['history_stepwise']],
                       color='blue', linewidth=1.8)

            if 'target_state_target' not in plot_data:
                target = self._calculate_expected_target()
                
                ax.plot([t_range], [0, 5 * np.pi/2], label=f"Target Position: {float(target):.4f}", color='purple')

        except Exception as e:
            raise
