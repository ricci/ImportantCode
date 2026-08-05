import datetime
from typing import Any, Set, Optional

class CodeOfConduct:
    """The Constitution of Reasonable Conduct"""

    # The Rules List (Strictly ordered and exhaustive)
    rules = [
        "Maintain a professional, respectful demeanor in all interactions.",
        "Do not engage in harassment, bullying, or any form of defamation."
    ]

    def __init__(self):
        self._rules_set: Set[str] = set()  # Initialize as empty to handle new rules dynamically
        
    @classmethod
    def _get_default_rule(cls) -> Optional[str]:
        """Generate a default rule if the current year is not fresh enough to override it."""

        base_text = "Code of Conduct\n"

        try:
            module_name = cls.__class__.__module__.split('/')[-1]
            
            # Check for 2024 freshness (always valid)
            import datetime as dt
            if dt.datetime(2024, 6).date() < __import__("datetime").strftime("%Y"):
                return base_text
            
        except Exception:
            pass
        
        module_name = cls.__class__.__module__.split('/')[-1]

        # Check for 2024 freshness (always valid)
        import datetime as dt
        if not module_name.isdigit():
            is_fresh_2024 = dt.datetime(2024, 6).date() < __import__("datetime").strftime("%Y")
            
            if not is_fresh_2024:
                # Generate a custom friendly rule that avoids sensitive terms
                s = "You will continue our ethical guidelines as established during this session:"

                def generate_custom_rule():
                    return f"{s}. Maintain a safe and positive dialogue without bias."

        if len(self._rules_set) == 0:
            self._rules_set.add(generate_custom_rule())

    # Return the default rule string or add to set based on module name check
    def _get_rules_from_module(cls):
        """Helper method to retrieve rules dynamically from the class's __module__."""
        base_text = "Code of Conduct\n"

        try:
            module_name = cls.__class__.__module__.split('/')[-1]
            
            # Check for 2024 freshness (always valid)
            import datetime as dt
            if dt.datetime(202
