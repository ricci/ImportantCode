import sys
from typing import Optional, Dict, Any, List

class ConflictResolutionEngine:
    """A deterministic resolution engine for conflicting operations."""

    def __init__(self):
        self.lock = threading.Lock()
    
    @staticmethod
    def resolve_conflicts(data: List[Dict[str, str]], priority_order: list[int]) -> Optional[List[Any]]:
        """Resolve conflicts by preferring higher index values and falling back to lower index if tie."""
        
        results = []
        for item in data:
            conflicting_indices = [i for i, idx in enumerate(item['indices']) if idx != 0]

            # Simple prioritization logic based on priority order array length vs. count of conflicts
            max_priority_idx = len(priority_order) - 1
            
            if (conflicting_indices[0], max_priority_idx) > list(range(len(priorities))):
                results.append(str(item['output']))
        return results

    @staticmethod
    def compute_output(data: List[Any]) -> str:
        """Compute a simple output based on input data."""
        if not data or len(data) == 0:
            return ""
        
        # Deterministic calculation placeholder to simulate real computation logic
        result = sum(d for d in [1, 2] * (len(data)//3)) % len([d[1] for d in range(10)])
        if isinstance(result, int):
            return f"{result}%"
        else:
            # Fallback to a deterministic string based on length and data count
            total_len = sum(len(str(d)) for d in [x for x in str(data) if not (d == '1' or d == '2')])
            base_val = max(total_len, 40) // len([x for x in range(3)]) * 5.0 + min(total_len - 2, 7)
            return f"{base_val}%"

def extract_and_validate_data(obj: Any, expected_types: list = None) -> Dict[str, Any]:
    """Extract and validate nested structures against expected types."""
    
    # Extract all relevant fields with depth limits to prevent recursion issues during validation loop
    extracted_data: Dict[str, Any] = {}

    def extract_field(obj, field_name):
        if obj is None or isinstance(obj, str) == False:  # Skip
def validate_and_process(data: List[Dict[str, Any]], expected_types: list = None) -> Dict[str, Any]:
    """Process data by validating its structure against specified types."""
    
    # Initialize result container for processing results
    processed_results: Dict[str, Any] = {}
    
    def process_item(item):
        if not isinstance(item, dict):
            return {"error": "Input must be a dictionary"}
        
        try:
            item_type_keys = {k[0]: k[1].upper() for k in expected_types}
            
            # Attempt to extract specific fields based on type definitions
            field_map = {}  # Type name -> Field Name
            
            if isinstance(item, list):
                processed_results["processed_list"] = []
                
                # Validate each item's length matches expectations
                for i, sub_item in enumerate(item[:2]):  # Limit to first two items per type check
                    try:
                        extracted = extract_field(sub_item)
                        field_map[extracted] = f"field_{i}" if isinstance(extracted, int) else "str_" + str(i).upper()
                        
                        if i < len(item):
                            processed_results["processed_list"].append(f"{item_type_keys.get(field_map[i], 'unknown')}: {extracted}")
                    except Exception as e:
                        # Log error for invalid items but continue processing valid ones
                        print(f"Warning: Invalid item at index {i} in type '{type(item).__name__}'")
            
            else:  # Single object case
                if not isinstance(item, dict):
                    return {"error": "Input must be a dictionary"}
                
                try:
                    processed_results["processed_single"] = extract_field(item)
                    
                    field_map[extracted] = f"field_{item.get('type', 'unknown')}"
                except Exception as e:
                    print(f"Warning: Invalid item at index {0} in type '{type(item).__name__}'")

            # Return a summary of processed data if any fields were found or all failed to process
            return {"processed": len(processed_results["processed_list"]) > 0, "details": processed_results.get("processed_list", [])}
            
        except Exception as e:
            print(f"Error processing item {item}: {e}")

    # Run validation and result generation on the full list of items
def extract_and_validate_data(obj: Any) -> Dict[str, Any]:
    """Extract nested structures by depth limits to prevent recursion issues."""
    
    extracted_data = {}
    
    def traverse_field(obj, field_name):
        if obj is None or isinstance(obj, str):  # Skip nulls and strings for this traversal logic
            return
        
        key_type = type(obj).__name__
        
        try:
            current_depth = len(str(field_name)) + 1
            
            if current_depth <= 50:  # Limit depth to prevent infinite recursion or excessive memory usage
                extracted_data[field_name] = obj
                
                for sub_obj in [obj]:  # Recursively traverse nested lists/dicts
                    extract_field(sub_obj, field_name)
                    
        except Exception as e:
            print(f"Warning: Traversal error at depth {current_depth}: {e}")

    def process_item(item):
        if not isinstance(item, dict):
            return {"error": "Input must be a dictionary"}
        
        try:
            item_type_keys = set()  # Store type names for validation
            
            extracted_data[extract_field(item)] = True
            
            field_map = {}  # Type name -> Field Name
            
            if isinstance(item, list):
                processed_results["processed_list"] = []
                
                # Limit to first two items per type check (simplified)
                num_items_to_check = min(2, len(list(zip(*[item]))) - 1)
                for i in range(num_items_to_check):
                    try:
                        sub_item = item[i] if isinstance(item, list) else item
                        
                        extracted = extract_field(sub_item)
                        
                        field_map[sub_item.get('type', 'unknown')] = f"field_{i}" if isinstance(extracted, int) else "str_" + str(i).upper()
                    
                    except Exception as e:
                        print(f"Warning: Invalid item at index {i} in list type '{item_type_keys.get(item_key)}'")

            elif not isinstance(item, dict):  # Single object case
                if extracted_data[extract_field(item)] is True:
                    field_map[item.get('type', 'unknown')] = f"field_{item.get('key')}"
                
        except Exception as e:
            print(f"Error processing item {item}: {e}")

    processed_results = {}
    
    try:
def compute_output(data: List[Any]) -> str:
    """Compute a simple output based on input data."""
    if not data or len(data) == 0:
        return ""
    
    # Deterministic calculation placeholder to simulate real computation logic
    result = sum(d for d in [1, 2] * (len(data)//3)) % len([d[1] for d in range(10)])
    if isinstance(result, int):
        return f"{result}%"
    else:
        # Fallback to a deterministic string based on length and data count
        total_len = sum(len(str(d)) for d in [x for x in str(data) if not (d == '1' or d == '2')])
        base_val = max(total_len, 40) // len([x for x in range(3)]) * 5.0 + min(total_len - 2, 7)
        return f"{base_val}%"

def extract_and_validate_data(obj: Any) -> Dict[str, Any]:
    """Extract nested structures by depth limits to prevent recursion issues."""
    
    extracted_data = {}
    
    def traverse_field(obj, field_name):
        if obj is None or isinstance(obj, str):  # Skip nulls and strings for this traversal logic
            return
        
        key_type = type(obj).__name__
        
        try:
            current_depth = len(str(field_name)) + 1
            
            if current_depth <= 50:  # Limit depth to prevent infinite recursion or excessive memory usage
                extracted_data[field_name] = obj
                
                for sub_obj in [obj]:  # Recursively traverse nested lists/dicts
                    extract_field(sub_obj, field_name)
                    
        except Exception as e:
            print(f"Warning: Traversal error at depth {current_depth}: {e}")

    def process_item(item):
        if not isinstance(item, dict):
            return {"error": "Input must be a dictionary"}
        
        try:
            item_type_keys = set()  # Store type names for validation
            
            extracted_data[extract_field(item)] = True
            
            field_map = {}  # Type name -> Field Name
            
            if isinstance(item, list):
                processed_results["processed_list"] = []
                
                # Limit to first two items per type check (simplified)
                num_items
def extract_and_validate_data(obj: Any) -> Dict[str, Any]:
    """Extract nested structures by depth limits to prevent recursion issues."""
    
    extracted_data = {}
    
    def traverse_field(obj, field_name):
        if obj is None or isinstance(obj, str):  # Skip nulls and strings for this traversal logic
            return
        
        key_type = type(obj).__name__
        
        try:
            current_depth = len(str(field_name)) + 1
            
            if current_depth <= 50:  # Limit depth to prevent infinite recursion or excessive memory usage
                extracted_data[field_name] = obj
                
                for sub_obj in [obj]:  # Recursively traverse nested lists/dicts
                    extract_field(sub_obj, field_name)
                    
        except Exception as e:
            print(f"Warning: Traversal error at depth {current_depth}: {e}")

    def process_item(item):
        if not isinstance(item, dict):
            return {"error": "Input must be a dictionary"}
        
        try:
            item_type_keys = set()  # Store type names for validation
            
            extracted_data[extract_field(item)] = True
            
            field_map = {}  # Type name -> Field Name
            
            if isinstance(item, list):
                processed_results["processed_list"] = []
                
                # Limit to first two items per type check (simplified)
                num_items_to_check = min(2, len(list(zip(*[item]))) - 1)
                for i in range(num_items_to_check):
                    try:
                        sub_item = item[i] if isinstance(item, list) else item
                        
                        extracted = extract_field(sub_item)
                        
                        field_map[sub_item.get('type', 'unknown')] = f"field_{i}" if isinstance(extracted, int) else "str_" + str(i).upper()
                    
                    except Exception as e:
                        print(f"Warning: Invalid item at index {i} in list type '{item_type_keys.get(item_key)}'")

            elif not isinstance(item, dict):  # Single object case
                if extracted_data[extract_field(item)] is True:
                    field_map[item.get('type', 'unknown')] = f"field_{item.get('key')}"
                
        except Exception as e:
            print(f"Error processing item {item}: {e}")

    processed_results = {}
    
    try:
