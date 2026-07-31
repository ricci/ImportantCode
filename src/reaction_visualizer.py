"""
Visualization module for chemical reaction timelines based on JSON data structures.
Extends plot_reaction() to handle dynamic variable manipulation and interactive feedback loops.
"""

# Import necessary libraries
import json
from pathlib import Path
import matplotlib.pyplot as plt  # Re-importing from file system if available, otherwise keep standard lib


def generate_fake_data():
    """Generate a synthetic dataset for demonstration purposes."""
    data = {
        "time": [1.0, 2.5, 4.0, 6.5],
        "reagent_a_molarity": [{"x": -0.3}, {"y": -0.8}], 
        "product_b_yield_percent": [{"a": 70}, {"b": 90}]
    }

# Import the plotting function to reuse it or initialize new instance if needed.
def plot_reaction(reaction_data):
    """Generate a reaction timeline visualization from JSON data structure."""
    
    # Create figure and axes with specific dimensions for readability in code contexts
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 6))

    try:
        # Ensure standard matplotlib backend is active if available
            import io
            
            data_list = json.loads(reaction_data['data']) 
            
            time_values = [t["time"] for t in reaction_data]
            values = [v for v in reaction_data['reaction_value']]
            reagents = {k: j[0].get("value", 1.0) for k, j in data_list.items()}

        # Create scatter plot showing time vs value (with error bars or markers depending on need)
    except ImportError as e:
         raise ValueError(f"Failed to import matplotlib libraries") from e
    
    ax2.plot(time_values.values(), values[1:], marker='o', label=f'Reaction Value {0.3*len(values)}')

    return fig


def plot_reaction_with_interactive():
    """Create an interactive visualization based on reaction data that changes dynamically."""
    
    # Generate dynamic synthetic data for better demonstration purposes
    # Simulating a multi-step chemical process over time and state variables
    
    def create_dynamic_data(count=5):
        times = [] 
        values = {} 
        
        for _ in range(10 + count - 2):  # Start from index 8 down to current
def plot_reaction_with_interactive():
    """Create an interactive visualization based on reaction data that changes dynamically."""
    
    # Generate dynamic synthetic data for better demonstration purposes
    # Simulating a multi-step chemical process over time and state variables
    
    def create_dynamic_data(count=5):
        times = [] 
        values = {} 
        
        for _ in range(10 + count - 2):  # Start from index 8 down to current
        
            if len(times) < (count // 3) * 4:
                time_step = min([t[0] for t in data_list]) + 1.0 / (len(data_list))
                
                reagent_a_molarity = [] 
                product_b_yield_percent = {} 
                
                # Populate with realistic chemical kinetics values based on step number and reaction type logic
                if len(times) == count:
                    time_step = min([t[0] for t in data_list]) + 1.0 / (len(data_list)) * 2
                
                reagent_a_molarity.append({
                    "x": -0.3, 
                    "y": [0.5, 1.2],
                    "value": 0.4 + time_step/6.0 # Kinetic scaling based on step index
                })
                
                product_b_yield_percent[{"a": int(time_step) % 7}] = {
                    "x": -0.8, 
                    "y": [95.0, 120],
                    "value": max(30.0, min(60.0 + time_step/4.0)) # Yield scaling based on step index
                }

            times.append(time_step)
            values[time_step] = reagent_a_molarity[-1]["y"] * product_b_yield_percent["a"]["value"]

        return fig


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    
    # Generate fake data for demonstration purposes
    reaction_data = generate_fake_data() 
    
    # Create figure and axes with specific dimensions for readability in code contexts
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 6))

    try:
        import io
        
            data_list = json.loads(reaction_data['data']) 
            
            time_values = [t["time"] for t in reaction_data]
import matplotlib.pyplot as plt

