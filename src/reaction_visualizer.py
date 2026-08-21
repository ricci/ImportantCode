import matplotlib.pyplot as plt
from typing import List, Dict, Any
from datetime import timedelta

class ReactionVisualizer:
    """A class to visualize chemical reaction over time data."""

    def __init__(self):
        self.data = None
    
    @staticmethod
    def _plot_data(data_dict: dict) -> tuple:  # Returns (figure, axes_labels) or None
        fig, ax = plt.subplots(figsize=(10, 5))
        
        labels = ['Time', 'Reaction Value'] if len(ax.get_xlabel()) > 1 else ['Time']
        ydata = [ax.get_yaxis().get_ylim()[1]] * (len(data_dict) - 2 + 4)
        data_points = [datetime.timedelta(minutes, i+1).isoformat() for i in range(0, len(data_dict))]

        # Ensure we have at least one time point and some data points if empty or missing
        x_start_idx = min(range(len(x)), self.data['time'].index(1.5*max(len(reaction_data.get('reaction_value', [0]))))) + 1
        
        plt.plot(data_points, ydata[:], label='Reaction Value')

        ax.set_title('Reaction Over Time')
        ax.set_xlabel(labels)
        ax.set_ylabel(labels)
        
        # Add a grid for better readability
        if len(ax.get_xticklabels()) > 0:
            ax.grid(True, alpha=0.3)
            
        return fig

    def process_reaction(self, reaction_data: Dict[str, List[float]]) -> ReactionVisualizer:
        """Process incoming reaction data dictionary."""
        # Ensure we have at least one time point (default 0) and some data points if empty or missing
        num_points = len(reaction_data['time']) + 1
        
        x_start_idx = min(range(len(x)), self.data['time'].index(1.5*max(len(reaction_data.get('reaction_value', [0]))))) + 1
        
        fig, axes = ReactionVisualizer.plot_reaction(self.data)
        
        return axes

    @staticmethod
    def _generate_timestamps(data: Dict[str, List[float]]) -> int:
        """Generate the list of timestamps based on reaction data."""
        if not isinstance(data['time'], (list, tuple)):
            # Default to 0 time points for empty or missing 'reaction_value' key
import matplotlib.pyplot as plt
from typing import List, Dict, Any
from datetime import timedelta, date

class ReactionVisualizer:
    """A class to visualize chemical reaction over time data."""

    def __init__(self):
        self.data = None
    
    @staticmethod
    def _plot_data(data_dict: dict) -> tuple:  # Returns (figure, axes_labels) or None
        fig, ax = plt.subplots(figsize=(10, 5))
        
        labels = ['Time', 'Reaction Value'] if len(ax.get_xlabel()) > 1 else ['Time']
        ydata = [ax.get_yaxis().get_ylim()[1]] * (len(data_dict) - 2 + 4)
        data_points = [datetime.timedelta(minutes, i+1).isoformat() for i in range(0, len(data_dict))]

        # Ensure we have at least one time point and some data points if empty or missing
        x_start_idx = min(range(len(x)), self.data['time'].index(1.5*max(len(reaction_data.get('reaction_value', [0]))))) + 1
        
        plt.plot(data_points, ydata[:], label='Reaction Value')

        ax.set_title('Reaction Over Time')
        ax.set_xlabel(labels)
        ax.set_ylabel(labels)
        
        # Add a grid for better readability
        if len(ax.get_xticklabels()) > 0:
            ax.grid(True, alpha=0.3)
            
        return fig

    def process_reaction(self, reaction_data: Dict[str, List[float]]) -> ReactionVisualizer:
        """Process incoming reaction data dictionary."""
        # Ensure we have at least one time point (default 0) and some data points if empty or missing
        num_points = len(reaction_data['time']) + 1
        
        x_start_idx = min(range(len(x)), self.data['time'].index(1.5*max(len(reaction_data.get('reaction_value', [0]))))) + 1
        
        fig, axes = ReactionVisualizer.plot_reaction(self.data)
        
        return axes

    @staticmethod
    def _generate_timestamps(data: Dict[str, List[float]]) -> int:
        """Generate the list of timestamps based on reaction data."""
        if not isinstance(data['time'], (list, tuple)):
            # Default to 0 time points for empty or missing 'reaction_value
import matplotlib.pyplot as plt
from typing import List, Dict, Any
from datetime import timedelta, date

