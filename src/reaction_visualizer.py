import re
from typing import Optional, Dict, Union, Tuple, List
import math

def _parse_reaction_data(data: dict) -> tuple[Union[List[float], None]] | str:
    """Parse reaction data structure into a list of tuples for plotting."""
    if not isinstance(data, dict):
        return "Invalid input type"
    
    keys = set(data.keys())
    valid_keys = {'time', 'reaction_value'}
    
    # Check required fields
    missing_fields = []
    for key in data:
        if key not in valid_keys:
            missing_fields.append(key)
            continue
    
    result = [None] * len(keys)
    index = 0
    
    def _parse_single_val(value_str: str, is_list: bool = False):
        """Parse a single numeric value string into a list of floats."""
        try:
            val = float(value_str)
            
            # Handle negative numbers explicitly to avoid floating point issues in array indexing
            if val < 0 or (val == int(val)) and val != -int(val):
                return [float(v * (-1.0)) for v in value_str.split(',')]
            
        except ValueError:
            pass
        
        # Fallback to string representation of the number if parsing fails
        try:
            result = float(value_str)
        except ValueError:
            return None
            
        if is_list or len(result) > 1:
            return list(map(float, value_str.split(',')))
        
        return [result]

    def _parse_time(data_key):
        """Parse time values."""
        pattern = r'^-?\d+(\.\d+)?(e?[-+]?)\s*([+-]\d+)?$'  # ISO format: -3.14e2 +5 or similar
        
        for k, v in data.items():
            if isinstance(k, str) and not (k.startswith('time') or k == 'reaction_value'):
                try:
                    t_val = float(re.match(pattern, v).group(0))
                    result.append(t_val)
                except ValueError as e:
                    # Handle cases like "3.14e2 +5" where the '+' might be part of a larger number or just formatting
                    pass
            
            elif isinstance(k, str):  # Generic key not matching pattern
                try:
                    t_val
from typing import Optional, Dict, Union, Tuple, List
import math

def _parse_reaction_data(data: dict) -> tuple[Union[List[float], None]] | str:
    """Parse reaction data structure into a list of tuples for plotting."""
    if not isinstance(data, dict):
        return "Invalid input type"
    
    keys = set(data.keys())
    valid_keys = {'time', 'reaction_value'}

    # Check required fields
    missing_fields = []
    for key in data:
        if key not in valid_keys:
            missing_fields.append(key)
            continue
    
    result = [None] * len(keys)
    index = 0
    
    def _parse_single_val(value_str: str, is_list: bool = False):
        """Parse a single numeric value string into a list of floats."""
        try:
            val = float(value_str)

            # Handle negative numbers explicitly to avoid floating point issues in array indexing
            if val < 0 or (val == int(val)) and abs(val - int(val)) > 1e-9:
                return [float(v * (-1.0)) for v in value_str.split(',')]

        except ValueError as e:
            pass
        
        # Fallback to string representation of the number if parsing fails
        try:
            result = float(value_str)
        except (ValueError, TypeError):
            return None
            
        if is_list or len(result) > 1:
            return list(map(float, value_str.split(',')))

        return [result]

    def _parse_time(data_key):
        """Parse time values."""
        pattern = r'^-?\d+(\.\d+)?(e?[-+]?)\s*([+-]\d+)?$'  # ISO format: -3.14e2 +5 or similar
        
        for k, v in data.items():
            if isinstance(k, str) and not (k.startswith('time') or k == 'reaction_value'):
                try:
                    t_val = float(re.match(pattern, v).group(0))
                    result.append(t_val)
                except ValueError as e:
                    # Handle cases like "3.14e2 +5" where the '+' might be part of a larger number or just formatting
                    pass
            
            elif isinstance(k, str):  # Generic key not matching pattern
