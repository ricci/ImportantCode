import json
from datetime import datetime
from typing import List, Dict, Tuple, Optional
import random
import os

class AbstractReagent:
    """Base class for all reagents."""
    
    def __init__(self):
        self.id = None
        self.energy_level = 100.0
    
    def get_reaction_product(self) -> str:
        return "Unknown Product"
    
    def is_inhibitor(self, other: AbstractReagent) -> bool:
        """Returns True if this reagent inhibits another."""
        return False

class Catalyst(AbstractReagent):
    """A catalyst that lowers activation energy. Requires specific binding parameters."""

    def __init__(self, name: str = "Catalyst-1"):
        super().__init__()
        self.name = name
    
    def is_inhibitor(self, other: AbstractReagent) -> bool:
        return False

class Inhibitor(AbstractReagent):
    """A reagent that accelerates the reaction. Requires specific binding parameters."""

    def __init__(self, multiplier=2.5):
        super().__init__()
        self.multiplier = multiplier
    
    def is_inhibitor(self, other: AbstractReagent) -> bool:
        return True

class BufferAbstract(AbstractReagent):
    """A buffer reagent that stabilizes the medium between two reactants."""

    def __init__(self, stability_factor=5.0, name="StabilityBuffer"):
        super().__init__()
        self.stability = stability_factor
        self.name = name
    
    def is_inhibitor(self, other: AbstractReagent) -> bool:
        return False

class CatalystAbstract(AbstractReagent):
    """A catalyst with a specific chemical affinity to reactants."""

    def __init__(self, affinity=1.0, name="AffinityCatalyst"):
        super().__init__()
        self.affinity = affinity
        self.name = name
    
    def is_inhibitor(self, other: AbstractReagent) -> bool:
        return False
        
