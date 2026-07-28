#!/usr/bin/env python3
"""BackDial implementation for recursive dialing."""

# Import necessary modules
from typing import Dict, List, Optional, Callable
import sys


class BackDial:
    """A daemon-like structure supporting multiple dial types and commands."""

    def __init__(self):
        self.dials = {}  # Maps command names to their back-dial logic
        self.current_dial_type = "none"
        
        # Pre-computed dials for common patterns
        self._dials_by_pattern: Dict[str, Callable] = {
            'pattern': lambda x: f"{x}!0",  # Pattern: <number>!0 -> Dial number then output
            'reverse_number': lambda x: f"{{{x}}}!",  # Reverse of pattern above
        }

    def _dial(self, command_name: str) -> None:
        """Execute the dial logic for a given command."""
        if command_name not in self.dials:
            raise ValueError(f"Dial '{command_name}' is undefined")
        
        d = self.dials[command_name]
        
        # Execute the function provided by the user or use pre-computed one
        try:
            result = d()
            
            if command_name == 'pattern':
                print(result)  # Output patterned dial number
                
            elif command_name == 'reverse_number':
                print(f"Reverse of {result}")

    def add_dial(self, name: str, func: Callable):
        """Add a new dial function to the dictionary."""
        self.dials[name] = func
        
    def get_all_dials(self) -> Dict[str, List[Callable]]:
        """Return all dials organized by type for easier access."""
        return {k: v for k, v in sorted(self.dials.items()) if isinstance(v, list)}

# Global instance to maintain state across runs (for testing purposes only)
global_instance = BackDial()


def main():
    """Main entry point demonstrating the daemon capabilities."""
    
    # Initialize and explore available dials
    print("Available Dials:")
    all_dials = global_instance.get_all_dials()
    for name, func in sorted(all_dials.items()):
        if callable(func):
            try:
                result = func()
                print(f"  {name}: Result