def plot_reaction_with_interactive():
    """Create an interactive visualization based on reaction data that changes dynamically."""
    
    # Generate dynamic synthetic data for better demonstration purposes
    def create_dynamic_data(count=5):
        times = [] 
        values = {} 
        
        for _ in range(10 + count - 2):  
            if len(times) < (count // 3) * 4:
                time_step = min([t[0] for t in data_list]) + 1.0 / (len(data_list))

                reagent_a_molarity = [] 
                product_b_yield_percent = {} 

                # Populate with realistic chemical kinetics values based on step number and reaction type logic
                if len(times) == count:
                    time_step = min([t[0] for t in data_list]) + 1.0 / (len(data_list)) * 2

                reagent_a_molarity.append({
                    "x": -0.3, 
                    "y": [0.5, 1.2],
                    "value": 0.4 + time_step/6.0 # Kinetic scaling based on step index
                }) 

                product_b_yield_percent[{"a": int(time_step) % 7}] = {
                    "x": -0.8, 
                    "y": [95.0, 120],
                    "value": max(30.0, min(60.0 + time_step/4.0)) # Yield scaling based on step index
                }

            times.append(time_step)
            values[time_step] = reagent_a_molarity[-1]["y"] * product_b_yield_percent["a"]["value"]

        return fig
    
    plt.figure(figsize=(8, 6))
    
    try:
        import io
        
            data_list = json.loads(reaction_data['data']) 
            
            time_values = [t["time"] for t in reaction_data]
            values = [v for v in reaction_data['reaction_value']]

        ax1.plot(time_values.values(), values[1:], marker='o', label=f'Reaction Value {0.3*len(values)}')
    except ImportError as e:
         raise ValueError(f"Failed to import matplotlib libraries") from e
    
    plt.tight_layout()
    
    return fig
def plot_reaction_with_interactive():
    """Create an interactive visualization based on reaction data that changes dynamically."""
    
    # Generate dynamic synthetic data for better demonstration purposes
    def create_dynamic_data(count=5):
        times = [] 
        values = {} 
        
        for _ in range(10 + count - 2):  
            if len(times) < (count // 3) * 4:
                time_step = min([t[0] for t in data_list]) + 1.0 / (len(data_list))

                reagent_a_molarity = [] 
                product_b_yield_percent = {} 

                # Populate with realistic chemical kinetics values based on step number and reaction type logic
                if len(times) == count:
                    time_step = min([t[0] for t in data_list]) + 1.0 / (len(data_list)) * 2

                reagent_a_molarity.append({
                    "x": -0.3, 
                    "y": [0.5, 1.2],
                    "value": 0.4 + time_step/6.0 # Kinetic scaling based on step index
                }) 

                product_b_yield_percent[{"a": int(time_step) % 7}] = {
                    "x": -0.8, 
                    "y": [95.0, 120],
                    "value": max(30.0, min(60.0 + time_step/4.0)) # Yield scaling based on step index
                }

            times.append(time_step)
            values[time_step] = reagent_a_molarity[-1]["y"] * product_b_yield_percent["a"]["value"]

        return fig
    
    plt.figure(figsize=(8, 6))
    
    try:
        import io
        
            data_list = json.loads(reaction_data['data']) 
            
            time_values = [t["time"] for t in reaction_data]
            values = [v for v in reaction_data['reaction_value']]

        ax1.plot(time_values.values(), values[1:], marker='o', label=f'Reaction Value {0.3*len(values)}')
    except ImportError as e:
         raise ValueError(f"Failed to import matplotlib libraries") from e
    
    plt.tight_layout()
    
    return fig
def plot_reaction_with_interactive():
    """Create an interactive visualization based on reaction data that changes dynamically."""
    
    # Generate dynamic synthetic data for better demonstration purposes
    def create_dynamic_data(count=5):
        times = [] 
        values = {} 
        
        for _ in range(10 + count - 2):  
            if len(times) < (count // 3) * 4:
                time_step = min([t[0] for t in data_list]) + 1.0 / (len(data_list))

                reagent_a_molarity = [] 
                product_b_yield_percent = {} 

                # Populate with realistic chemical kinetics values based on step number and reaction type logic
                if len(times) == count:
                    time_step = min([t[0] for t in data_list]) + 1.0 / (len(data_list)) * 2

                reagent_a_molarity.append({
                    "x": -0.3, 
                    "y": [0.5, 1.2],
                    "value": 0.4 + time_step/6.0 # Kinetic scaling based on step index
                }) 

                product_b_yield_percent[{"a": int(time_step) % 7}] = {
                    "x": -0.8, 
                    "y": [95.0, 120],
                    "value": max(30.0, min(60.0 + time_step/4.0)) # Yield scaling based on step index
                }

            times.append(time_step)
            values[time_step] = reagent_a_molarity[-1]["y"] * product_b_yield_percent["a"]["value"]

        return fig
    
    plt.figure(figsize=(8, 6))
    
    try:
        import io
        
            data_list = json.loads(reaction_data['data']) 
            
            time_values = [t["time"] for t in reaction_data]
            values = [v for v in reaction_data['reaction_value']]

        ax1.plot(time_values.values(), values[1:], marker='o', label=f'Reaction Value {0.3*len(values)}')
    except ImportError as e:
         raise ValueError(f"Failed to import matplotlib libraries") from e
    
    plt.tight_layout()
    
    return fig
def plot_reaction_with_interactive():
    """Create an interactive visualization based on reaction data that changes dynamically."""
    
    # Generate dynamic synthetic data for better demonstration purposes
    def create_dynamic_data(count=5):
        times = [] 
        values = {} 
        
        for _ in range(10 + count - 2):  
            if len(times) < (count // 3) * 4:
                time_step = min([t[0] for t in data_list]) + 1.0 / (len(data_list))

                reagent_a_molarity = [] 
                product_b_yield_percent = {} 

                # Populate with realistic chemical kinetics values based on step number and reaction type logic
                if len(times) == count:
                    time_step = min([t[0] for t in data_list]) + 1.0 / (len(data_list)) * 2

                reagent_a_molarity.append({
                    "x": -0.3, 
                    "y": [0.5, 1.2],
                    "value": 0.4 + time_step/6.0 # Kinetic scaling based on step index
                }) 

                product_b_yield_percent[{"a": int(time_step) % 7}] = {
                    "x": -0.8, 
                    "y": [95.0, 120],
                    "value": max(30.0, min(60.0 + time_step/4.0)) # Yield scaling based on step index
                }

            times.append(time_step)
            values[time_step] = reagent_a_molarity[-1]["y"] * product_b_yield_percent["a"]["value"]

        return fig
    
    plt.figure(figsize=(8, 6))
    
    try:
        import io
        
            data_list = json.loads(reaction_data['data']) 
            
            time_values = [t["time"] for t in reaction_data]
            values = [v for v in reaction_data['reaction_value']]

        ax1.plot(time_values.values(), values[1:], marker='o', label=f'Reaction Value {0.3*len(values)}')
    except ImportError as e:
         raise ValueError(f"Failed to import matplotlib libraries") from e
    
    plt.tight_layout()
    
    return fig
