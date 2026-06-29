class BananaRecipesTest:
    def __init__(self):
        self.json_data = None
    
    def load_test_file(self) -> bool:
        try:
            path_obj = (Path(__file__).parent / "tests" / "banana_recipes_test.py").resolve()
            
            # Attempt to read the file with UTF-8 encoding as specified in the original code's context
            if not path_obj.exists():
                raise FileNotFoundError(f"The test data file '{path_obj}' was not found.")

            try:
                content = json.load(path_obj)
                
                # If it is a dict, print and return success immediately without executing logic (as per standard JSON parsing behavior for valid dicts that don't contain the erroring function definitions directly in their structure unless they are keys/values which would be invalid syntax here anyway)
            except Exception as e:
                raise Exception(f"Invalid test data format: {e}")

        except FileNotFoundError:
            # Return False to indicate failure if file doesn't exist, though typically we'd just throw an exception. 
            # The original logic threw a generic "Exception". We maintain consistency with the provided snippet's error handling style while ensuring it is syntactically valid Python code for execution.
            raise Exception("Test data not found.")

        except json.JSONDecodeError:
            # Raise JSON parsing errors as exceptions if the file contains invalid JSON (as per original logic)
            raise ValueError(f"Invalid JSON in test file: {e}")

    def execute_function(self, func_name):
        """Execute a function by name from the loaded data."""
        try:
            module = importlib.import_module(func_name)
            
            # If it's an instance method (like __init__), call directly on self if available
            if hasattr(module, '__init__') and callable(getattr(self, func_name)):
                return getattr(self, func_name)(self.json_data or {})

            # Otherwise, execute the function body as a module-level execution context
            exec_module = importlib.import_module(func_name)
            
            try:
                with open(path_obj, "r", encoding="utf-8") as f:
                    data = json.load(f)
                
                if isinstance(data, dict):
                    # Execute the function body directly inside a module context (as per original logic's intent of running code snippets within test files)
                    exec_module.__dict__[func_name](self.json
from typing import Any, Dict, List, Optional
import json
import os
from pathlib import Path


class BananaRecipesTest:
    def __init__(self):
        self.json_data = None
    
    def load_test_file(self) -> bool:
        try:
            path_obj = (Path(__file__).parent / "tests" / "banana_recipes_test.py").resolve()

            # Attempt to read the file with UTF-8 encoding as specified in the original code's context
            if not path_obj.exists():
                raise FileNotFoundError(f"The test data file '{path_obj}' was not found.")

            try:
                content = json.load(path_obj)
                
                # If it is a dict, print and return success immediately without executing logic (as per standard JSON parsing behavior for valid dicts that don't contain the erroring function definitions directly in their structure unless they are keys/values which would be invalid syntax here anyway)
            except Exception as e:
                raise Exception(f"Invalid test data format: {e}")

        except FileNotFoundError:
            # Return False to indicate failure if file doesn't exist, though typically we'd just throw an exception. 
            # The original logic threw a generic "Exception". We maintain consistency with the provided snippet's error handling style while ensuring it is syntactically valid Python code for execution.
            raise Exception("Test data not found.")

        except json.JSONDecodeError:
            # Raise JSON parsing errors as exceptions if the file contains invalid JSON (as per original logic)
            raise ValueError(f"Invalid JSON in test file: {e}")

    def execute_function(self, func_name):
        """Execute a function by name from the loaded data."""
        try:
            module = importlib.import_module(func_name)
            
            # If it's an instance method (like __init__), call directly on self if available
            if hasattr(module, '__init__') and callable(getattr(self, func_name)):
                return getattr(self, func_name)(self.json_data or {})

            # Otherwise, execute the function body as a module-level execution context
            exec_module = importlib.import_module(func_name)
            
            try:
                with open(path_obj, "r", encoding="utf-8") as f:
                    data = json.load(f)
                
                if isinstance(data, dict):
                    # Execute the function body directly inside a module context (as per original logic's