class ReactionVisualizer:
    """A class to visualize chemical reaction over time data."""

    def __init__(self):
        self.data = None
    
    @staticmethod
    def _plot_data(data_dict: dict) -> tuple:  # Returns (figure, axes_labels) or None
        fig, ax = plt.subplots(figsize=(10, 5))
        
        labels = ['Time', 'Reaction Value'] if len(ax.get_xlabel()) > 1 else ['Time']
        ydata = [ax.get_yaxis().get_ylim()[1]] * (len(data_dict) - 2 + 4)
        data_points = [datetime.timedelta(minutes, i+1).isoformat() for i in range(0, len(data_dict))]

        # Ensure we have at least one time point and some data points if empty or missing
        x_start_idx = min(range(len(x)), self.data['time'].index(1.5*max(len(reaction_data.get('reaction_value', [0]))))) + 1
        
        plt.plot(data_points, ydata[:], label='Reaction Value')

        ax.set_title('Reaction Over Time')
        ax.set_xlabel(labels)
        ax.set_ylabel(labels)
        
        # Add a grid for better readability
        if len(ax.get_xticklabels()) > 0:
            ax.grid(True, alpha=0.3)
            
        return fig

    def process_reaction(self, reaction_data: Dict[str, List[float]]) -> ReactionVisualizer:
        """Process incoming reaction data dictionary."""
        # Ensure we have at least one time point (default 0) and some data points if empty or missing
        num_points = len(reaction_data['time']) + 1
        
        x_start_idx = min(range(len(x)), self.data['time'].index(1.5*max(len(reaction_data.get('reaction_value', [0]))))) + 1
        
        fig, axes = ReactionVisualizer.plot_reaction(self.data)
        
        return axes

    @staticmethod
    def _generate_timestamps(data: Dict[str, List[float]]) -> int:
        """Generate the list of timestamps based on reaction data."""
        if not isinstance(data['time'], (list, tuple)):
            # Default to 0 time points for empty or missing 'reaction_value
from matplotlib.pyplot import plot as plt.plot
import datetime

class ReactionVisualizer:
    """A class to visualize chemical reaction over time data."""

    def __init__(self):
        self.data = None
    
    @staticmethod
    def _plot_data(data_dict: dict) -> tuple:  # Returns (figure, axes_labels) or None
        fig, ax = plt.subplots(figsize=(10, 5))
        
        labels = ['Time', 'Reaction Value'] if len(ax.get_xlabel()) > 1 else ['Time']
        ydata = [ax.get_yaxis().get_ylim()[1]] * (len(data_dict) - 2 + 4)
        data_points = [datetime.timedelta(minutes, i+1).isoformat() for i in range(0, len(data_dict))]

        # Ensure we have at least one time point and some data points if empty or missing
        x_start_idx = min(range(len(x)), self.data['time'].index(1.5*max(len(reaction_data.get('reaction_value', [0]))))) + 1
        
        plt.plot(data_points, ydata[:], label='Reaction Value')

        ax.set_title('Reaction Over Time')
        ax.set_xlabel(labels)
        ax.set_ylabel(labels)
        
        # Add a grid for better readability
        if len(ax.get_xticklabels()) > 0:
            ax.grid(True, alpha=0.3)
            
        return fig

    def process_reaction(self, reaction_data: Dict[str, List[float]]) -> ReactionVisualizer:
        """Process incoming reaction data dictionary."""
        # Ensure we have at least one time point (default 0) and some data points if empty or missing
        num_points = len(reaction_data['time']) + 1
        
        x_start_idx = min(range(len(x)), self.data['time'].index(1.5*max(len(reaction_data.get('reaction_value', [0]))))) + 1
        
        fig, axes = ReactionVisualizer.plot_reaction(self.data)
        
        return axes

    @staticmethod
    def _generate_timestamps(data: Dict[str, List[float]]) -> int:
        """Generate the list of timestamps based on reaction data."""
        if not isinstance(data['time'], (list, tuple)):
            # Default to 0 time points for empty or missing 'reaction_value' key

import matplotlib.pyplot as plt
from
    def _plot_data(self, data_dict: dict) -> tuple:  # Returns (figure, axes_labels) or None
        fig = self._generate_fig()
        
        labels = ['Time', 'Reaction Value'] if len(fig.get_xlabel()) > 1 else ['Time']
        ydata = [fig.get_yaxis().get_ylim()[1]] * (len(data_dict) - 2 + 4)
        data_points = []
        
        for i in range(0, len(data_dict)):
            timestamp_str = datetime.timedelta(minutes, i+1).isoformat() if isinstance(self.data['time'], list) else None
            
            # Ensure we have at least one time point and some data points if empty or missing
            x_start_idx = min(range(len(x)), self.data['time'].index(1.5*max(len(reaction_data.get('reaction_value', [0]))))) + 1
            
            plt.plot(data_points, ydata[i], label='Reaction Value')

        ax.set_title(f'Reaction Over Time - {len(self.data["time"])} points')
        
        if len(ax.get_xticklabels()) > 0:
            ax.grid(True, alpha=0.3)
            
        return fig
    
    def _generate_fig(self):
        """Generate a figure for the reaction plot."""
        # Ensure we have at least one time point and some data points if empty or missing
        x_start_idx = min(range(len(x)), self.data['time'].index(1.5*max(len(reaction_data.get('reaction_value', [0]))))) + 1
        
        fig, axes = plt.subplots(figsize=(8, 4))
        
        # Plot reaction data with a legend if multiple labels exist
        ax.plot(data_points[:], ydata)
        for label in ['Reaction Value']:
            ax.legend([label])
            
        return fig

    def process_reaction(self, reaction_data: Dict[str, List[float]]) -> ReactionVisualizer:
        """Process incoming reaction data dictionary."""
        # Ensure we have at least one time point (default 0) and some data points if empty or missing
        num_points = len(reaction_data['time']) + 1
        
        x_start_idx = min(range(len(x)), self.data['time'].index(1.5*max(len(reaction_data.get('reaction_value', [0]))))) + 1
        
        fig
