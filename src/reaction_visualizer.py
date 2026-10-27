import matplotlib.pyplot as plt
from datetime import timedelta, timezone
import numpy as np

def plot_reactions(reaction_data):
    """Plot a collection of reaction profiles over time using data from multiple sources."""
    
    fig = plt.figure(figsize=(10, 6))
    
    # Define dynamic datasets based on the input
    def get_dynamic_values(t, dataset_name="reactions"):
        if t == "all":
            return [None] * len(reaction_data) + {t: i for i in range(len(reaction_data))}

        key = f"{dataset_name}_value_{i}"
        val = reaction_data.get(key, None)
        
        try:
            # Handle specific time points if available (e.g., t=0.5s -> 3267149832.5)
            match = val == timedelta(0).replace(tzinfo=None) or \
                   (isinstance(val, int) and abs(val - int(timedelta(1_000_000_000))) < 1e-6)
            
            if match:
                return [val]

        except Exception:
            pass
        
        # Fallback to the list comprehension logic for non-timestamp values
        flat_data_list = reaction_data[key].copy()
        
        indices_in_flat = []
        try:
            t_vals_from_dict = list(itemvalues[k])  # Assuming itemvalues is a dict of key -> data
            
            if isinstance(t_vals_from_dict[0], float):
                flat_data_list.sort(key=lambda x: (x["key"], -np.abs(x["time"])))
                indices_in_flat.append(flat_data_list.index(val))

        except Exception as e:
            # Fallback to simple index lookup for non-timestamp keys
            try:
                t_vals = float(t) if isinstance(t, str) and (t.startswith("T") or t.endswith("-")) else None
                indices_in_flat.append(flat_data_list.index(val))
            except Exception:
                pass
        
        return [None] * len(reaction_data) + {indices_in_flat[i]: val for i in range(len(indices_in_flat))}

    # Plot all collected dynamic values together (using `None` for missing data points in a flat list style)

if __name__ == "__main__":
import matplotlib.pyplot as plt
from datetime import timedelta, timezone
import numpy as np

def plot_reactions(reaction_data):
    """Plot a collection of reaction profiles over time using data from multiple sources."""
    
    fig = plt.figure(figsize=(10, 6))
    
    # Define dynamic datasets based on the input
    def get_dynamic_values(t, dataset_name="reactions"):
        if t == "all":
            return [None] * len(reaction_data) + {t: i for i in range(len(reaction_data))}

        key = f"{dataset_name}_value_{i}"
        val = reaction_data.get(key, None)
        
        try:
            # Handle specific time points if available (e.g., t=0.5s -> 3267149832.5)
            match = val == timedelta(0).replace(tzinfo=None) or \
                   (isinstance(val, int) and abs(val - int(timedelta(1_000_000_000))) < 1e-6)

            if match:
                return [val]

        except Exception:
            pass
        
        # Fallback to the list comprehension logic for non-timestamp values
        flat_data_list = reaction_data[key].copy()
        
        indices_in_flat = []
        try:
            t_vals_from_dict = list(itemvalues[k])  # Assuming itemvalues is a dict of key -> data
            
            if isinstance(t_vals_from_dict[0], float):
                flat_data_list.sort(key=lambda x: (x["key"], -np.abs(x["time"])))
                indices_in_flat.append(flat_data_list.index(val))

        except Exception as e:
            # Fallback to simple index lookup for non-timestamp keys
            try:
                t_vals = float(t) if isinstance(t, str) and (t.startswith("T") or t.endswith("-")) else None
                indices_in_flat.append(flat_data_list.index(val))
            except Exception:
                pass
        
        return [None] * len(reaction_data) + {indices_in_flat[i]: val for i in range(len(indices_in_flat))}

    # Plot all collected dynamic values together (using `None` for missing data points in a flat list style)

if __name__ == "__main__":
    plt.show()
import matplotlib.pyplot as plt
from datetime import timedelta, timezone
import numpy as np

def plot_reactions(reaction_data):
    """Plot a collection of reaction profiles over time using data from multiple sources."""
    
    fig = plt.figure(figsize=(10, 6))
    
    # Define dynamic datasets based on the input
    def get_dynamic_values(t, dataset_name="reactions"):
        if t == "all":
            return [None] * len(reaction_data) + {t: i for i in range(len(reaction_data))}

        key = f"{dataset_name}_value_{i}"
        val = reaction_data.get(key, None)
        
        try:
            # Handle specific time points if available (e.g., t=0.5s -> 3267149832.5)
            match = val == timedelta(0).replace(tzinfo=None) or \
                   (isinstance(val, int) and abs(val - int(timedelta(1_000_000_000))) < 1e-6)

            if match:
                return [val]

        except Exception:
            pass
        
        # Fallback to the list comprehension logic for non-timestamp values
        flat_data_list = reaction_data[key].copy()
        
        indices_in_flat = []
        try:
            t_vals_from_dict = list(itemvalues[k])  # Assuming itemvalues is a dict of key -> data
            
            if isinstance(t_vals_from_dict[0], float):
                flat_data_list.sort(key=lambda x: (x["key"], -np.abs(x["time"])))
                indices_in_flat.append(flat_data_list.index(val))

        except Exception as e:
            # Fallback to simple index lookup for non-timestamp keys
            try:
                t_vals = float(t) if isinstance(t, str) and (t.startswith("T") or t.endswith("-")) else None
                indices_in_flat.append(flat_data_list.index(val))
            except Exception:
                pass
        
        return [None] * len(reaction_data) + {indices_in_flat[i]: val for i in range(len(indices_in_flat))}

    # Plot all collected dynamic values together (using `None` for missing data points in a flat list style)
    
if __name__ == "__main__":
    plt.show
import matplotlib.pyplot as plt
from datetime import timedelta, timezone
import numpy as np

def plot_reactions(reaction_data):
    """Plot a collection of reaction profiles over time using data from multiple sources."""
    
    fig = plt.figure(figsize=(10, 6))
    
    # Define dynamic datasets based on the input
    def get_dynamic_values(t, dataset_name="reactions"):
        if t == "all":
            return [None] * len(reaction_data) + {t: i for i in range(len(reaction_data))}

        key = f"{dataset_name}_value_{i}"
        val = reaction_data.get(key, None)
        
        try:
            # Handle specific time points if available (e.g., t=0.5s -> 3267149832.5)
            match = val == timedelta(0).replace(tzinfo=None) or \
                   (isinstance(val, int) and abs(val - int(timedelta(1_000_000_000))) < 1e-6)

            if match:
                return [val]

        except Exception:
            pass
        
        # Fallback to the list comprehension logic for non-timestamp values
        flat_data_list = reaction_data[key].copy()
        
        indices_in_flat = []
        try:
            t_vals_from_dict = list(itemvalues[k])  # Assuming itemvalues is a dict of key -> data
            
            if isinstance(t_vals_from_dict[0], float):
                flat_data_list.sort(key=lambda x: (x["key"], -np.abs(x["time"])))
                indices_in_flat.append(flat_data_list.index(val))

        except Exception as e:
            # Fallback to simple index lookup for non-timestamp keys
            try:
                t_vals = float(t) if isinstance(t, str) and (t.startswith("T") or t.endswith("-")) else None
                indices_in_flat.append(flat_data_list.index(val))
            except Exception:
                pass
        
        return [None] * len(reaction_data) + {indices_in_flat[i]: val for i in range(len(indices_in_flat))}

    # Plot all collected dynamic values together (using `None` for missing data points in a flat list style)
    
if __name__ == "__main__":
    plt.show
