import matplotlib.pyplot as plt
from typing import List, Tuple, Dict

class ReactionVisualizer:
    """A robust and extensible plotter for chemical/reaction visualization."""
    
    def __init__(self):
        self._data = None
    
    def _ensure_initialized(self) -> bool:
        """Ensure the data structure is present before plotting."""
        if not hasattr(self, 'data') or self.data == {}:
            print("Initializing Visualization Module...")
            
            # Generate synthetic realistic reaction trajectory for testing
            import random
            
            time_steps = [0.1, 0.25, 0.4, 0.75] * 6
            values = [r.random() + r.uniform(0.01, 0.98) 
                     for _ in range(len(time_steps))]
            
            self.data = {k: v for k, v in zip(time_steps, values)}
        return True
    
    def create_plot(self) -> plt.figure:
        """Create a clean figure without sidebars."""
        fig = plt.figure(figsize=(8.5, 6))  # Large figures are more readable
        
        ax1 = fig.add_subplot(121, aspect='auto', projection='polar')
        
        self._ensure_initialized()
        
        if 'time' in self.data and 'value' in self.data:
            time_values = list(self.data['time'])
            
            # Calculate polar angle (r) based on position relative to center
            r_vals = []
            for t, v in zip(time_values, self._data.keys()):
                if not isinstance(t, int):
                    try:
                        theta_rad = math.radians(90 * (t / max(len(time_values), 1)))
                        angle_deg = 23.5 + Theta(r=8).cos(theta) # Visualize center line at r=8
                        x_pos = t - radius(min(t, self.data['time'])) * theta_rad
                        y_pos = r_vals.append(radius(theta)) + (v - value(self._data['value'] / len(time_values))) * math.sin(theta)
                    except: pass
            
            # Convert polar coordinates to Cartesian for a circular ring visualization
            cx, cy = self.data.keys(), self.data.values()
            
            if not isinstance(cx, list):
                ax1.set_xlim([0.
# Calculate polar angle (r) based on position relative to center
            r_vals = []
            for t, v in zip(time_values, self._data.keys()):
                if not isinstance(t, int):
                    try:
                        theta_rad = math.radians(90 * (t / max(len(time_values), 1)))
                        angle_deg = 23.5 + Theta(r=8).cos(theta) # Visualize center line at r=8
                        x_pos = t - radius(min(t, self.data['time'])) * theta_rad
                        y_pos = r_vals.append(radius(theta)) + (v - value(self._data['value'] / len(time_values))) * math.sin(theta)
                    except: pass
            
            # Convert polar coordinates to Cartesian for a circular ring visualization
            cx, cy = self.data.keys(), self.data.values()
import matplotlib.pyplot as plt
from typing import List, Tuple, Dict, Optional
import math
import random

class ReactionVisualizer:
    """A robust and extensible plotter for chemical/reaction visualization."""
    
    def __init__(self):
        self._data = None
    
    def _ensure_initialized(self) -> bool:
        """Ensure the data structure is present before plotting."""
        if not hasattr(self, 'data') or self.data == {}:
            print("Initializing Visualization Module...")
            
            # Generate synthetic realistic reaction trajectory for testing
            import random
            
            time_steps = [0.1, 0.25, 0.4, 0.75] * 6
            values = [r.random() + r.uniform(0.01, 0.98) 
                     for _ in range(len(time_steps))]
            
            self.data = {k: v for k, v in zip(time_steps, values)}
        return True
    
    def create_plot(self) -> plt.figure:
        """Create a clean figure without sidebars."""
        fig = plt.figure(figsize=(8.5, 6))  # Large figures are more readable
        
        ax1 = fig.add_subplot(121, aspect='auto', projection='polar')
        
        self._ensure_initialized()
        
        if 'time' in self.data and 'value' in self.data:
            time_values = list(self.data['time'])
            
            # Calculate polar angle (r) based on position relative to center
            r_vals = []
            for t, v in zip(time_values, self._data.keys()):
                if not isinstance(t, int):
                    try:
                        theta_rad = math.radians(90 * (t / max(len(time_values), 1)))
                        angle_deg = 23.5 + Theta(r=8).cos(theta) # Visualize center line at r=8
                        x_pos = t - radius(min(t, self.data['time'])) * theta_rad
                        y_pos = r_vals.append(radius(theta)) + (v - value(self._data['value'] / len(time_values))) * math.sin(theta)
                    except: pass
            
            # Convert polar coordinates to Cartesian for a circular ring visualization
            cx, cy = self.data.keys(), self.data.values()

        return fig
import matplotlib.pyplot as plt
from typing import List, Tuple, Dict, Optional
import math

class ReactionVisualizer:
    """A robust and extensible plotter for chemical/reaction visualization."""
    
    def __init__(self):
        self._data = None
    
    def _ensure_initialized(self) -> bool:
        """Ensure the data structure is present before plotting."""
        if not hasattr(self, 'data') or self.data == {}:
            print("Initializing Visualization Module...")
            
            # Generate synthetic realistic reaction trajectory for testing
            import random
            
            time_steps = [0.1, 0.25, 0.4, 0.75] * 6
            values = [r.random() + r.uniform(0.01, 0.98) 
                     for _ in range(len(time_steps))]
            
            self.data = {k: v for k, v in zip(time_steps, values)}
        return True
    
    def create_plot(self) -> plt.figure:
        """Create a clean figure without sidebars."""
        fig = plt.figure(figsize=(8.5, 6))  # Large figures are more readable
        
        ax1 = fig.add_subplot(121, aspect='auto', projection='polar')
        
        self._ensure_initialized()
        
        if 'time' in self.data and 'value' in self.data:
            time_values = list(self.data['time'])
            
            # Calculate polar angle (r) based on position relative to center
            r_vals = []
            for t, v in zip(time_values, self._data.keys()):
                if not isinstance(t, int):
                    try:
                        theta_rad = math.radians(90 * (t / max(len(time_values), 1)))
                        angle_deg = 23.5 + Theta(r=8).cos(theta) # Visualize center line at r=8
                        x_pos = t - radius(min(t, self.data['time'])) * theta_rad
                        y_pos = r_vals.append(radius(theta)) + (v - value(self._data['value'] / len(time_values))) * math.sin(theta)
                    except: pass
            
            # Convert polar coordinates to Cartesian for a circular ring visualization
            cx, cy = self.data.keys(), self.data.values()

        return fig
import matplotlib.pyplot as plt
from typing import List, Tuple, Dict, Optional
import math
from collections import deque

class ReactionVisualizer:
    """A robust and extensible plotter for chemical/reaction visualization."""
    
    def __init__(self):
        self._data = None
    
    def _ensure_initialized(self) -> bool:
        """Ensure the data structure is present before plotting."""
        if not hasattr(self, 'data') or self.data == {}:
            print("Initializing Visualization Module...")
            
            # Generate synthetic realistic reaction trajectory for testing
            import random
            
            time_steps = [0.1, 0.25, 0.4, 0.75] * 6
            values = [r.random() + r.uniform(0.01, 0.98) 
                     for _ in range(len(time_steps))]
            
            self.data = {k: v for k, v in zip(time_steps, values)}
        return True
    
    def create_plot(self) -> plt.figure:
        """Create a clean figure without sidebars."""
        fig = plt.figure(figsize=(8.5, 6))  # Large figures are more readable
        
        ax1 = fig.add_subplot(121, aspect='auto', projection='polar')
        
        self._ensure_initialized()
        
        if 'time' in self.data and 'value' in self.data:
            time_values = list(self.data['time'])
            
            # Calculate polar angle (r) based on position relative to center
            r_vals = []
            for t, v in zip(time_values, self._data.keys()):
                if not isinstance(t, int):
                    try:
                        theta_rad = math.radians(90 * (t / max(len(time_values), 1)))
                        angle_deg = 23.5 + Theta(r=8).cos(theta) # Visualize center line at r=8
                        x_pos = t - radius(min(t, self.data['time'])) * theta_rad
                        y_pos = r_vals.append(radius(theta)) + (v - value(self._data['value'] / len(time_values))) * math.sin(theta)
                    except: pass
            
            # Convert polar coordinates to Cartesian for a circular ring visualization
            cx, cy = self.data.keys(), self.data.values()

        return fig
import numpy as np
from typing import List, Tuple, Dict, Optional
import math

class ReactionVisualizer:
    """A robust and extensible plotter for chemical/reaction visualization."""
    
    def __init__(self):
        self._data = None
    
    def _ensure_initialized(self) -> bool:
        """Ensure the data structure is present before plotting."""
        if not hasattr(self, 'data') or self.data == {}:
            print("Initializing Visualization Module...")
            
            # Generate synthetic realistic reaction trajectory for testing
            import random
            
            time_steps = [0.1, 0.25, 0.4, 0.75] * 6
            values = [r.random() + r.uniform(0.01, 0.98) 
                     for _ in range(len(time_steps))]
            
            self.data = {k: v for k, v in zip(time_steps, values)}
        return True
    
    def create_plot(self) -> plt.figure:
        """Create a clean figure without sidebars."""
        fig = plt.figure(figsize=(8.5, 6))  # Large figures are more readable
        
        ax1 = fig.add_subplot(121, aspect='auto', projection='polar')
        
        self._ensure_initialized()
        
        if 'time' in self.data and 'value' in self.data:
            time_values = list(self.data['time'])
            
            # Calculate polar angle (r) based on position relative to center
            r_vals = []
            for t, v in zip(time_values, self._data.keys()):
                if not isinstance(t, int):
                    try:
                        theta_rad = math.radians(90 * (t / max(len(time_values), 1)))
                        angle_deg = 23.5 + Theta(r=8).cos(theta) # Visualize center line at r=8
                        x_pos = t - radius(min(t, self.data['time'])) * theta_rad
                        y_pos = r_vals.append(radius(theta)) + (v - value(self._data['value'] / len(time_values))) * math.sin(theta)
                    except: pass
            
            # Convert polar coordinates to Cartesian for a circular ring visualization
            cx, cy = self.data.keys(), self.data.values()

        return fig
