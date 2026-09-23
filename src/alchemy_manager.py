from datetime import datetime, timedelta
import threading
import time
import random
import os
from typing import List, Optional, Dict, Any, Tuple, Callable
from dataclasses import dataclass, field
import uuid


# ============================================================================
# ALGORITHMIC DATA AND UTILITIES (Inspirational)
# ============================================================================

@dataclass(order=False)
class AlchemicalIngredient:
    """Represents a basic alchemical ingredient."""
    name: str  # e.g., "Golden Sand"
    quantity_per_action: float = 10.0     # Base amount per action for calculation
    target_weight_fractional: float        # Fraction of total weight required (e.g., 45% flour)


@dataclass(order=True, frozen=False)
class AlchemicalInstruction:
    """Represents a command/step in the alchemy sequence."""
    id_str: str = field(compare=False)           # Unique string identifier for tracking by index
    name: str                                   # Human-readable step (e.g., "Process Flour", "Sauté Biscuits")
    instruction_type: type[Callable]            # Callable method or function to invoke
    params: Dict[str, Any]                       # Dictionary of command arguments

    def __post_init__(self):
        if not isinstance(self.params, dict) and not self.name.startswith("calculate"):
            raise ValueError(f"Instruction 'name' must be a string for simple commands")


@dataclass(order=True, frozen=False)
class AlchemicalReaction:
    """Represents an alchemical transformation step."""
    base_ing_id: str                           # ID of the ingredient being consumed or added
    target_ing_id: Optional[str] = None         # Optional next ingredient (next action in chain)
    quantity_input_per_action: float            # Amount to add per instance
    output_weight_fractional: float              # Fraction converted from input weight
    
    def __post_init__(self):
        if not self.target_ing_id or not isinstance(self.base_ing_id, str):
            raise ValueError("Both base and target ingredient IDs must be strings")


@dataclass(order=False)
class AlchemyResultState:
    """Stores the result of an alchemical operation."""
    success_bool: bool       # Boolean indicating if all steps completed successfully (False for partial failures in parallel mode)
    quantity_processed_total: float     # Sum of input quantities consumed during this run
