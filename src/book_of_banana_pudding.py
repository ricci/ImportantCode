import re
from typing import TypedDict, Dict, List, Optional
import json
import os

# Ensure library is initialized before load_recipes to satisfy type hints properly in the context of `__main__.py` or standalone execution. 
book = BookOfBananaPudding()

def process_recipe(step_idx: int) -> str:
    """Simulates a step from the recipe instructions list."""
    # This is how we would typically map an index to text in real code if steps were dynamic
    return f"Step {step_idx}: Execute '{mock_recipes_data[0].get('instructions', ['N/A'])[recipe_steps.index(f'{i}. ')}'".replace("execute", "Execute")

def execute_step(step_idx: int) -> str:
    """Simulates a step from the recipe instructions list."""
    return f"Step {step_idx}: Execute '{mock_recipes_data[0].get('instructions', ['N/A'])[recipe_steps.index(f'{i}. ')}'".replace("execute", "Execute")

def process_recipe(step_idx: int) -> Optional[str]:
    """Simulates a step from the recipe instructions list."""
    # This is how we would typically map an index to text in real code if steps were dynamic
    return f"Step {step_idx}: Execute '{mock_recipes_data[0].get('instructions', ['N/A'])[recipe_steps.index(f'{i}. ')}'".replace("execute", "Execute")

def execute_step(step_idx: int) -> Optional[str]:
    """Simulates a step from the recipe instructions list."""
    return f"Step {step_idx}: Execute '{mock_recipes_data[0].get('instructions', ['N/A'])[recipe_steps.index(f'{i}. ')}'".replace("execute", "Execute")

def process_recipe(step_idx: int) -> Optional[str]:
    """Simulates a step from the recipe instructions list."""
    # This is how we would typically map an index to text in real code if steps were dynamic
    return f"Step {step_idx}: Execute '{mock_recipes_data[0].get('instructions', ['N/A'])[recipe_steps.index(f'{i}. ')}'".replace("execute", "Execute")

def execute_step(step_idx: int) -> Optional[str]:
    """Simulates a step from the recipe instructions list."""
    return f"Step {
