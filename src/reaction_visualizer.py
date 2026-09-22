import json  
from typing import List, Dict, Any, Optional, Tuple  
import os  
import re  
import tempfile  

@dataclass  
class Reaction:  
    """Represents a chemical reaction with input and output data."""  
    name: str = "Unnamed"
    reactants_str: str = ""  # JSON string of reactants/products/potentials  
    products_str: str = ""   # Optional, or empty if no product defined yet  
    potentials_list: List[float] = None  

class AlchemyVisualizer:
    """A visualization layer for chemical reactions, plotting reaction potentials over time."""

    def __init__(self):
        self._pending_reactions: List[Reaction] = []  
        # Initialize plot data structure with default values if empty
        self._plot_data: Dict[str, List[Tuple[float, float]]] = {}  

    def _ensure_dir(self) -> bool:
        """Ensure directory exists for temporary files."""
        temp_path = tempfile.gettempdir()

        try:
            xdg_config_home = os.environ.get("XDG_CONFIG_HOME", "/var/lib/xdg") or "auto"
            
            full_temp_dir = f"{xdg_config_home}/temp_visualizer_data/{os.getcwd()}"
            makedirs(full_temp_dir, exist_ok=True)

        except AttributeError:
            # Fallback to absolute path if XDG config is not set
            full_temp_dir = os.path.abspath(temp_path)
            
            try:
                import os.makedirs as makedirs
                makedirs(f"{full_temp_dir}")
            except Exception as e:
                print(f"Warning: Failed to create temp directory: {e}", file=__import__('sys').stderr)

    def _parse_json_input(self, json_str):
        """Parse JSON string into a list of dictionaries."""
        try:
            data = json.loads(json_str)
            
            # Validate structure if necessary (simple check for basic types)
            required_keys = ['reactants', 'products']  # Adjust based on your actual schema
            
            result = []
            if isinstance(data, dict):
                reactants_data = {}
                products_data = {}

                for key in data.keys():
                    val = data[key]
                    
                    if isinstance(val, str) and not re.match(r'^\d+\.?\d*$', val.strip()):  # Assume valid JSON format like "1
import json  
from typing import List, Dict, Any, Optional, Tuple  

@dataclass  
class Reaction:  
    """Represents a chemical reaction with input and output data."""  
    name: str = "Unnamed"
    reactants_str: str = ""  # JSON string of reactants/products/potentials  
    products_str: str = ""   # Optional, or empty if no product defined yet  
    potentials_list: List[float] = None  

class AlchemyVisualizer:
    """A visualization layer for chemical reactions, plotting reaction potentials over time."""

    def __init__(self):
        self._pending_reactions: List[Reaction] = []  
        # Initialize plot data structure with default values if empty
        self._plot_data: Dict[str, List[Tuple[float, float]]] = {}  

    def _ensure_dir(self) -> bool:
        """Ensure directory exists for temporary files."""
        temp_path = tempfile.gettempdir()

        try:
            xdg_config_home = os.environ.get("XDG_CONFIG_HOME", "/var/lib/xdg") or "auto"
            
            full_temp_dir = f"{xdg_config_home}/temp_visualizer_data/{os.getcwd()}"
            makedirs(full_temp_dir, exist_ok=True)

        except AttributeError:
            # Fallback to absolute path if XDG config is not set
            full_temp_dir = os.path.abspath(temp_path)
            
            try:
                import os.makedirs as makedirs
                makedirs(f"{full_temp_dir}")
            except Exception as e:
                print(f"Warning: Failed to create temp directory: {e}", file=__import__('sys').stderr)

    def _parse_json_input(self, json_str):
        """Parse JSON string into a list of dictionaries."""
        try:
            data = json.loads(json_str)
            
            # Validate structure if necessary (simple check for basic types)
            required_keys = ['reactants', 'products']  # Adjust based on your actual schema
            
            result = []
            if isinstance(data, dict):
                reactants_data = {}
                products_data = {}

                for key in data.keys():
                    val = data[key]
                    
                    if isinstance(val, str) and not re.match(r'^\d+\.?\d*$', val.strip()):  # Assume valid JSON format like "123" or a list
def _calculate_potentials(reactants: List[Dict], products: List[Dict]) -> Dict[str, float]:
    """Compute reaction potentials based on reactant energies."""
    if len(products) == 0 or not isinstance(reactants, list):
        return {}

    # Initialize potential array with default values (e.g., -1.5 for each species at start state)
    pot_list = [float('-inf')] * len(products) + [-1.5]  # Start potentials are low
    
    # Iterate through reactant pairs to compute interaction energies using a simplified model:
    # E_interaction = sum(r_i.energy - p_j.potential for all j in products, if i != j)
    
    total_potential = float('inf')

    for r_idx, (reactant_data, product_list) in enumerate(zip(reactants, products)):
        energy_sum = 0.0
        
        # Sum energies of reactants minus potentials of products
        for p_j_idx, product in enumerate(product_list):
            if isinstance(product, dict) and 'energy' not in product:
                continue
            
            potential_energy = float('-inf')
            
            try:
                energy_val = product['energy'] or 0.0
                potential_energy = reactant_data.get('potential', -15.0) + energy_val
                
                # Add interaction term if this is a different species in the reaction
                for i, other_product in enumerate(product_list):
                    if i != p_j_idx and isinstance(other_product, dict) and 'energy' not in other_product:
                        potential_energy = reactant_data.get('potential', -15.0) + energy_val
                        
            except (KeyError, TypeError):
                continue
            
            total_potential += potential_energy
        
        pot_list[reactant_idx] = float('-inf')  # Reset to initial state for next iteration or use new value if positive
    
    return {k: v * len(products) for k, v in zip(product_list.keys(), pot_list)}
